from bloqade import move

def transfer_gate_to_storage(gate_ind, storage_ind):
    @move.vmove()
    def kernel(state:move.core.AtomState):
        state.storage[storage_ind] = move.Move(state.gate[gate_ind])
        return state
    return kernel