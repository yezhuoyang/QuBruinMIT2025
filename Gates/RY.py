from bloqade import move

'''
Module implementing Ry rotations, both local and global rotation.

Implemented by: Lorenzo
'''

@move.vmove()
def local_y_rotation(state:move.core.AtomState, rotation_angle, starting_indices, target_indices) -> move.core.AtomState:
    '''
    method implementing local y-rotations.

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
    state = move.LocalXY(atom_state=state,x_exponent=rotation_angle, axis_phase_exponent=0.5, 
                         indices=target_indices)
    state.storage[starting_indices] = move.Move(state.gate[target_indices])
    return state

def global_y_rotation(state:move.core.AtomState, rotation_angle, starting_indices, 
                      target_indices) -> move.core.AtomState:
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
    state = move.GlobalXY(atom_state=state,x_exponent=rotation_angle, axis_phase_exponent=0.5)
    state.storage[starting_indices] = move.Move(state.gate[target_indices])
    return state