import re

class Scanner:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.current_char = self.text[self.position] if self.text else None

    def advance(self):
        self.position += 1
        if self.position > len(self.text) - 1:
            self.current_char = None  # End of input
        else:
            self.current_char = self.text[self.position]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return result

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return ('NUMBER', self.get_number())

            if self.current_char == '+':
                self.advance()
                return ('PLUS', '+')

            if self.current_char == '-':
                self.advance()
                return ('MINUS', '-')

            if self.current_char == '*':
                self.advance()
                return ('MUL', '*')

            if self.current_char == '/':
                self.advance()
                return ('DIV', '/')

            if self.current_char == '(':
                self.advance()
                return ('LPAREN', '(')

            if self.current_char == ')':
                self.advance()
                return ('RPAREN', ')')

            raise Exception(f'Invalid character: {self.current_char}')

        return ('EOF', None)  # End of file/input

    def tokenize(self):
        tokens = []
        token = self.get_next_token()
        while token[0] != 'EOF':
            tokens.append(token)
            token = self.get_next_token()
        tokens.append(token)  # Add EOF token
        return tokens
