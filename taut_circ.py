# now lets build a circuit that under normal conditions would always return 1
# this circut resembles the logical principle the law of excluded middle
# which states that given a proposion it is always true that the proposition
# is either true or false.

from logicClass import LogicGate
from kleen_logic import *

def run_taut_circ():

    # this initializes a not gate
    nt = NotGate("not gate")
    # this initializes an or gate
    o = OrGate("or gate")

    # now we need them to both recieve the same input
    # and the second input of the or gate should be the not gates output
    
    # this collects input for the not gate and returns its output
    nt.getOutput()

    # now we set the input for the or gate to be the not gate's output
    # as well as the same input that the not gate recieved

    # I did'nt use connectors to make this circut, just used assignment of 
    # the not gate's attributes to the or gate's inputs
    o.pinA = nt.pin
    o.pinB = nt.output

    print("orgate output " + str(o.performGateLogic()))





run_taut_circ()