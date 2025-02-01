from bloqade import move

@move.vmove
def local_H_pulse(state: move.core.AtomState, gate_ind):
    state = move.LocalXY(atom_state=state,x_exponent=-0.5,axis_phase_exponent=0.5,indices=gate_ind)
    state = move.LocalRz(atom_state=state,phi=1,indices=gate_ind)
    return state


@move.vmove
def global_H_pulse(state: move.core.AtomState):
    state = move.GlobalXY(atom_state=state,x_exponent=-0.5,axis_phase_exponent=0.5)
    state = move.GlobalRz(atom_state=state,phi=1)
    return state