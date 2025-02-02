from bloqade import move

@move.vmove
def local_Ry_pulse(state: move.core.AtomState, gate_ind, theta):
    state = move.LocalXY(atom_state=state,x_exponent=0.5,axis_phase_exponent=theta,indices=gate_ind)
    return state

@move.vmove
def global_Ry_pulse(state: move.core.AtomState, theta):
    state = move.GlobalXY(atom_state=state,x_exponent=0.5, axis_phase_exponent=theta)
    return state