#  shika - controlled Rotations
from qiskit import QuantumCircuit

# qiskit implementation
# def controlled_rx(circuit, control, target, theta):
#     circuit.cx(control, target)  # cnot
#     circuit.rx(theta, target)    # rx(theta)
#     circuit.cx(control, target)  # cnot

# def controlled_ry(circuit, control, target, theta):
#     circuit.cx(control, target)
#     circuit.ry(theta, target)
#     circuit.cx(control, target)

@move.vmove()
def LocalH(state: move.core.AtomState, indices) -> move.core.AtomState:
    state = move.LocalXY(state, 0.25, 0.5, indices)
    state = move.LocalRz(state, pi, indices)
    state = move.LocalXY(state, -0.25, 0.5, indices)
    return state

@move.vmove()
def GlobalH(state: move.core.AtomState, indices) -> move.core.AtomState:
    state = move.GlobalXY(state, 0.25, 0.5, indices)
    state = move.GlobalRz(state, pi, indices)
    state = move.GlobalXY(state, -0.25, 0.5, indices)
    return state

@move.vmove()
def GlobalCX(state: move.core.AtomState, storage_site: int, gate_index: int):
    state.gate[[gate_index]] = move.Move(state.storage[[storage_site]])
    state = GlobalH(state, [gate_index])
    state = move.GlobalCZ(state)
    state = GlobalH(state, [gate_index])
    state.storage[[storage_site]] = move.Move(state.gate[[gate_index]])
    return state

@move.vmove()
def GlobalCRX(state: move.core.AtomState, storage_site: int, gate_index: int, theta: int):
    state.gate[[gate_index]] = move.Move(state.storage[[storage_site]])
    state = move.GlobalCX(state)
    state = move.GlobalXY(atom_state=state, x_exponent=theta, axis_phase_exponent=0.0)
    state = move.GlobalCX(state)
    state.storage[[storage_site]] = move.Move(state.gate[[gate_index]])
    return state


