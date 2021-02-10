# REFERENCIAS:
    # https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/

class Evaluador:
    def __init__(self, expression):
        self.expression = expression
        self.precedence = {
            '+': 0, 
	        '-': 0, 
            '*': 1, 
            '/': 1
        }
        self.output = []
        self.operation = []
        # si hay datos vacios
        self.top =- 1
        self.number_account = ''

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    # verificación si numero 
    def isNumber(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    # verificacion de operaciones
    def possible_Operation(self, data):
        if (data == '+') or ( data == '-') or (data == '/') or (data == '^') or (data == '*'):
            return True
        else:
            return False
    
    def convertToNumber(self):
        if self.number_account !=  '':
            self.output.append(int(self.number_account))
            self.number_account = ''
            return self.number_account

    def evaluator(self, exp):
        for i in range(len(exp)):
            value = exp[i]
            #print(value)
            if self.isNumber(value):
                self.number_account = self.number_account + value
            elif self.possible_Operation(value):
                self.convertToNumber()
                while (len(self.operation) > 0) and (self.operation[-1] != '(') and (self.precedence[self.operation[-1]] >= self.precedence[value]):
                    data = self.operation.pop()
                    self.output.append(data)
                self.operation.append(value)
            elif value == '(':
                self.operation.append(value)
            elif value == ')':
                self.convertToNumber()
                while (len(self.operation)>0) and (self.operation[-1] != '('):
                    self.output.append(self.operation)
                    if (len(self.operation) == 0):
                        print('Imposible Parenthesization')
                        exit(-1)
                self.operation()

        if  self.number_account != '':
            self.output.append(int(self.number_account))
        
        while len(self.operation) > 0:
            value = self.operation.pop()
            if value == '(':
                print('Imposible Parenthesization')
                exit(-1)
            self.output.append(value)

        print(f'output: {self.output}')

        for value in self.output:
            if self.isNumber(value):
                self.operation.append(value)
            if self.possible_Operation(value):
                a, b = self.operation.pop(), self.operation.pop()
                if (value == '+'):
                    self.operation.append(a+b)
                if (value == '-'):
                    self.operation.append(a-b)
                if (value == '/'):
                    self.operation.append(a/b)
                if (value == '*'):
                    self.operation.append(a*b)
                if (value == '^'):
                    self.operation.append(a^b)
        
        print(f'result: {self.operation[0]}')

if __name__ == "__main__": 
    expression = input("Ingrese una expresion aritmetica: ")
    expression.replace(' ', '')
    #print(expression)
    obj = Evaluador(len(expression))
    obj.evaluator(expression)


