from bloqade import move
from Movement import Gate_to_storage,Storage_to_Gate
from Pulses import CNOT_pulse
from kirin.passes import aggressive
from iquhack_scoring import MoveScorer
import math

pi=math.pi

kernal1=Storage_to_Gate.transfer_storage_to_gate([0,1],[0,1])
kernal3=Gate_to_storage.transfer_gate_to_storage([0,1],[0,1])

@move.vmove
def main():
    q = move.NewQubitRegister(6)
    qubits = [q[0], q[1]]
    indices = [0, 1]
    state = move.Init(qubits=qubits, indices=indices)

    t_ind=[1]
    kernal1(state)
    state=CNOT_pulse.cx_pulse(state, t_ind)
    kernal3(state)
    
    move.Execute(state)

expected_qasm = """
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];

cx q[0],q[1];

"""

# subroutines are not allowed by the scoring.
# run this pass to inline the subroutines
aggressive.Fold(move.vmove)(main)

#MoveScorer(main, expected_qasm=expected_qasm).animate()
print(MoveScorer(main, expected_qasm=expected_qasm).score())