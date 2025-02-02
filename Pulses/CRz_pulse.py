from bloqade import move
import math

@move.vmove()
def CRz_pulse(state: move.core.AtomState, t_ind, theta):
    pi=math.pi
    beta=-1*pi+(theta/2)
    state = move.LocalRz(atom_state=state,phi=(beta),indices=t_ind)
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=t_ind)
    state = move.GlobalCZ(state)
    state = move.LocalXY(atom_state=state,x_exponent=-theta/2,axis_phase_exponent=0.0,indices=t_ind)
    state = move.GlobalCZ(state)
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=t_ind)
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0,indices=t_ind)
    return state