from bloqade import move



@move.vmove()
def local_xy_rotation(state:move.core.AtomState):
    state = move.LocalXY(atom_state=state,x_exponent=1.0,axis_phase_exponent=1.0,indices=[3,4])
    return state


@move.vmove()
def local_z_rotation(state:move.core.AtomState):
    state = move.LocalRz(atom_state=state,phi=0.5,indices=[3])
    

@move.vmove()
def global_xy_rotation(state:move.core.AtomState):
    state = move.GlobalXY(atom_state=state,x_exponent=1.0,axis_phase_exponent=1.0)
    return state


@move.vmove()
def global_z_rotation(state:move.core.AtomState):
    state = move.GlobalRz(atom_state=state,phi=0.5)
    return state


@move.vmove()
def global_cz(state:move.core.AtomState):
    state = move.GlobalCZ(atom_state=state)
    return state

