from bloqade import move
import math
from kirin.passes import aggressive

pi = math.pi

@move.vmove
def main():

    register = move.NewQubitRegister(7)
    state=move.Init(qubits=[register[0],register[1],register[2],register[3],register[4],register[5],register[6]], indices=[0,1,2,3,4,5,6])

    state = move.GlobalXY(state, pi*0.5, -0.5*pi)
    state = move.GlobalXY(state, pi, 0.0)

    
    # Move S[0]=G[0], S[1]=G[1], S[2]=G[2], S[4]=G[3], S[5]=G[4], S[6]=G[5]
    state.gate[[0,1,2,3,4,5]] = move.Move(state.storage[[0,1,2,4,5,6]])

    # Local Gates
    state = move.LocalXY(state, -pi, 0.0, indices=[5])
    state = move.LocalXY(state, -0.5*pi, -0.5*pi, indices=[5])
    
    # Now apply rest of CZ gates
    state = move.GlobalCZ(atom_state=state)

    # Move back S[1]=G[1], S[4]=G[3], S[6]=G[5], S[2]=G[2], S[5]=G[4]
    state.storage[[1]] = move.Move(state.gate[[1]])
    state.storage[[4]] = move.Move(state.gate[[3]])
    state.storage[[6]] = move.Move(state.gate[[5]])
    state.storage[[2]] = move.Move(state.gate[[2]])
    state.storage[[5]] = move.Move(state.gate[[4]])

    # Move new entangling qubit's pair S[2]=G[1], S[5]=G[3], S[6]=G[5], 
    state.gate[[1]] = move.Move(state.storage[[2]])
    
    state.gate[[3]] = move.Move(state.storage[[5]])
    state.gate[[2]] = move.Move(state.storage[[3]]) #S[3]=G[2]
    
    state.gate[[5]] = move.Move(state.storage[[6]]) 
    state.gate[[4]] = move.Move(state.storage[[4]]) # S[4] = G[4]

    # Now apply rest of CZ gates
    state = move.GlobalCZ(atom_state=state)
    # Here teh assignement is: S[2]=G[1], S[5]=G[3], S[6]=G[5], S[4] = G[4], S[3]=G[2], S[0]=G[0]

    # Move back S[2]=G[1], S[5]=G[3], S[6]=G[5], S[3]=G[2], S[4]=G[4], S[0]=G[0]
    state.storage[[2]] = move.Move(state.gate[[1]])
    state.storage[[5]] = move.Move(state.gate[[3]])
    state.storage[[6]] = move.Move(state.gate[[5]])
    state.storage[[3]] = move.Move(state.gate[[2]])
    state.storage[[4]] = move.Move(state.gate[[4]])
    state.storage[[0]] = move.Move(state.gate[[0]])

    # Move entangling pairs S[3]=G[1], S[4]=G[0], S[1]=G[2], S[5]=G[3], S[2]=G[4], S[6]=G[5]
    state.gate[[1]] = move.Move(state.storage[[3]])
    state.gate[[0]] = move.Move(state.storage[[4]])
    state.gate[[2]] = move.Move(state.storage[[1]])
    state.gate[[3]] = move.Move(state.storage[[5]])
    state.gate[[4]] = move.Move(state.storage[[2]])
    state.gate[[5]] = move.Move(state.storage[[6]])

    # ROtation Gates on qubit 6
    state = move.LocalXY(state, pi*0.5, -0.5*pi, indices=[5]) # As S[6]=G[5]
    state = move.LocalXY(state, pi, 0.0*pi, indices=[5]) # As S[6]=G[5]
    
    # Now apply rest of CZ gates
    state = move.GlobalCZ(atom_state=state)
    # Here the assignement is: S[4]=G[0], S[3]=G[1], S[1]=G[2], S[5]=G[3], S[2]=G[4], S[6]=G[5]

    # Move back all qubits except S[6]=G[5], so, S[0]=G[0], S[3]=G[1], S[1]=G[2], S[5]=G[3], S[2]=G[4]
    state.storage[[4]] = move.Move(state.gate[[0]])
    state.storage[[1]] = move.Move(state.gate[[2]])
    state.storage[[5]] = move.Move(state.gate[[3]])
    state.storage[[2]] = move.Move(state.gate[[4]])

    # Move entangling pairs S[3]=G[0], S[4]=G[1] and second pair is S[1]=G[4], S[6]=G[5]
    state.gate[[0]] = move.Move(state.storage[[0]])
    state.gate[[4]] = move.Move(state.storage[[1]])

    # Now apply rest of CZ gates
    state = move.GlobalCZ(atom_state=state)
    # Here the assignement is: S[3]=G[1], S[0]=G[0], S[1]=G[4], S[6]=G[5]

    # Move for rotations S[2]=G[2]
    state.gate[[2]] = move.Move(state.storage[[2]])
    
    # Rotations
    state = move.GlobalXY(state, 0.5*pi, -0.5*pi)
    state = move.LocalXY(state, -0.5*pi, -0.5*pi, indices=[1,2,4]) #S[1]=G[4], S[2]=G[2], S[3]=G[1]
    state = move.GlobalXY(state, pi, 0.0)
    state = move.LocalXY(state, -pi, 0.0, indices=[1,2,4])
    
    move.Execute(state)

#aggressive.Fold(move.vmove)(main)

if __name__ == "__main__":

    with open("assets/qasm/5.qasm", "r", encoding="utf-8") as file:
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
