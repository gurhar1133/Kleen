# now a demonstration of why principle of non-contradiction has counter examples
# with trinary logic
from logicClass import LogicGate
from kleen_logic import *


def contra():
    print("Welcome to a demonstration of why the principle of non-contradiction has")
    print("counter exapmles under trinary logic\n")
    for i in range(3):

        nt = NotGate(" not gate")
        a = AndGate(" And")
        ntnt = NotGate(" final gate (not)")
    
        con = Connector(nt, a)
        con2 = Connector(a, ntnt)
        if i == 0:
            print("try entering -1\n")
        elif i == 1:
            print("cool, now enter 1\n")
        else:
            print("Ok, now enter the third value (0)\n")
        nt.getOutput()
        a.pinB = nt.pin
    

        print("final output " + str(ntnt.performGateLogic())+"\n")
        if i == 2:
            print("\nNotice how the output of the or gate was not 1")
            print("This represents how a counter example to the principle of")
            print("non-contradiction follows from trinary logic")
            print("ie. it is not-tautologically true that not(a and not a)")
            


contra()