from bloqade import move
import math

pi = math.pi

@move.vmove
def cx_gate(state: move.core.AtomState, store_ind: int, gate_ind: int):
    state.gate[[gate_ind]] = move.Move(state.storage[[store_ind]])
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indicies=gate_ind)
    state = move.LocalRz(atom_state=state,phi=1*pi,indices=gate_ind)
    state = move.GlobalCZ(atom_state=state)
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indicies=gate_ind)
    state = move.LocalRz(atom_state=state,phi=1*pi,indices=gate_ind)
    state.storage[[store_ind]] = move.Move(state.gate[[gate_ind]])
    return state

