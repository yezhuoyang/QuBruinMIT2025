from bloqade import move

@move.vmove
def local_Rz_pulse(state: move.core.AtomState, gate_ind, theta):
    state = move.LocalRz(atom_state=state,axis_phase_exponent=theta,indices=gate_ind)
    return state

@move.vmove
def global_Rz_pulse(state: move.core.AtomState, theta):
    state = move.GlobalRz(atom_state=state,phi=theta)
    return state