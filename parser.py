class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', None)

    def eat(self, token_type):
        if self.current_token()[0] == token_type:
            self.pos += 1
        else:
            raise SyntaxError(f"Expected {token_type}, found {self.current_token()}")

    def parse(self):
        return self.expr()

    def expr(self):
        node = self.term()
        while self.current_token()[0] in ('PLUS', 'MINUS'):
            token_type, token_value = self.current_token()
            self.eat(token_type)
            node = ('binary_op', token_type, node, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current_token()[0] in ('MUL', 'DIV'):
            token_type, token_value = self.current_token()
            self.eat(token_type)
            node = ('binary_op', token_type, node, self.factor())
        return node

    def factor(self):
        token_type, token_value = self.current_token()
        if token_type == 'NUMBER':
            self.eat('NUMBER')
            return ('num', int(token_value))
        elif token_type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node
        else:
            raise SyntaxError(f"Unexpected token: {token_value}")
