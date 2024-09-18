from ply.lex import lex
from enum import Enum

class Alfabeto(Enum):
    IDENTIFICADOR = 0
    ENTERO = 1
    REAL = 2
    CADENA = 3
    TIPO = 4 # int, float, void
    OPSUMA = 5 # +, -
    OPMUL = 6 # *, /
    OPRELAC = 7 # <, >, <=, >=, ==, !=
    OPOR = 8 # ||
    OPAND = 9 # &&
    OPNOT = 10 # !
    OPIGUALDAD = 11 # ==, !=
    PUNTOCOMA = 12 # ;
    COMA = 13 # ,
    PARENTESISIZQ = 14 # (
    PARENTESISDER = 15 # )
    LLAVEIZQ = 16 # {
    LLAVEDER = 17 # }
    ASIGNACION = 18 # =
    IF = 19
    WHILE = 20
    RETURN = 21
    ELSE = 22
    SIGNODINERO = 23 # $
    DESCONOCIDO = 24
    FIN = 25




# Reserved words
reserved = {
    'if': 'IF',
    'while': 'WHILE',
    'return': 'RETURN',
    'else': 'ELSE',
    'int': 'TIPO',
    'float': 'TIPO',
    'void': 'TIPO'
}

# Tokens
tokens = [name for name in Alfabeto.__members__]

# Regular expressions for the tokens
t_ENTERO = r'\d+'
t_REAL = r'\d+\.\d+'
t_CADENA = r'\".*\"'
t_OPSUMA = r'\+|-'
t_OPMUL = r'\*|/'
t_OPRELAC = r'<|>|<=|>=|==|!='
t_OPOR = r'\|\|'
t_OPAND = r'&&'
t_OPNOT = r'!'
t_OPIGUALDAD = r'==|!='
t_PUNTOCOMA = r';'
t_COMA = r','
t_PARENTESISIZQ = r'\('
t_PARENTESISDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_ASIGNACION = r'='
t_SIGNODINERO = r'\$'

# Ignore spaces and tabs
t_ignore = ' \t'

def t_TIPO(t):
    r'int|float|void'
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')
    return t

# Regular expression to handle errors
def t_error(t):
    print(f'Unrecognized character: {t.value[0]}')
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    # No return value. Token discarded

def t_comments_oneline(t):
    r'//.*\n'
    # No return value. Token discarded




# Build the lexer | This is the function that will be called from the main program
def analyze_lexical(text):
    lexer = lex()

    # Give the lexer some input
    lexer.input(text)

    # Tokenize
    result = []
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        result.append((tok.value, tok.type, Alfabeto[tok.type].value))

    return result