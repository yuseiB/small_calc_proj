#include <cmath>
#include <iostream>
#include <stdexcept>
#include <vector>

double free_space_path_loss_db(double distance_m, double frequency_hz) {
    if (distance_m <= 0 || frequency_hz <= 0) {
        throw std::invalid_argument("distance_m and frequency_hz must be positive");
    }
    constexpr double c = 299792458.0;
    constexpr double pi = 3.14159265358979323846;
    return 20.0 * std::log10(4.0 * pi * distance_m * frequency_hz / c);
}

double rms(const std::vector<double>& samples) {
    if (samples.empty()) {
        throw std::invalid_argument("samples must not be empty");
    }
    double sum_sq = 0.0;
    for (double x : samples) {
        sum_sq += x * x;
    }
    return std::sqrt(sum_sq / samples.size());
}

double linear_model_predict(const std::vector<double>& weights, double bias,
                            const std::vector<double>& features) {
    if (weights.size() != features.size()) {
        throw std::invalid_argument("weights and features must have the same length");
    }
    double y = bias;
    for (size_t i = 0; i < weights.size(); ++i) {
        y += weights[i] * features[i];
    }
    return y;
}

int main() {
    const double fspl = free_space_path_loss_db(1000.0, 2.4e9);
    const double signal_rms = rms({0.1, -0.1, 0.2, -0.2, 0.0});
    const double y_hat = linear_model_predict({0.6, -0.2, 0.1}, 1.0, {2.0, 0.5, -1.0});

    std::cout << "FSPL(1 km, 2.4 GHz): " << fspl << " dB\n";
    std::cout << "RMS([0.1,-0.1,0.2,-0.2,0]): " << signal_rms << "\n";
    std::cout << "Linear model prediction: " << y_hat << "\n";
    return 0;
}
