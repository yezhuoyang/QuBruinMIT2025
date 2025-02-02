from bloqade import move
import math

pi=math.pi

@move.vmove()
def cx_pulse(state,t_ind):
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=t_ind)
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=t_ind)
    state = move.GlobalCZ(atom_state=state)
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=t_ind)
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=t_ind)
    return state