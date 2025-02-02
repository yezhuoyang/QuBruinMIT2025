from bloqade import move

@move.vmove
def cx_pulse(state: move.core.AtomState, gate_ind):
    state = move.LocalXY(atom_state=state,x_exponent=-0.5,axis_phase_exponent=0.5,indicies=gate_ind)
    state = move.LocalRz(atom_state=state,phi=1,indices=gate_ind)
    state = move.GlobalCZ(atom_state=state)
    state = move.LocalXY(atom_state=state,x_exponent=-0.5,axis_phase_exponent=0.5,indicies=gate_ind)
    state = move.LocalRz(atom_state=state,phi=1,indices=gate_ind)
    return state