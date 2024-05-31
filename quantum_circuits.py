from qiskit import QuantumCircuit

def clean_circuit(num_qubits):
    qc = QuantumCircuit(num_qubits, num_qubits)
    for q in range(num_qubits):
        qc.h(q)
        qc.measure(q, q)
    return qc

def noisy_circuit(num_qubits):
    qc = QuantumCircuit(num_qubits, num_qubits)
    for q in range(num_qubits):
        qc.h(q)
        qc.measure(q, q)
    return qc
