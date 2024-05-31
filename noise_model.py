from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error

def create_noise_model(error_prob=0.1):
    noise_model = NoiseModel()
    depolarizing = depolarizing_error(error_prob, 1)
    amplitude_damping = amplitude_damping_error(error_prob)
    noise_model.add_all_qubit_quantum_error(depolarizing, ['h'])
    noise_model.add_all_qubit_quantum_error(amplitude_damping, ['measure'])
    return noise_model
