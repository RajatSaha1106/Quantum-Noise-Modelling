from Num_Picker import num_picker
from quantum_circuits import clean_circuit, noisy_circuit
from noise_model import create_noise_model
from text_shift import shift_plaintext
from qiskit import Aer, transpile, assemble
from qiskit.visualization import plot_histogram

# Define the string and determine the number of qubits
string = "MyHouseisInFlames"
num_qubits = num_picker(string)

# Create clean and noisy circuits
clean_circuit = clean_circuit(num_qubits)
noisy_circuit = noisy_circuit(num_qubits)

# Get backend simulator
sim = Aer.get_backend('qasm_simulator')

# Transpile and assemble the clean circuit
transpiled_clean = transpile(clean_circuit, sim)
job_clean = assemble(transpiled_clean, shots=1)
result_clean = sim.run(job_clean).result()
counts_clean = result_clean.get_counts()
print("Measurement Result without Noise: ")
print(counts_clean)

# Create noise model
noise_model = create_noise_model()

# Simulate the circuit with noise
job_noisy = assemble(transpiled_clean, shots=1024)
result_noisy = sim.run(job_noisy, noise_model=noise_model).result()
counts_noisy = result_noisy.get_counts()
print("Measurement Result with Noise: ")
print(counts_noisy)

# Example plaintext shifting
plaintext = "HELLO WORLD"
shift_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
shifted_text = shift_plaintext(plaintext, shift_values)
print("Original:", plaintext)
print("Shifted:", shifted_text)
