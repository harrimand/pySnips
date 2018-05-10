import math
class rpn:
    def __init__(self, inStr=''):
        """Create RPN Stack from string"""
        self.stack = []
        self.funs = {
            "h": self.help,
            "+": self.add,
            "*": self.mul,
            "-": self.sub,
            "/": self.div,
            "du": self.dup,
            "sq": self.sq,
            "sqr": self.sqr,
            "^": self.power,
            "%": self.mod,
            "p": self.pick,
            "pi": self.pi,
            "1/": self.inv,
            "sh": self.show,
            "dr": self.drop,
            "sw": self.swap
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

    def help(self):
        print("\n\
            h    display this help\n\
            +    add Level 1 to Level 2\n\
            *    muliply Level 1 by Level 2\n\
            -    subract Level 1 from Level 2\n\
            /    divide Level 2 by Level 1\n\
            du   duplicate Level 1\n\
            sq   square of Level 1\n\
            sqr  square root of Level 1\n\
            ^    Level 2 raised to power of Level 1\n\
            %    Level 2 modulo Level 1\n\
            p    pick Level defined by Level 1 value\n\
            pi   push Pi to stack\n\
            1/   invert (1/x) Level 1\n\
            sh   Print stack with Level numbers\n\
            dr   drop Level 1 from stack\n\
            sw   swap Level 1 and Level 2\n\
            ")

    def getStack(self):
        return self.stack

    def isnum(self, n):
        return n.replace('.','',1).isdigit()

    def add(self):
        if len(self.stack) > 1:
            n2 = self.stack.pop()
            n1 = self.stack.pop()
            self.stack.append(n1 + n2)
            print("Add".ljust(15), (str(n1) + ' + ' + str(n2)).ljust(15), self.stack)
        else:
            print("Add requires 2 items on Stack")

    def mul(self):
        if len(self.stack) > 1:
            n2 = self.stack.pop()
            n1 = self.stack.pop()
            self.stack.append(n1 * n2)
            print("Multiply".ljust(15), (str(n1) + ' * ' + str(n2)).ljust(15), self.stack)
        else:
            print("Multiply requires 2 items on Stack")

    def sub(self):
        if len(self.stack) > 1:
            n2 = self.stack.pop()
            n1 = self.stack.pop()
            self.stack.append(n1 - n2)
            print("Subtract".ljust(15), (str(n1) + ' - ' + str(n2)).ljust(15), self.stack)
        else:
            print("Subtract requires 2 items on Stack")

    def div(self):
        if len(self.stack) > 1:
            n2 = self.stack.pop()
            n1 = self.stack.pop()
            self.stack.append(n1 / n2)
            print("Divide".ljust(15), (str(n1) + ' / ' + str(n2)).ljust(15), self.stack)
        else:
            print("Divide requires 2 items on Stack")

    def dup(self):
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(n1)
            self.stack.append(n1)
            print("Duplicate".ljust(15), str(n1).ljust(15), self.stack)
        else:
            print("Stack Empty")

    def sq(self):
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(n1 * n1)
            print("Square".ljust(15), str(n1).ljust(15), self.stack)
        else:
            print("Stack Empty")

    def sqr(self):
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(math.sqrt(n1))
            print("Square Root".ljust(15), str(n1).ljust(15), self.stack)
        else:
            print("Stack Empty")

    def power(self):
        if len(self.stack) > 1:
            n1 = self.stack.pop()
            n2 = self.stack.pop()
            self.stack.append(n2**n1)
            print("Power".ljust(15), (str(n1) + ' ^ ' + str(n2)).ljust(15), self.stack)
        else:
            print("Power requires 2 items on Stack")

    def mod(self):
        if len(self.stack) > 1:
            n1 = self.stack.pop()
            n2 = self.stack.pop()
            self.stack.append(n2%n1)
            print("Modulo".ljust(15), (str(n2) + ' % ' + str(n1)).ljust(15), self.stack)
        else:
            print("Modulo requires 2 items on Stack")

    def pick(self):
        n1 = self.stack.pop()
        if len(self.stack) > (n1 - 2):
            n2 = self.stack[len(self.stack) - n1 + 1]
            self.stack.append(n2)
            print("Pick Level".ljust(15), str(n1).ljust(15), self.stack)
        else:
            self.stack.append(n1)
            print("Pick Level out of range")

    def pi(self):
        n1 = math.pi
        self.stack.append(n1)
        print("Push Pi".ljust(15), (str(n1)[:4]+"...").ljust(15), self.stack)

    def inv(self):
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(1 / n1)
            print("Invert".ljust(15), ("1/"+str(n1)).ljust(15), self.stack)
        else:
            print("Stack Empty")

    def show(self):
        l = len(self.stack)
        i = 0
        for L in range(l, 0, -1):
            print(str(L).rjust(8), "\t", self.stack[i])
            i += 1

    def drop(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            print("Stack Empty")

    def swap(self):
        if len(self.stack) > 1:
            n1 = self.stack.pop()
            n2 = self.stack.pop()
            self.stack.append(n1)
            self.stack.append(n2)
            print("Swap".ljust(15), "L1 <-> L2".ljust(15), self.stack)
        else:
            print("Swap requires 2 items on Stack")



R = rpn("h 1 2 3 4 5")

R.update("sh 4 sh p sh 7 sh p sh sw sh")

"""
R.update("sh")
R.update("4")
R.update("sh")
R.update("p")
R.update("sh")
R.update("7")
R.update("sh")
R.update("p")
R.update("sh")
R.update("sw")
R.update("sh")
"""

#R = rpn(" 2 1 + 4.5 * 5 * 2 / 7 + 7 8 9 + 2 sq * * du du 169 sqr 6 p pi 27 du + 4 * 13 14 15 sh")
#P = rpn("3 sq 4 sq + sqr pi * 1/")

print(R.getStack())

