
class LogicGates():

    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGates(LogicGates):

    def __init__(self, n):
        LogicGates.__init__(self, n)
        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.get_label()+"-->")
        else:
            return self.pinA.get_from().get_output()

    def get_pinB(self):
        if self.pinB == None:
            return input("Enter Pin B input for gate " + self.get_label()+"-->")
        else:
            return self.pinA.get_from().get_output()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("No Empty pins")


class UnaryGates(LogicGates):

    def __init__(self, n):
        LogicGates.__init__(self, n)
        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return input("Enter Pin B input for gate " + self.get_label()+"-->")
        else:
            return self.pin.get_from().get_output()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("No Empty pins")


class AndGate(BinaryGates):

    def __init__(self, n):
        BinaryGates.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        return 1 if a == b == 1 else 0


class OrGate(BinaryGates):

    def __init__(self, n):
        BinaryGates.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        return 0 if a == b == 0 else 1


class NotGate(UnaryGates):

    def __init__(self, n):
        UnaryGates.__init__(self, n)

    def perform_gate_logic(self):
        return 0 if self.get_pin() == 1 else 1

g1 = AndGate("g1")
g2 = AndGate("g2")
g3 = OrGate("g3")
g4 = NotGate("g4")


class Connector():

    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.setNextPin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate

c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

class NandGate(BinaryGates):

	def __init__(self,n):
		BinaryGates.__init__(self,n)

	def perform_gate_logic(self):
		a = self.get_pinA()
		b = self.get_pinB()
		return 0 if a==b==1 else 1

class NorGate(BinaryGates):

	def __init__(self,n):
		BinaryGates.__init__(self,n)

	def perform_gate_logic(self):
		a = self.get_pinA()
		b = self.get_pinB()
		return 1 if a == b == 0 else 0

g5 = NandGate("g5")
g6 = NorGate("g6")

u2 = AndGate("u2")
u3 = AndGate("u3")
u11 = NorGate("u11")
c_2_11 = Connector(u2,u11)
c_3_11 = Connector(u3,u11)

u10 = NandGate("u10")
u12 = NandGate("u12")
u4 = AndGate("u4")
c_10_4 = Connector(u10,u4)
c_12_4 = Connector(u12,u4)

print "m1 -> ", u11.get_output()
print "m2 -> ",u4.get_output()

