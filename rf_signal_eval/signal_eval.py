"""RF信号のダウンコンバートと位相推定の簡易評価。"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class SimulationConfig:
    duration_s: float = 10e-6
    sample_rate_hz: float = 200e6
    rf_freq_hz: float = 20e6
    ref_freq_hz: float = 20e6
    damping_tau_s: float = 2.0e-6
    rf_phase_rad: float = np.deg2rad(35.0)
    ref_phase_rad: float = 0.0
    lowpass_cutoff_hz: float = 2.0e6


def make_time_axis(duration_s: float, sample_rate_hz: float) -> np.ndarray:
    dt = 1.0 / sample_rate_hz
    n = int(duration_s * sample_rate_hz)
    return np.arange(n) * dt


def generate_damped_rf(t: np.ndarray, freq_hz: float, tau_s: float, phase_rad: float) -> np.ndarray:
    envelope = np.exp(-t / tau_s)
    return envelope * np.cos(2.0 * np.pi * freq_hz * t + phase_rad)


def generate_reference(t: np.ndarray, freq_hz: float, phase_rad: float) -> np.ndarray:
    return np.cos(2.0 * np.pi * freq_hz * t + phase_rad)


def lowpass_ema(x: np.ndarray, sample_rate_hz: float, cutoff_hz: float) -> np.ndarray:
    dt = 1.0 / sample_rate_hz
    rc = 1.0 / (2.0 * np.pi * cutoff_hz)
    alpha = dt / (rc + dt)

    y = np.empty_like(x)
    y[0] = x[0]
    for i in range(1, len(x)):
        y[i] = y[i - 1] + alpha * (x[i] - y[i - 1])
    return y


def downconvert_iq(
    rf_signal: np.ndarray,
    t: np.ndarray,
    ref_freq_hz: float,
    ref_phase_rad: float,
    sample_rate_hz: float,
    lowpass_cutoff_hz: float,
) -> tuple[np.ndarray, np.ndarray]:
    lo_i = np.cos(2.0 * np.pi * ref_freq_hz * t + ref_phase_rad)
    lo_q = -np.sin(2.0 * np.pi * ref_freq_hz * t + ref_phase_rad)

    mixed_i = rf_signal * lo_i * 2.0
    mixed_q = rf_signal * lo_q * 2.0

    i_baseband = lowpass_ema(mixed_i, sample_rate_hz, lowpass_cutoff_hz)
    q_baseband = lowpass_ema(mixed_q, sample_rate_hz, lowpass_cutoff_hz)
    return i_baseband, q_baseband


def estimate_phase(i_baseband: np.ndarray, q_baseband: np.ndarray, tail_ratio: float = 0.5) -> float:
    start = int(len(i_baseband) * (1.0 - tail_ratio))
    i_mean = np.mean(i_baseband[start:])
    q_mean = np.mean(q_baseband[start:])
    return float(np.arctan2(q_mean, i_mean))


def run_simulation(config: SimulationConfig) -> dict[str, np.ndarray | float]:
    t = make_time_axis(config.duration_s, config.sample_rate_hz)
    rf_signal = generate_damped_rf(t, config.rf_freq_hz, config.damping_tau_s, config.rf_phase_rad)

    i_baseband, q_baseband = downconvert_iq(
        rf_signal=rf_signal,
        t=t,
        ref_freq_hz=config.ref_freq_hz,
        ref_phase_rad=config.ref_phase_rad,
        sample_rate_hz=config.sample_rate_hz,
        lowpass_cutoff_hz=config.lowpass_cutoff_hz,
    )
    estimated_phase = estimate_phase(i_baseband, q_baseband)

    return {
        "t": t,
        "rf_signal": rf_signal,
        "i_baseband": i_baseband,
        "q_baseband": q_baseband,
        "estimated_phase_rad": estimated_phase,
    }


def main() -> None:
    config = SimulationConfig()
    result = run_simulation(config)

    actual_diff = config.rf_phase_rad - config.ref_phase_rad
    actual_diff = float(np.arctan2(np.sin(actual_diff), np.cos(actual_diff)))
    estimated = float(result["estimated_phase_rad"])

    print(f"actual phase difference [rad]:    {actual_diff:.6f}")
    print(f"estimated phase difference [rad]: {estimated:.6f}")


if __name__ == "__main__":
    main()
