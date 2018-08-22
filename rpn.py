#!/bin/python3
# RPN Calculator by Darrell Harriman  harrimand@gmail.com

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
            "dup2": self.dup2,
            "sq": self.sq,
            "sqr": self.sqr,
            "^": self.power,
            "%": self.mod,
            "p": self.pick,
            "pi": self.pi,
            "1/": self.inv,
            "sh": self.show,
            "dr": self.drop,
            "sw": self.swap,
            "clr": self.clr
        }
        self.update(inStr)

    def update(self, inStr):
        """Parse input, push integers and floats or perfrom operation """    
        for n in inStr.split():
            if self.isnum(n):
                if '.' in n:
                    self.stack.append(float(n))
                    print("Push".ljust(15), n.ljust(30), self.stack)
                else:
                    self.stack.append(int(n))
                    print("Push".ljust(15), n.ljust(30), self.stack)
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
            dup2 duplicate Level 2 and Level 1\n\
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
            clr  clear stack\n\
            ")

    def getStack(self):
        """Return list of stack contents"""
        return self.stack

    def isnum(self, n):
        return n.replace('.','',1).isdigit()

    def add(self):
        """Add Level 2 to Level 1 and place result on stack"""
        if len(self.stack) > 1:
            n2 = self.stack.pop()
            n1 = self.stack.pop()
            self.stack.append(n1 + n2)
            print("Add".ljust(15), (str(n1) + ' + ' + str(n2)).ljust(30), self.stack)
        else:
            print("Add requires 2 items on Stack")

    def mul(self):
        """Multiply Level 2 by Level 1 and place result on stack"""
        if len(self.stack) > 1:
            n2 = self.stack.pop()
            n1 = self.stack.pop()
            self.stack.append(n1 * n2)
            print("Multiply".ljust(15), (str(n1) + ' * ' + str(n2)).ljust(30), self.stack)
        else:
            print("Multiply requires 2 items on Stack")

    def sub(self):
        """Subtract Level 1 from Level 2 and place result on stack"""
        if len(self.stack) > 1:
            n2 = self.stack.pop()
            n1 = self.stack.pop()
            self.stack.append(n1 - n2)
            print("Subtract".ljust(15), (str(n1) + ' - ' + str(n2)).ljust(30), self.stack)
        else:
            print("Subtract requires 2 items on Stack")

    def div(self):
        """Divide Level 2 by Level 1 and place result on stack"""
        if len(self.stack) > 1:
            n2 = self.stack.pop()
            n1 = self.stack.pop()
            self.stack.append(n1 / n2)
            print("Divide".ljust(15), (str(n1) + ' / ' + str(n2)).ljust(30), self.stack)
        else:
            print("Divide requires 2 items on Stack")

    def dup(self):
        """Duplicate Level 1 on the stack"""
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(n1)
            self.stack.append(n1)
            print("Duplicate".ljust(15), str(n1).ljust(30), self.stack)
        else:
            print("Stack Empty")

    def dup2(self):
        """Duplicate Level 2 and Level 1 on the stack"""
        if len(self.stack) > 1:
            self.stack = self.stack + self.stack[-2:]
            dupStr = " ".join([str(i) for i in self.stack[-2:]])
            print("Dup 2".ljust(15), dupStr.ljust(30), self.stack)
        else:
            print("dup2 requires 2 items on the stack")

    def sq(self):
        """Square Level 1 and place result on stack"""
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(n1 * n1)
            print("Square".ljust(15), str(n1).ljust(30), self.stack)
        else:
            print("Stack Empty")

    def sqr(self):
        """Square Root Level 1 and place result on stack"""
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(math.sqrt(n1))
            print("Square Root".ljust(15), str(n1).ljust(30), self.stack)
        else:
            print("Stack Empty")

    def power(self):
        """Raise Level 2 to power of Level 1 and place result on stack"""
        if len(self.stack) > 1:
            n1 = self.stack.pop()
            n2 = self.stack.pop()
            self.stack.append(n2**n1)
            print("Power".ljust(15), (str(n2) + ' ^ ' + str(n1)).ljust(30), self.stack)
        else:
            print("Power requires 2 items on Stack")

    def mod(self):
        """Level 2 modulo Level 1 and place result on stack"""
        if len(self.stack) > 1:
            n1 = self.stack.pop()
            n2 = self.stack.pop()
            self.stack.append(n2%n1)
            print("Modulo".ljust(15), (str(n2) + ' % ' + str(n1)).ljust(30), self.stack)
        else:
            print("Modulo requires 2 items on Stack")

    def pick(self):
        """Pick item from stack selected by Level 1 value + 1"""
        n1 = self.stack.pop()
        if len(self.stack) > (n1 - 2):
            n2 = self.stack[len(self.stack) - n1]
            self.stack.append(n2)
            print("Pick Level".ljust(15), str(n1).ljust(30), self.stack)
        else:
            self.stack.append(n1)
            print("Pick Level out of range")

    def pi(self):
        """Place Pi on stack """
        n1 = math.pi
        self.stack.append(n1)
        print("Push Pi".ljust(15), (str(n1)[:4]+"...").ljust(30), self.stack)

    def inv(self):
        """1 / Level 1 Place result on stack"""
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(1 / n1)
            print("Invert".ljust(15), ("1/"+str(n1)).ljust(30), self.stack)
        else:
            print("Stack Empty")

    def show(self):
        """Print columns with Level #s and Level Values"""
        l = len(self.stack)
        i = 0
        for L in range(l, 0, -1):
            print(str(L).rjust(8), "\t", self.stack[i])
            i += 1

    def drop(self):
        """Drop Level 1 from stack"""
        if len(self.stack) > 0:
            print("Drop".ljust(15), str(self.stack.pop()).ljust(30), self.stack)
#           self.stack.pop()
        else:
            print("Stack Empty")

    def swap(self):
        """Swap Level 1 with Level 2"""
        if len(self.stack) > 1:
            n1 = self.stack.pop()
            n2 = self.stack.pop()
            self.stack.append(n1)
            self.stack.append(n2)
            print("Swap".ljust(15), "L1 <-> L2".ljust(30), self.stack)
        else:
            print("Swap requires 2 items on Stack")

    def clr(self):
        """Clear (empty) stack"""
        self.stack = []
        print("Clear Stack".ljust(15), "clr".ljust(30), self.stack)
