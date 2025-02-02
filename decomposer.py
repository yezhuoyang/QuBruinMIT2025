from qiskit import QuantumCircuit, transpile
import numpy as np


def example():
    # Define theta
    theta = np.pi / 4

    # Create a 2-qubit circuit and add CRX(theta) with qubit 0 as control and qubit 1 as target
    qc = QuantumCircuit(3)
    qc.ccx(0, 1, 2)

    print("Original circuit:")
    print(qc.draw())

    # Transpile to a basis of single-qubit (u) gates plus CZ
    decomposed_qc = transpile(
        qc,
        basis_gates=['cz', 'rx', 'ry', 'rz'],   # or e.g. ['rx', 'ry', 'rz', 'cz']
        optimization_level=3
    )

    print("\nDecomposed circuit (using only single-qubit gates and CZ):")
    print(decomposed_qc.draw())


def decompose_from_file(filename):
    qc = QuantumCircuit.from_qasm_file(filename)
    # Transpile to a basis of single-qubit (u) gates plus CZ
    decomposed_qc = transpile(
        qc,
        basis_gates=['cz', 'rx', 'ry', 'rz'],   # or e.g. ['rx', 'ry', 'rz', 'cz']
        optimization_level=3
    )

    print("\nDecomposed circuit (using only single-qubit gates and CZ):")
    print(decomposed_qc.draw())    
    #return qc



def C1circuit1():
    qc = QuantumCircuit.from_qasm_file("../qasm/1.2.qasm")
    # Transpile to a basis of single-qubit (u) gates plus CZ
    decomposed_qc = transpile(
        qc,
        basis_gates=['cz', 'rx', 'ry', 'rz'],   # or e.g. ['rx', 'ry', 'rz', 'cz']
        optimization_level=3
    )

    print("\nDecomposed circuit (using only single-qubit gates and CZ):")
    print(decomposed_qc.draw())    
    #return qc









if __name__ == "__main__":
    C1circuit1()
