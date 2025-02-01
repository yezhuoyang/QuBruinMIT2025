from bloqade import move

'''
Module implementing Rx rotations, both local and global rotation.

Implemented by: Lorenzo
'''


@move.vmove()
def local_x_rotation(state:move.core.AtomState, rotation_angle, target_indices:list, direction:str='plus') -> move.core.AtomState:
    '''
    method implementing local x-rotations.

    Inputs:
        state: move.core.AtomState object
        rotation_angle: angle of the rotation KEEP IN MIND THAT THIS PARAMETER IS MULTIPLIED BY PI 
                        IN QUERA MODULE
        target_indices: list of position to perform such a rotations
        directions: string encoding the direction of the rotation pulse, 'plus' for a rotation along the 
                    +X direction and 'minus' for a rotation along -X direction

    Outputs:
        state: modified move.core.AtomState object
    '''

    if direction == 'minus':
      dir_angle = 0
    else:
      dir_angle = 1.0 
    state = move.LocalXY(atom_state=state,x_exponent=dir_angle,axis_phase_exponent=rotation_angle,indices=target_indices)
    return state

@move.vmove()
def global_x_rotation(state:move.core.AtomState, rotation_angle, direction:str='plus') -> move.core.AtomState:
    '''
    method implementing global x-rotations.

    Inputs:
        state: move.core.AtomState object
        rotation_angle: angle of the rotation KEEP IN MIND THAT THIS PARAMETER IS MULTIPLIED BY PI 
                        IN QUERA MODULE
        directions: string encoding the direction of the rotation pulse, 'plus' for a rotation along the 
                    +X direction and 'minus' for a rotation along -X direction

    Outputs:
        state: modified move.core.AtomState object
    '''

    if direction == 'minus':
      dir_angle = 0
    else:
      dir_angle = 1.0 
    state = move.GlobalXY(atom_state=state,x_exponent=dir_angle, axis_phase_exponent=rotation_angle)
    return state