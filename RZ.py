from bloqade import move

'''
Module implementing Rz rotations, both local and global rotation.

Implemented by: Lorenzo
'''

@move.vmove()
def local_z_rotation(state:move.core.AtomState, rotation_angle, target_indices:list):
    '''
    method implementing local z-rotations.

    Inputs:
        state: move.core.AtomState object
        rotation_angle: angle of the rotation KEEP IN MIND THAT THIS PARAMETER IS MULTIPLIED BY PI 
                        IN QUERA MODULE
        target_indices: list of position to perform such a rotations

    Outputs:
        state: modified move.core.AtomState object
    '''

    state = move.LocalRz(atom_state=state,axis_phase_exponent=rotation_angle,indices=target_indices)
    return state

@move.vmove()
def global_z_rotation(state:move.core.AtomState, rotation_angle):
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
    
    state = move.GlobalRz(atom_state=state,phi=rotation_angle)
    return state