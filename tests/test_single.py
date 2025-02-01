from bloqade import move
from iquhack_scoring import MoveScorer





@move.vmove
def cx_gate(state: move.core.AtomState, store_ind: int, gate_ind: int):
    state.gate[[gate_ind]] = move.Move(state.storage[[store_ind]])
    state = move.LocalRz(atom_state=state,phi=1,indices=gate_ind)
    state = move.LocalXY(atom_state=state,x_exponent=-0.5,axis_phase_exponent=0.5,indicies=gate_ind)
    state = move.GlobalCZ(atom_state=state)
    state = move.LocalRz(atom_state=state,phi=1,indices=gate_ind)
    state = move.LocalXY(atom_state=state,x_exponent=-0.5,axis_phase_exponent=0.5,indicies=gate_ind)
    state.storage[[store_ind]] = move.Move(state.gate[[gate_ind]])
    return state




def test_cx():
    cx_gate(0,1)
    
    with open("cnot.qasm", "r", encoding="utf-8") as file:
        content = file.read()
    
    print(content)  # Prints the file contents as a string
    
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





if __name__ == "__main__":

    test_cx()