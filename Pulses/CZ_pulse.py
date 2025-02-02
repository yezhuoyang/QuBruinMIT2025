from bloqade import move

@move.vmove
def cz_pulse(state: move.core.AtomState):
    state = move.GlobalCZ(state)
    return state