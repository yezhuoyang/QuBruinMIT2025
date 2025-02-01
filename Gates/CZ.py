from bloqade import move

@move.vmove
def CZ_gate(state: move.core.AtomState, store_ind: int, gate_ind: int):
    state.gate[gate_ind] = move.Move(state.storage[store_ind])
    state=move.GlobalCZ(atom_state=state)
    state.storage[[store_ind]] = move.Move(state.gate[[gate_ind]])
    return state 

