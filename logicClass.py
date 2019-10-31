# Some class definitions for some logic gates 
# performGateLogic() is based on traditional binary logic

class LogicGate:
    """ the parent-most class """
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        # this method when called on any logic gate will perform its gate logic
        # operations and report the output of those operations
        self.output = self.performGateLogic()
        # this conveniently prints the value of the logic operations on the gate
        print("output for " + str(self.label) + ": " + str(self.output)+"\n")
        return self.output


class BinaryGate(LogicGate):
    """ this class inherits from the LogicGate parent class, it is 
        the class of binary logic gates """

    def __init__(self, n):
        # when this class is initialized it initializes an instance of its 
        # parent class and two additional pin A and pin B attributes
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None
    
    def getPinA(self):
        if self.pinA == None:
            # see comments on getPinB
            vals = [1,0]
            p = int(input("Enter Pin for unary gate"+self.getLabel()+"-->"))
            if p not in vals:
                raise RuntimeError("must enter 0 or 1")
            else:
                return p 
        else: 
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            # if the pin is not already set 
            vals = [1,0]
            p = int(input("Enter Pin for unary gate"+self.getLabel()+"-->"))
            if p not in vals:
                raise RuntimeError("must enter 0 or 1")
            else:
                return p
        else:
            # if the pin is set then ther is a connection and we get it
            # by retrieving fromgate's output
            return self.pinB.getFrom().getOutput()
    
    def setNextPin(self, source):
        # starting at the first pin of the binary gate passed into 
        # the connector as input, if it is not set, then set it as
        # the value of the source, otherwise try with the second pin.
        # if both pins have been checked and are set already, then the 
        # gate has no empty pins and an exception will be raised
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: this gate has no empty pins")

        


class UnaryGate(LogicGate):
    """ this is the unary class that inherits from the Logic gate parent class"""

    def __init__(self, n):
        # as you can see, it is initialized as a LogicGate instantiation 
        # with only a single pin because it is a unary gate "Child class constructors
        # need to call parent class constructors and then move on to their own
        # distinguising data"
        LogicGate.__init__(self,n)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            vals = [1,0]
            p = int(input("Enter Pin for unary gate"+self.getLabel()+"-->"))
            if p not in vals:
                raise RuntimeError("must enter 0 or 1")
            else:
                return p
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: this gate has no empty pins")


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self, n):
        # when we initialize a class that inherits from its parent, and we
        # want it to get its parent's attributes, we have to initialize and instantiation
        # of the parent class when initializing the child class instantiation
        BinaryGate.__init__(self, n)
    
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        pin = self.getPin()

        if pin == 1:
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        # this calls a LogicGate method that connects the connector to the
        # next gate
        tgate.setNextPin(self)
    
    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

if __name__ == '__main__':
    print("Hello and welcome to logic class! You need it!\n\n")

    # A circut!

    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")

    # the mappings defined in the c1-c3 variable declarations specify a flow
    # of input from one logical gate to another. By mapping the first argument gate
    # to the second, output flows from the first to the second as the second gate's
    # input

    # maps g1, an and gate, to the or gate g3
    c1 = Connector(g1,g3)
    # then maps g2, another and gate, to g3
    c2 = Connector(g2,g3)
    # then maps the or gate to g4, the not gate
    c3 = Connector(g3,g4)
    print("final: " + str(g4.getOutput()))



    
    



    