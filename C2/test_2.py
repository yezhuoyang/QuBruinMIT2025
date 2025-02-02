import math
from bloqade import move
from kirin.passes import aggressive
from iquhack_scoring import MoveScorer
from bloqade.move.emit import MoveToQASM2

pi = math.pi

@move.vmove
def main():
    q = move.NewQubitRegister(3)

    test_state = move.Init(qubits=[q[0],q[1],q[2]], indices=[0,1,2])

    #---------------------------------------------------------------------

    test_state.gate[[3]] = move.Move(test_state.storage[[2]])

    test_state = move.LocalRz(test_state, -pi, indices=[3])
    test_state = move.LocalXY(test_state, -1.3421, 0.0, indices=[3])

    test_state.gate[[2]] = move.Move(test_state.storage[[1]])

    # global CZ gate
    test_state = move.GlobalCZ(test_state)    

    
    
    '''
    test_state = move.Init(qubits=[q[0],q[1],q[2]], indices=[0,1,2])

    #---------------------------------------------------------------------

    test_state.gate[[0,2,3]] = move.Move(test_state.storage[[0,1,2]])

    # Hadamard gate
    test_state = move.LocalRz(test_state, -pi, indices=[3])
    test_state = move.LocalXY(test_state, -1.3421, 0.0, indices=[3])

    # global CZ gate
    test_state = move.GlobalCZ(test_state)
    # Hadamard gate
    test_state = move.LocalRz(test_state, 0.5*pi, indices=[3])
    test_state = move.LocalXY(test_state, pi, 0.5*pi, indices=[2])
    test_state = move.LocalXY(test_state, 0.25*pi, 0.5*pi, indices=[3])

    # CZ gate
    test_state = move.GlobalCZ(test_state)

    test_state = move.LocalXY(test_state, -0.55667, 0.5*pi, indices=[3])
    test_state = move.LocalXY(test_state, pi, 0.5*pi, indices=[2])
    test_state = move.LocalRz(test_state, -0.5*pi, indices=[3])

    test_state.gate[[1]] = move.Move(test_state.gate[[3]])

    # CZ gate
    test_state = move.GlobalCZ(test_state)

    test_state = move.LocalXY(test_state, -pi/8, 0.0, indices=[1])

    # CZ gate
    test_state = move.GlobalCZ(test_state)

    test_state.gate[[3]] = move.Move(test_state.gate[[0]])

    # CZ gate
    test_state = move.GlobalCZ(test_state)

    test_state = move.LocalXY(test_state, -pi/4, 0.0, indices=[2])

    # CZ gate
    test_state = move.GlobalCZ(test_state)

    # Global XY gate
    test_state = move.GlobalXY(atom_state=test_state, x_exponent=-0.5*pi, axis_phase_exponent=0.5*pi)

    test_state = move.LocalXY(atom_state=test_state, x_exponent=pi, axis_phase_exponent=0.5*pi, indices=[3])


    test_state = move.LocalRz(test_state, -7/8*pi, indices=[1])

    test_state = move.LocalXY(atom_state=test_state, x_exponent=pi, axis_phase_exponent=0.0, indices=[3])

    test_state = move.LocalRz(test_state, -3/4*pi, indices=[2])

    move.Execute(test_state)
    '''

    '''
    #---------------------------------------------------------------------    


    #---------------------------------------------------------------------
    # Second CRX GATE

    test_state.gate[[1]] = move.Move(test_state.storage[[1]])

    # Hadamard gate
    test_state = move.LocalXY(test_state, -0.5*pi, 0.5*pi, indices=[2])
    test_state = move.LocalRz(test_state, 1.0*pi, indices=[2])
    # global CZ gate
    test_state = move.GlobalCZ(test_state)
    # Hadamard gate
    test_state = move.LocalXY(test_state, -0.5*pi, 0.5*pi, indices=[2])
    test_state = move.LocalRz(test_state, 1.0*pi, indices=[2])
    
    # Global XY gate
    test_state = move.GlobalXY(atom_state=test_state, x_exponent=0.25*pi, axis_phase_exponent=0.0*pi)

    test_state.storage[[3]] = move.Move(test_state.gate[[2]])
    #--------------------------------------------------------------------- 


    #---------------------------------------------------------------------
    # Third CRX GATE

    test_state.gate[[2]] = move.Move(test_state.storage[[2]])

    # Hadamard gate
    test_state = move.LocalXY(test_state, -0.5*pi, 0.5*pi, indices=[2])
    test_state = move.LocalRz(test_state, 1.0*pi, indices=[2])
    # global CZ gate
    test_state = move.GlobalCZ(test_state)
    # Hadamard gate
    test_state = move.LocalXY(test_state, -0.5*pi, 0.5*pi, indices=[2])
    test_state = move.LocalRz(test_state, 1.0*pi, indices=[2])
    
    # Global XY gate
    test_state = move.GlobalXY(atom_state=test_state, x_exponent=0.5*pi, axis_phase_exponent=0.0*pi)

    #---------------------------------------------------------------------

    test_state.gate[[3]] = move.Move(test_state.storage[[3]])

    # global Hadamard
    test_state = move.GlobalXY(test_state, 0.25*pi, 0.5*pi)
    test_state = move.GlobalRz(test_state, 1.0*pi)
    test_state = move.GlobalXY(test_state, -0.25*pi, 0.5*pi)

    test_state.storage[[1,2,3]] = move.Move(test_state.gate[[1,2,3]])
    '''



if __name__ == '__main__':

    # subroutines are not allowed by the scoring.
    # run this pass to inline the subroutines
    aggressive.Fold(move.vmove)(main)

    '''
    analysis = MoveScorer(main,expected_qasm = "")

    score:dict = analysis.score()
    for key,val in score.items():
        print(f"{key}: {val}")

    # Commented out due to bad rendering of qasm string
    #analysis.validate_output(analysis.run_move_analysis())
    '''

    '''
    qasm = MoveToQASM2().emit_str(main)

    print(qasm)
    
    '''
    expected_qasm = "./assets/qasm/2.qasm"

    with open(expected_qasm) as f:
            qasm_string = f.read()

    MoveScorer(main, expected_qasm=qasm_string).animate()
    print(MoveScorer(main, expected_qasm=qasm_string).score())