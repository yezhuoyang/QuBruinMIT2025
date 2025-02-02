from bloqade import move

def transfer_storage_to_gate(storage_ind, gate_ind):
    @move.vmove()
    def kernel(state:move.core.AtomState):
        state.gate[gate_ind] = move.Move(state.storage[storage_ind])
        return state
    return kernel