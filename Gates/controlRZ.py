from qiskit import QuantumCircuit

@move.vmove()
def local_z_rotation(state:move.core.AtomState, phi, indices):
    state = move.LocalRz(state, phi, indices)

@move.vmove()
def CRZ(state: move.core.AtomState, storage_site: int, gate_index: int, theta: int):
    state.gate[[gate_index]] = move.Move(state.storage[[storage_site]])
    state = move.GlobalCZ(state)
    state = move.LocalRz(state, theta, indices)
    state = move.GlobalCZ(state)
    state = move.LocalRz(state, -theta, indices)



