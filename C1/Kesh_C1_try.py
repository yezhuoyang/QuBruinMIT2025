from bloqade import move

@move.vmove
def main():
    register = move.NewQubitRegister(3)
    state = move.Init(qubits=[register[0],register[1],register[2]], indices=[0,1,2])
    state.gate[[0,1]] = move.Move(state.storage[[0,1]]) # Move for entangling gate
    state = move.GlobalCZ(atom_state=state) # CZ gate
    state.storage[[0,1]] = move.Move(state.gate[[0,1]]) # Move back from entangling gate
    
    state.gate[[1]] = move.Move(state.storage[[1]]) # Rz and Ry gates
    state = move.LocalXY(atom_state=state,x_exponent=0.25,axis_phase_exponent=0.5,indices=[1])
    state = move.LocalRz(atom_state=state,phi=1,indices=[1])   
    state = move.LocalXY(atom_state=state,x_exponent=-0.25,axis_phase_exponent=0.5,indices=[1])             
    state.storage[[1]] = move.Move(state.gate[[1]])

    state.gate[[0,1]] = move.Move(state.storage[[1,2]]) # Move for entangling gate
    state = move.GlobalCZ(atom_state=state) # CZ gate
    state.storage[[1,2]] = move.Move(state.gate[[0,1]]) # Move back from entangling gate

    state.gate[[1]] = move.Move(state.storage[[1]]) # Rz and Ry gates
    state = move.LocalXY(atom_state=state,x_exponent=0.25,axis_phase_exponent=0.5,indices=[1])
    state = move.LocalRz(atom_state=state,phi=1,indices=[1])   
    state = move.LocalXY(atom_state=state,x_exponent=-0.25,axis_phase_exponent=0.5,indices=[1])             
    state.storage[[1]] = move.Move(state.gate[[1]])
    
    move.Execute(state)


if __name__ == "__main__":


    with open("assets/qasm/1.1.qasm", "r", encoding="utf-8") as file:
        content = file.read()
    
    print(content)  # Prints the file contents as a string
    
    from iquhack_scoring import MoveScorer
    analysis = MoveScorer(main,expected_qasm = content)
    
    score:dict = analysis.score()
    for key,val in score.items():
        print(type(key))
        print(f"{key}: {val}")
    
    #from bloqade.move.emit import MoveToQASM2
    # Commented out due to bad rendering of qasm string
    #analysis.validate_output(analysis.run_move_analysis())
    
    #qasm = MoveToQASM2().emit_str(main)
    #print(qasm)
