from scanner import Scanner
from parser import Parser

def main(expression):
    scanner = Scanner(expression)
    tokens = scanner.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)

if __name__ == "__main__":
    expression = "3 + 5 * (2 - 8)"
    main(expression)
