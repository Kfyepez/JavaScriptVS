import ply.lex as lex
import ply.yacc as yacc

reserved = {
    # Santiago Tumbaco
    'if': 'IF',  #
    'break': 'BREAK',  #
    'case': 'CASE',  #
    'catch': 'CATCH',  #
    'continue': 'CONTINUE',  #
    'default': 'DEFAULT',  #
    'delete': 'DELETE',
    'do': 'DO',  #
    'else': 'ELSE',  #
    'finally': 'FINALLY',  #
    'class': 'CLASS',
    'constructor': 'CONSTRUCTOR',
    # Andrea Soriano
    'for': 'FOR',  #
    'function': 'FUNCTION',  #
    'in': 'IN',  #
    'instanceof': 'INSTANCEOF',  #
    'new': 'NEW',
    'return': 'RETURN',  #
    'switch': 'SWITCH',  #
    'this': 'THIS',
    # Kenny Yépez
    'throw': 'THROW',  #
    'try': 'TRY',  #
    'typeof': 'TYPEOF',  #
    'var': 'VAR',  #
    'while': 'WHILE',  #
    'let': 'LET',  #
    'const': 'CONST'  #
}

# List of token names.   This is always required
tokens = (
             # Santiago Tumbaco
             "VARIABLE",  #
             "ENTERO",  ##
             "FLOAT",  ##
             "STRING",  #
             "BOOL",  #
             "SUMA",  ##
             "RESTA",  ##
             "MULTI",  ##
             "DIV",  ##
             "MOD",  #
             "IGUAL",  ##
             "DIGUAL",  ##
             "NOIGUAL",  ##
             # Andrea Soriano
             "MAYOR",  ##
             "MENOR",  ##
             "MAYIGUAL",  ##
             "MENIGUAL",  ##
             "ISNEGADO",
             "PUNTOYCOMA",  ##
             "DSUMA",  #
             "DRESTA",  #
             "LIZQ",  ##
             "LDER",  ##
             # Kenny Yépez
             "CIZQ",  #
             "CDER",  #
             "PIZQ",  ##
             "PDER",  ##
             "DOSPUNTOS",  #
             "COMA",  ##
             "DAMPERSAND",  ##
             "DTUBO",  ##
             "PUNTO"  ##
         ) + tuple(reserved.values())

# Regular expression rules for simple tokens
# Santiago Tumbaco
t_STRING = r'("[^"]*"|\'[^\']*\')'
t_FLOAT = r'\d+\.\d+'
t_ENTERO = r'\d+'
t_SUMA = r"\+"
t_RESTA = r"-"
t_MULTI = r"\*"
t_DIV = r"/"
t_MOD = r"%"
t_IGUAL = r"="
# Andrea Soriano
t_DIGUAL = r"=="
t_NOIGUAL = "!="
t_MAYOR = r">"
t_MENOR = r"<"
t_MAYIGUAL = r">="
t_MENIGUAL = r"<="
t_PUNTOYCOMA = r";"
t_DSUMA = r"\+\+"
t_DRESTA = r"\-\-"
t_CIZQ = r"\["
# Kenny Yépez
t_CDER = r"\]"
t_LIZQ = r"\{"
t_LDER = r"\}"
t_PIZQ = r"\("
t_PDER = r"\)"
t_DOSPUNTOS = r"\:"
t_COMA = r","
t_DAMPERSAND = r'&&'
t_DTUBO = r"\|\|"
t_PUNTO = r"\."


# t_VARIABLE = r'[a-z]+'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_BOOL(t):
    r"(true|false)"
    return t


def t_VARIABLE(t):
    r"[a-zA-Z][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = ''' 
  var prueba="hola"
for (let i = 0; i < 9; i++){}
  if 4>5 && 5<4:
    return true || function(hola,adios)
    4.5 +25'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)


# analizador sintactico
# Andrea Soriano
def p_cuerpo(p):
    ''' cuerpo : instrucciones
               | funcion
               | estrcontrol
               | def_clase
               | constructor
               |  '''


def p_instrucciones(p):
    '''instrucciones : instruccion PUNTOYCOMA
                      | instruccion PUNTOYCOMA instrucciones
                      | BREAK PUNTOYCOMA
                      | CONTINUE PUNTOYCOMA
                      | RETURN VARIABLE PUNTOYCOMA
                      | TYPEOF VARIABLE
                      | VARIABLE INSTANCEOF VARIABLE
                      | estrcontrol
                      | estrcontrol instrucciones
                      | llamarfuncion
                      | llamarfuncion instrucciones
                      | trycatch
                      | trycatch instrucciones'''


def p_instruccion(p):
    '''instruccion : asignacion
                     | expression
                     | comparacion
                     | declaracion
                     | declaasig
                     | operadores '''


def p_declaracion(p):
    '''declaracion : VAR VARIABLE
                   | LET VARIABLE'''


def p_declaasig(p):
    ''' declaasig : VAR asignacion
                  | LET asignacion
                  | CONST asignacion '''


def p_estr_control(p):
    '''estrcontrol : if
                   | for
                   | while
                   | dowhile
                   | switch '''


def p_valor(p):
    ''' valor : ENTERO
              | FLOAT
              | STRING
              | BOOL '''


def p_if(p):
    ''' if : IF PIZQ comparacion PDER LIZQ instrucciones LDER
           | IF PIZQ comparacion PDER LIZQ instrucciones LDER elseif
           | IF PIZQ comparacion PDER LIZQ instrucciones LDER else
           '''


def p_elseif(p):
    ''' elseif : ELSE IF PIZQ comparacion PDER LIZQ instrucciones LDER
           | ELSE IF PIZQ comparacion PDER LIZQ instrucciones LDER elseif
           | ELSE IF PIZQ comparacion PDER LIZQ instrucciones LDER else
           '''


def p_else(p):
    '''else : ELSE LIZQ instrucciones LDER
            | ELSE LIZQ LDER'''


def p_for(p):
    ''' for : FOR PIZQ declaasig PUNTOYCOMA comparacion PUNTOYCOMA operadores PDER LIZQ instrucciones LDER
            | FOR PIZQ declaasig PUNTOYCOMA comparacion PUNTOYCOMA asignacion PDER LIZQ instrucciones LDER
            | FOR PIZQ declaracion IN VARIABLE PDER LIZQ instrucciones LDER'''


def p_while(p):
    'while : WHILE PIZQ comparacion PDER LIZQ instrucciones LDER'


def p_dowhile(p):
    'dowhile : DO LIZQ instrucciones LDER WHILE PIZQ comparacion PDER PUNTOYCOMA'


def p_switch(p):
    'switch : SWITCH PIZQ VARIABLE PDER LIZQ cases LDER'


def p_cases(p):
    ''' cases : CASE VARIABLE DOSPUNTOS instrucciones
              | CASE VARIABLE DOSPUNTOS instrucciones cases
              | DEFAULT DOSPUNTOS instrucciones'''