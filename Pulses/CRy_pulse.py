from bloqade import move
from Pulses import CNOT_pulse

def CRy_pulse(state: move.core.AtomState, gate_ind, theta):
    state = CNOT_pulse.cx_pulse(state, gate_ind)
    state = move.GlobalXY(atom_state=state, x_exponent=0.0, axis_phase_exponent=theta)
    state = CNOT_pulse.cx_pulse(state, gate_ind)
    return state