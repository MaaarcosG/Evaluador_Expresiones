class Evaluador:
    def __init__(self, expression):
        self.expression = expression
        self.precedence = {
            '+': 1, 
	        '-': 1, 
            '*': 2, 
            '/': 2,
            '^': 3
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

    # verificación si numero, aceptamos doubles 
    def isNumber(self, value):
        try:
            float(value)
            return True
        except ValueError:
            #print('THE CHARACTER IS INCORRECT')
            return False

    # verificacion de operaciones
    def possible_Operation(self, data):
        return True if (data == '+') or ( data == '-') or (data == '/') or (data == '^') or (data == '*') else False
           
    def convertToNumber(self):
        if self.number_account !=  '':
            self.output.append(float(self.number_account))
            self.number_account = ''
            return self.number_account

    def deletePoint(self, point):
    	return point.lstrip('.')

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
                    self.output.append(self.operation.pop())
                    if (len(self.operation) == 0):
                        print('Imposible Parenthesization')
                        exit(-1)
                self.operation.pop()

        if  self.number_account != '':
            self.output.append(float(self.number_account))
        
        while len(self.operation) > 0:
            value = self.operation.pop()
            if value == '(':
                print('Imposible Parenthesization')
                exit(-1)
            self.output.append(value)

        for value in self.output:
            if self.isNumber(value):
                self.operation.append(value)
            if self.possible_Operation(value):
                a, b = self.operation.pop(), self.operation.pop()
                #print(a, b)
                if (value == '+'):
                    self.operation.append(a+b)
                if (value == '-'):
                    self.operation.append(a-b)
                if (value == '/'):
                    self.operation.append(b/a)
                if (value == '*'):
                    self.operation.append(a*b)
                if (value == '^'):
                	self.operation.append(pow(b,a))
            '''
            elif self.possible_Operation(value) == '**':
                a = self.operation.pop()
                self.operation.append(pow(a,a))
            '''
        print('Resultado de la Expresion: ', self.operation[0])

if __name__ == "__main__": 
    expression = input("Ingrese una expresion aritmetica: ")
    #print(expression)
    obj = Evaluador(len(expression))
    obj.evaluator(expression)


