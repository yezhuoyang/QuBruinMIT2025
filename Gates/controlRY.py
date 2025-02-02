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
def CRY(state: move.core.AtomState, storage_site: int, gate_index: int, theta: int):
    state.gate[[gate_index]] = move.Move(state.storage[[storage_site]])
    state = move.CX(state)
    state = move.GlobalXY(atom_state=state, x_exponent=0.0*pi, axis_phase_exponent=theta)
    state = move.CX(state)
    state.storage[[storage_site]] = move.Move(state.gate[[gate_index]])
    return state

