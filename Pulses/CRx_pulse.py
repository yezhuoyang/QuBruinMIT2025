from bloqade import move
from Pulses import CNOT_pulse

def CRx_pulse(state: move.core.AtomState, gate_ind, theta):
    state = CNOT_pulse.cx_pulse(state, gate_ind)
    state = move.GlobalXY(atom_state=state, x_exponent=theta, axis_phase_exponent=0.0)
    state = CNOT_pulse.cx_pulse(state, gate_ind)
    return state

