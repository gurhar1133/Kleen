# this is a demonstration of what taut_circ does but this one implements the 
# connector class to model the law of excluded middle using a composite circutry

from logicClass import LogicGate
from kleen_logic import *

def circ():
    print("Welcome to a demonstration of why the law of excluded middle breaks down")
    print("under trinary logic\n")
    for i in range(3):

        nt = NotGate(" not gate")
        o = OrGate(" An or")
    
        con = Connector(nt, o)
        if i == 0:
            print("try entering -1\n")
        elif i == 1:
            print("cool, now enter 1\n")
        else:
            print("Ok, now enter the third value (0)\n")
        nt.getOutput()
        o.pinB = nt.pin
    

        print("orgate output " + str(o.performGateLogic())+"\n")
        if i == 2:
            print("\nNotice how the output of the or gate was not 1")
            print("This represents how the law of excluded middle is no longer")
            print("Tautological once we introduce 0 as a third valuation")


circ()

