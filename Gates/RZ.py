from bloqade import move
import math

pi = math.pi

'''
Module implementing Rz rotations, both local and global rotation.

Implemented by: Lorenzo
'''

@move.vmove()
def local_z_rotation(state:move.core.AtomState, rotation_angle, starting_indices:list, 
                     target_indices:list) -> move.core.AtomState:
    '''
    method implementing local z-rotations.

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
    state = move.LocalRz(atom_state=state,axis_phase_exponent=rotation_angle*pi,indices=target_indices)
    state.storage[starting_indices] = move.Move(state.gate[target_indices])
    return state

@move.vmove()
def global_z_rotation(state:move.core.AtomState, starting_indices:list, target_indices:list,
                      rotation_angle) -> move.core.AtomState:
    '''
    method implementing local x-rotations.

    Inputs:
        state: move.core.AtomState object
        rotation_angle: angle of the rotation KEEP IN MIND THAT THIS PARAMETER IS MULTIPLIED BY PI 
                        IN QUERA MODULE
        starting_indices: list of position in the storage section to move into the gate section
        target_indices: list of position to gate section perform such a rotations
        directions: string encoding the direction of the rotation pulse, 'plus' for a rotation along the 
                    +X direction and 'minus' for a rotation along -X direction

    Outputs:
        state: modified move.core.AtomState object
    '''
    
    state.gate[target_indices] = move.Move(state.storage[starting_indices])
    state = move.GlobalRz(atom_state=state,phi=rotation_angle*pi)
    state.storage[starting_indices] = move.Move(state.gate[target_indices])

    return state