import math
from statistics import fmean


def free_space_path_loss_db(distance_m: float, frequency_hz: float) -> float:
    if distance_m <= 0 or frequency_hz <= 0:
        raise ValueError("distance_m and frequency_hz must be positive")
    c = 299_792_458.0
    return 20.0 * math.log10(4.0 * math.pi * distance_m * frequency_hz / c)


def rms(samples: list[float]) -> float:
    if not samples:
        raise ValueError("samples must not be empty")
    return math.sqrt(fmean(x * x for x in samples))


def linear_model_predict(weights: list[float], bias: float, features: list[float]) -> float:
    if len(weights) != len(features):
        raise ValueError("weights and features must have the same length")
    return sum(w * x for w, x in zip(weights, features)) + bias


def demo() -> None:
    fspl = free_space_path_loss_db(distance_m=1_000.0, frequency_hz=2.4e9)
    signal_rms = rms([0.1, -0.1, 0.2, -0.2, 0.0])
    y_hat = linear_model_predict([0.6, -0.2, 0.1], bias=1.0, features=[2.0, 0.5, -1.0])

    print(f"FSPL(1 km, 2.4 GHz): {fspl:.3f} dB")
    print(f"RMS([0.1,-0.1,0.2,-0.2,0]): {signal_rms:.6f}")
    print(f"Linear model prediction: {y_hat:.6f}")


if __name__ == "__main__":
    demo()
