from logicClass import LogicGate
# now lets model three valued logic with -1 as false, 0 as unknown and 1 as true


class BinaryGate(LogicGate):
    # this is the binary gate for three valued logic

    def __init__(self, n):
        # when this class is initialized it initializes an instance of its 
        # parent class and two additional pin A and pin B attributes
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None
        # when a binary gate is initialized it is not connected unless 
        # we connected after it is initialized
        self.connectedA = False
        self.connectedB = False
    
    def getPinA(self):
        if self.pinA == None:
            # see comments on getPinB
            vals = [-1,0,1]
            p = int(input("Enter Pin for binary gate "+self.getLabel()+"-->"))
            if p not in vals:
                raise RuntimeError("must enter -1, 0 or 1")
            else:
                return p 
        elif self.connectedA: 
            return self.pinA.getFrom().getOutput()
        else:
            return self.pinA

    def getPinB(self):
        if self.pinB == None:
            # if the pin is not already set. Vals is set to include three truth values
            vals = [-1,0,1]
            p = int(input("Enter Pin for binary gate "+self.getLabel()+"-->"))
            if p not in vals:
                raise RuntimeError("must enter -1, 0 or 1")
            else:
                return p
        elif self.connectedB:
            # if the pin is set then ther is a connection and we get it
            # by retrieving fromgate's output
            return self.pinB.getFrom().getOutput()
        else:
            return self.pinB
    
    def setNextPin(self, source):
        # starting at the first pin of the binary gate passed into 
        # the connector as input, if it is not set, then set it as
        # the value of the source, otherwise try with the second pin.
        # if both pins have been checked and are set already, then the 
        # gate has no empty pins and an exception will be raised
        if self.pinA == None:
            self.pinA = source
            self.connectedA = True
        else:
            if self.pinB == None:
                self.pinB = source
                self.connectedB = True
            else:
                raise RuntimeError("Error: this gate has no empty pins")



class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        
        # the following performs three value logic operations
        if a == 1 and b == 1:
            return 1
        elif a == -1 or b == -1:
            return -1
        elif a == 0 or b == 0:
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
        
        # this or gate performs three valued logic operations
        # if either a or b is true, then return true
        if a == 1 or b == 1:
            return 1
        # if a and b are both false, then return false
        elif a == -1 and b == -1:
            return -1
        # this covers all other cases which involve unknown logic values
        else:
            return 0

class UnaryGate(LogicGate):
    """ this is the unary class that inherits from the Logic gate parent class"""

    def __init__(self, n):
        # as you can see, it is initialized as a LogicGate instantiation 
        # with only a single pin because it is a unary gate "Child class constructors
        # need to call parent class constructors and then move on to their own
        # distinguising data"
        LogicGate.__init__(self,n)
        self.pin = None
        self.connected = False

    def getPin(self):
        if self.pin == None:
            # vals includes three truth values
            vals = [-1,0,1]
            p = int(input("Enter Pin for unary gate"+self.getLabel()+"-->\n"))
            if p not in vals:
                raise RuntimeError("must enter 0 or 1")
            else:
                return p
        elif self.connected:
            return self.pin.getFrom().getOutput()
        else:
            return self.pin

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
            self.connected = True
        else:
            raise RuntimeError("Error: this gate has no empty pins")


class NotGate(UnaryGate):
    
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        pin = self.getPin()
        self.pin = pin
        # now we have to model our not gate on three valued logic
        if pin == 1:
            return -1
        elif pin == -1:
            return 1
        elif pin == 0:
            return 0

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

# TODO: define more circuits which demonstrate implications of using three value
# logic
def main():
    for i in range(3):
        if i == 0:
            print("Welcome to Kleen logic\n")
            print("You'll be asked for some input")
            print("In this demonstration you'll be playing with a not gate")
            print("attached to another not gate")
            print("Try inputting 1, you'll notice that the input is negated twice")
            print("Basically two inverse processes are caried out")
            
        elif i == 1:
            print("Now try -1, you'll get the similar results")
        elif i == 2:
            print("now try 0")

        t1 = NotGate("First one")
        t2 = NotGate("Second one")

        c = Connector(t1, t2)

        print(t2.getOutput())

        if i == 0:
            print("notice how output of the first gate was the opposite")
            print("of its input, then that output serves as input")
            print("for the second gate's input and the output of the second gate")
            print("is equal to the original input. INVERSE OF INVERSE\n")
        
        elif i == 2:
            print("Notice how you just get a bunch of zeros? You've just")
            print("Violated the principle of non-contradiction! Congradulations")
            print("Aristotle would be sad.\n")
            print("Not really though, but negation doesnt work the same anymore")
            print("Normally not not is yeppy to the original input! But not not")
            print("to an unknown truth valuation is ummmm???? IDFK")
            print("Thanks for playing. Bye bye!")


if __name__ == "__main__":
    main()