from bloqade import move
import math

pi = math.pi

'''
Module implementing Rx rotations, both local and global rotation.

Implemented by: Lorenzo
'''


@move.vmove()
def local_x_rotation(state:move.core.AtomState, rotation_angle, starting_indices:list,
                     target_indices:list) -> move.core.AtomState:
    '''
    method implementing local x-rotations.

    Inputs:
        state: move.core.AtomState object
        rotation_angle: angle of the rotation KEEP IN MIND THAT THIS PARAMETER IS MULTIPLIED BY PI 
                        IN QUERA MODULE
        starting_indices: list of position in the storage section to move into the gate section
        target_indices: list of position to gate section perform such a rotations

    Outputs:
        state: modified move.core.AtomState object
    '''

    state.gate[target_indices] = move.Move(state.storage[starting_indices])
    state = move.LocalXY(atom_state=state, x_exponent=rotation_angle*pi,indices=target_indices, 
                         axis_phase_exponent=0.0*pi)
    state.storage[starting_indices] = move.Move(state.gate[target_indices])
    return state

@move.vmove()
def global_x_rotation(state:move.core.AtomState, rotation_angle, starting_indices:list,
                      target_indices:list) -> move.core.AtomState:
    '''
    method implementing global x-rotations.

    Inputs:
        state: move.core.AtomState object
        rotation_angle: angle of the rotation KEEP IN MIND THAT THIS PARAMETER IS MULTIPLIED BY PI 
                        IN QUERA MODULE
        starting_indices: list of position in the storage section to move into the gate section
        target_indices: list of position to gate section perform such a rotations
  
    Outputs:
        state: modified move.core.AtomState object
    '''

    state.gate[target_indices] = move.Move(state.storage[starting_indices])
    state = move.GlobalXY(atom_state=state, x_exponent=rotation_angle*pi, axis_phase_exponent=0.0*pi)
    state.storage[starting_indices] = move.Move(state.gate[target_indices])
    return state