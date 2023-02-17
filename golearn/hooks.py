'''
very hard example
validation hooks {[(<>)]}
'''

class Validation:
    def __init__(self):
        self.text = '(<([{}]())>)'
        self._opens = '({[<'
        self._closed = ')}]>'
        self._massage = ''
    def balanced(self):
        stack = []
        for symbol_position, symbol in enumerate(self.text):
            if symbol in self._opens:
                stack.append((symbol_position, symbol))
            elif symbol in self._closed:
                position = self._closed.index(symbol)
                if stack and (self._opens[position] == stack[-1][1]):
                    stack.pop()


q = Validation()
q.balanced()