from bloqade import move
from Pulses import Rz_Pulse

def CRz_pulse(state: move.core.AtomState, gate_ind, theta):
    state = move.GlobalCZ(state)
    state = Rz_Pulse.local_Rz_pulse(state, gate_ind, theta)
    state = move.GlobalCZ(state)
    state = Rz_Pulse.local_Rz_pulse(state, gate_ind, -1*theta)
    return state