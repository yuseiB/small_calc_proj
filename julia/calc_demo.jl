function free_space_path_loss_db(distance_m::Float64, frequency_hz::Float64)
    if distance_m <= 0 || frequency_hz <= 0
        error("distance_m and frequency_hz must be positive")
    end
    c = 299_792_458.0
    return 20.0 * log10(4.0 * π * distance_m * frequency_hz / c)
end

function rms(samples::Vector{Float64})
    if isempty(samples)
        error("samples must not be empty")
    end
    return sqrt(sum(x^2 for x in samples) / length(samples))
end

function linear_model_predict(weights::Vector{Float64}, bias::Float64, features::Vector{Float64})
    if length(weights) != length(features)
        error("weights and features must have the same length")
    end
    return sum(weights .* features) + bias
end

function demo()
    fspl = free_space_path_loss_db(1000.0, 2.4e9)
    signal_rms = rms([0.1, -0.1, 0.2, -0.2, 0.0])
    y_hat = linear_model_predict([0.6, -0.2, 0.1], 1.0, [2.0, 0.5, -1.0])

    println("FSPL(1 km, 2.4 GHz): $(round(fspl, digits=3)) dB")
    println("RMS([0.1,-0.1,0.2,-0.2,0]): $(round(signal_rms, digits=6))")
    println("Linear model prediction: $(round(y_hat, digits=6))")
end

demo()
