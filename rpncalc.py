import math
class rpn:
    def __init__(self, inStr=''):
        """Create RPN Stack from string"""
        self.stack = []
        self.funs = {
            "+": self.add,
            "*": self.mul,
            "-": self.sub,
            "/": self.div,
            "d": self.dup,
            "sq": self.sq,
            "sqr": self.sqr,
            "^": self.power,
            "%": self.mod,
            "p": self.pick,
            "pi": self.pi,
            "1/": self.inv
        }
        self.update(inStr)
        
    def update(self, inStr):
        for n in inStr.split():
            if self.isnum(n):
                if '.' in n:
                    self.stack.append(float(n))
                    print("Push".ljust(15), n.ljust(15), self.stack)
                else:
                    self.stack.append(int(n))
                    print("Push".ljust(15), n.ljust(15), self.stack)
            else:
                if n in self.funs:
                    self.funs[n]()
        print()
    
    def getStack(self):
        return self.stack
    
    def isnum(self, n):
        return n.replace('.','',1).isdigit()
    
    def add(self):
        n2 = self.stack.pop()
        n1 = self.stack.pop()
        self.stack.append(n1 + n2)
        print("Add".ljust(15), (str(n1) + ' + ' + str(n2)).ljust(15), self.stack)

    def mul(self):
        n2 = self.stack.pop()
        n1 = self.stack.pop()
        self.stack.append(n1 * n2)
        print("Multiply".ljust(15), (str(n1) + ' * ' + str(n2)).ljust(15), self.stack)

    def sub(self):
        n2 = self.stack.pop()
        n1 = self.stack.pop()
        self.stack.append(n1 - n2)
        print("Subtract".ljust(15), (str(n1) + ' - ' + str(n2)).ljust(15), self.stack)

    def div(self):
        n2 = self.stack.pop()
        n1 = self.stack.pop()
        self.stack.append(n1 / n2)
        print("Divide".ljust(15), (str(n1) + ' / ' + str(n2)).ljust(15), self.stack)

    def dup(self):
        n1 = self.stack.pop()
        self.stack.append(n1)
        self.stack.append(n1)
        print("Duplicate".ljust(15), str(n1).ljust(15), self.stack)

    def sq(self):
        n1 = self.stack.pop()
        self.stack.append(n1 * n1)
        print("Square".ljust(15), str(n1).ljust(15), self.stack)

    def sqr(self):
        n1 = self.stack.pop()
        self.stack.append(math.sqrt(n1))
        print("Square Root".ljust(15), str(n1).ljust(15), self.stack)

    def power(self):
        n1 = self.stack.pop()
        n2 = self.stack.pop()
        self.stack.append(n2**n1)
        print("Power".ljust(15), (str(n1) + ' ^ ' + str(n2)).ljust(15), self.stack)

    def mod(self):
        n1 = self.stack.pop()
        n2 = self.stack.pop()
        self.stack.append(n2%n1)
        print("Modulo".ljust(15), (str(n2) + ' % ' + str(n1)).ljust(15), self.stack)
        
    def pick(self):
        n1 = self.stack.pop()
        n2 = self.stack[len(self.stack) - n1 + 1]
        self.stack.append(n2)
        print("Pick Level".ljust(15), str(n1).ljust(15), self.stack)
    
    def pi(self):
        n1 = math.pi
        self.stack.append(n1)
        print("Push Pi".ljust(15), str(n1)[:4]+"...".ljust(15), self.stack)

    def inv(self):
        n1 = self.stack.pop()
        self.stack.append(1 / n1)
        print("Invert".ljust(15), ("1/"+str(n1)).ljust(15), self.stack)
        
R = rpn(" 2 1 + 4.5 * 5 * 2 / 7 + 7 8 9 + 2 sq * * d d 169 sqr 6 p")
#P = rpn("3 sq 4 sq + sqr pi * 1/")

print(R.getStack())

