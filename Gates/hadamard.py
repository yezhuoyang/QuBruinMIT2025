# Hadamard Local
@move.vmove()
def Hadamard_local(state:move.core.AtomState, i, j):
    state.gate[[j]] = move.Move(state.storage[[i]]) # Rz and Ry gates
    state = move.LocalRz(atom_state=state,phi=1,indices=[j])
    state = move.LocalXY(atom_state=state,x_exponent=-0.5,axis_phase_exponent=0.5,indices=[j])
    state.storage[[i]] = move.Move(state.gate[[j]])
    return state

# Hadamard Global
@move.vmove()
def Hadamard_global(state:move.core.AtomState):
    state = move.GlobalRz(atom_state=state,phi=1)
    state = move.GlobalXY(atom_state=state,x_exponent=-0.5,axis_phase_exponent=0.5)
    return state