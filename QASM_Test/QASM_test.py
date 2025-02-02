from qiskit import QuantumCircuit

def circuit1():
    qasm_code = qasm_string = """
    OPENQASM 2.0;
    include "qelib1.inc";

    qreg q[4];

    // Gate: CZ**0.15524282950959892
    u3(pi*0.5,0,pi*0.25) q[0];
    u3(pi*0.5,0,pi*0.75) q[1];
    sx q[0];
    cx q[0],q[1];
    rx(pi*0.4223785852) q[0];
    ry(pi*0.5) q[1];
    cx q[1],q[0];
    sxdg q[1];
    s q[1];
    cx q[0],q[1];
    u3(pi*0.5,pi*0.8276214148,pi*1.0) q[0];
    u3(pi*0.5,pi*0.3276214148,pi*1.0) q[1];

    """

    # Convert QASM string to QuantumCircuit
    qc1 = QuantumCircuit.from_qasm_str(qasm_code)
    return qc1

# Draw the circuit

def circuit2():
    theta=0.15524282950959892
    qc2 = QuantumCircuit(2)
    qc2.crz(theta, 0, 1)
    return qc2


qc1=circuit1()
qc2=circuit2()
print(qc1==qc2)
