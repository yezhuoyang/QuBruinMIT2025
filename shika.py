from qiskit import QuantumCircuit
import math
from bloqade import move
from kirin.passes import aggressive
from iquhack_scoring import MoveScorer

pi = math.pi

# GATES

@move.vmove
def main():
    q = move.NewQubitRegister(3)
    qubits = [q[0], q[1], q[2]]
    indices = [0, 1, 2]
    state = move.Init(qubits=qubits, indices=indices)

    # 1st CZ
    state.gate[[0,1]] = move.Move(state.storage[[0,1]]) 
    state = move.GlobalCZ(atom_state=state) 
    state.storage[[0,1]] = move.Move(state.gate[[0,1]]) # move back 

    # 1st Rx: -pi/4
    state.gate[[1]] = move.Move(state.storage[[1]])
    state = move.LocalXY(atom_state=state, x_exponent=-0.25 * pi,indices=[2], 
                         axis_phase_exponent=0.0)
    state.storage[[1]] = move.Move(state.gate[[1]])

    # 2nd CZ 
    state.gate[[1,2]] = move.Move(state.storage[[1,2]]) 
    state = move.GlobalCZ(atom_state=state) 
    state.storage[[1,2]] = move.Move(state.gate[[1,2]]) # move back 

    # 2nd Rx: pi/4 
    state.gate[[1]] = move.Move(state.storage[[1]])
    state = move.LocalXY(atom_state=state, x_exponent=0.25 * pi,indices=[2], 
                         axis_phase_exponent=0.0)
    state.storage[[1]] = move.Move(state.gate[[1]])

    # 3rd CZ 
    state.gate[[0,1]] = move.Move(state.storage[[0,1]]) 
    state = move.GlobalCZ(atom_state=state) 
    state.storage[[0,1]] = move.Move(state.gate[[0,1]]) # move back 



    move.Execute(state)


expected_qasm = """
OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
qc.cz(1, 2)
rx(-0.78539816339) q[2]; // -π/4 in radians
"""

# subroutines are not allowed by the scoring.
# run this pass to inline the subroutines
aggressive.Fold(move.vmove)(main)

MoveScorer(main, expected_qasm=expected_qasm).animate()
print(MoveScorer(main, expected_qasm=expected_qasm).score())

