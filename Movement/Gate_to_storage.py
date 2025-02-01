from bloqade import move

@move.vmove()
def transfer_gate_to_storage(state:move.core.AtomState, gate_ind, storage_ind):
    state.storage[storage_ind] = move.Move(state.gate[gate_ind])
    return state