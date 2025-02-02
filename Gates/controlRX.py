#  shika - controlled Rotations
from qiskit import QuantumCircuit
import math

pi = math.pi

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
def local_z_rotation(state:move.core.AtomState, phi, indices):
    state = move.LocalRz(state, phi, indices)


# GLOBAL GATE SET ---     
@move.vmove()
def CX(state: move.core.AtomState, storage_site: int, gate_index: int):
    state.gate[[gate_index]] = move.Move(state.storage[[storage_site]])
    state = LocalH(state, [gate_index])
    state = move.GlobalCZ(state)
    state = LocalH(state, [gate_index])
    state.storage[[storage_site]] = move.Move(state.gate[[gate_index]])
    return state

@move.vmove()
def CRX(state: move.core.AtomState, storage_site: int, gate_index: int, theta: int):
    state.gate[[gate_index]] = move.Move(state.storage[[storage_site]])
    state = move.CX(state)
    state = move.GlobalXY(atom_state=state, x_exponent=theta, axis_phase_exponent=0.0)
    state = move.CX(state)
    state.storage[[storage_site]] = move.Move(state.gate[[gate_index]])
    return state
