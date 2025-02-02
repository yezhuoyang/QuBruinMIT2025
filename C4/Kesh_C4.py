from bloqade import move
import math
from kirin.passes import aggressive

pi = math.pi

@move.vmove
def main():

    register = move.NewQubitRegister(9)
    state=move.Init(qubits=[register[0],register[1],register[2],register[3],register[4],register[5],register[6],register[7],register[8]], indices=[0,1,2,3,4,5,6,7,8])
    
    state.gate[[0,1]] = move.Move(state.storage[[0,3]])
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[1])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[1])
    state = move.GlobalCZ(atom_state=state)
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[1])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[1])
    state.storage[[3]] = move.Move(state.gate[[1]])
    
    state.gate[[0,1]] = move.Move(state.storage[[0,6]])
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[1])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[1])
    state = move.GlobalCZ(atom_state=state)
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[1])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[1])
    ## Here we have 0th qubit at 0 and 6th qubit at 1

    # Apply Hadamards
    state.gate[[2]] = move.Move(state.storage[[3]])
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[0]) # H on 0 = 0
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[0])

    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[1]) # H on 1 = 6
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[1])

    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[2]) # H on 2 = 3
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[2])
    ## Here we have 0th qubit at 0 and 6th qubit at 1 and 3rd qubit at 2

    # Move 6th qubit at G[4]
    state.storage[[6]] = move.Move(state.gate[[1]])
    state.gate[[4]] = move.Move(state.storage[[6]])

    # Move rest of qubits to corresponding pairs
    state.gate[[1]] = move.Move(state.storage[[1]]) # Engtangle S[0]=G[0] with S[1]=G[1]
    state.gate[[3]] = move.Move(state.storage[[4]]) # Engtangle S[3]=G[2] with S[4]=G[3]
    state.gate[[5]] = move.Move(state.storage[[7]]) # Engtangle S[6]=G[4] with S[7]=G[5]
    
    # Now apply rest of CX gates
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[1])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[1])

    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[3])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[3])

    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[5])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[5])

    state = move.GlobalCZ(atom_state=state)
    
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[1])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[1])

    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[3])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[3])

    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[5])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[5])
    # Here we have S[0]=G[0], S[1]=G[1], S[3]=G[2], S[4]=G[3], S[6]=G[4], S[7]=G[5]

    # Move back S[1]=G[1], S[4]=G[3], S[7]=G[5]
    state.storage[[1]] = move.Move(state.gate[[1]])
    state.storage[[4]] = move.Move(state.gate[[3]])
    state.storage[[7]] = move.Move(state.gate[[5]])

    # Move new entangling qubit's pair
    state.gate[[1]] = move.Move(state.storage[[2]])
    state.gate[[3]] = move.Move(state.storage[[5]])
    state.gate[[5]] = move.Move(state.storage[[8]])

    # Now apply rest of CX gates
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[1])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[1])

    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[3])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[3])

    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[5])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[5])

    state = move.GlobalCZ(atom_state=state)
    
    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[1])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[1])

    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[3])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[3])

    state = move.LocalXY(atom_state=state,x_exponent=-0.5*pi,axis_phase_exponent=0.5*pi,indices=[5])
    state = move.LocalXY(atom_state=state,x_exponent=-1.0*pi,axis_phase_exponent=0.0*pi,indices=[5])
    # Here we have S[0]=G[0], S[2]=G[1], S[3]=G[2], S[5]=G[3], S[6]=G[4], S[8]=G[5]
    
    move.Execute(state)

#aggressive.Fold(move.vmove)(main)

if __name__ == "__main__":

    with open("assets/qasm/4.qasm", "r", encoding="utf-8") as file:
        content = file.read()
    
    print(content)  # Prints the file contents as a string
    
    from iquhack_scoring import MoveScorer
    analysis = MoveScorer(main,expected_qasm = content)
    
    score:dict = analysis.score()
    for key,val in score.items():
        print(type(key))
        print(f"{key}: {val}")
    
    from bloqade.move.emit import MoveToQASM2
    # Commented out due to bad rendering of qasm string
    #analysis.validate_output(analysis.run_move_analysis())
    
    qasm = MoveToQASM2().emit_str(main)
    print(qasm)
