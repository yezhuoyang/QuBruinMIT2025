from bloqade import move

@move.vmove()
def transfer_storage_to_gate(state:move.core.AtomState, storage_ind, gate_ind):
    state.gate[gate_ind] = move.Move(state.storage[storage_ind])
    return state