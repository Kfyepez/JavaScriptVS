import ply.lex as lex
 
reserved = {
  #Santiago Tumbaco
    'if' : 'IF',
    'break':'BREAK', 
    'case': 'CASE', 
    'catch': 'CATCH', 
    'continue':'CONTINUE',
    'default':'DEFAULT',
    'delete': 'DELETE',
    'do':'DO', 
    'else':'ELSE', 
    'finally':'FINALLY',
    # Andrea Soriano
    'for': 'FOR',
    'function': 'FUNCTION',
    'in': 'IN',
    'instanceof': 'INSTANCEOF',
    'new': 'NEW',
    'return': 'RETURN',
    'switch': 'SWITCH',
    'this': 'THIS',
    #Kenny Yépez 
    'throw':'THROW', 
    'try':'TRY', 
    'typeof':'TYPEOF', 
    'var':'VAR', 
    'void':'VOID', 
    'while':'WHILE', 
    'with':'WITH',
    'let':'LET',
    'const':'CONST'
}

 # List of token names.   This is always required
tokens = (
 #Santiago Tumbaco
    "VARIABLE",#
    "ENTERO",#
    "DOUBLE",#
    "STRING",
    "BOOL",#
    "SUMA",#
    "RESTA",#
    "MULTI",#
    "DIV",#
    "MOD",#
    "IGUAL",#
    "DIGUAL",#
    "NOIGUAL",#
 # Andrea Soriano
    "MAYOR",  #
    "MENOR",  #
    "MAYIGUAL",  #
    "MENIGUAL",  #
    "ISNEGADO",
    "PUNTOYCOMA",  #
    "DSUMA",  #
    "DRESTA",  #
    "LIZQ",  #
    "LDER",  #
    #Kenny Yépez
    "CIZQ",#
    "CDER",#
    "PIZQ",#
    "PDER",#
    "COMILLAS",
    "DOSPUNTOS",#
    "COMA",#
    "DAMPERSAND",#
    "DTUBO"#

) + tuple(reserved.values())
 
 # Regular expression rules for simple tokens
#Santiago Tumbaco
t_STRING = r'("[^"]*"|\'[^\']*\')'
t_DOUBLE = r'\d+\.\d+'
t_ENTERO = r'\d'
t_SUMA = r"\+"
t_RESTA = r"-"
t_MULTI = r"\*"
t_DIV = r"/"
t_MOD = r"%"
t_IGUAL = r"="
#Andrea Soriano
t_DIGUAL = r"=="
t_NOIGUAL = "!="
t_MAYOR = r">"
t_MENOR = r"<"
t_MAYIGUAL = r">="
t_MENIGUAL = r"<="
t_PUNTOYCOMA = r";"
t_DSUMA= r"\+\+"
t_DRESTA= r"--"
t_CIZQ = r"\["
#Kenny Yépez
t_CDER = r"\]"
t_LIZQ = r"\{"
t_LDER = r"\}"
t_PIZQ = r"\("
t_PDER = r"\)"
t_DOSPUNTOS = r"\:"
t_COMA = r","
t_DAMPERSAND=r'&&'
t_DTUBO="\|\|"

#t_VARIABLE = r'[a-z]+'
 
 # Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)  
def t_BOOL(t):
  r"(true|false)"
  return t
def t_VARIABLE(t):
  r"[a-zA-Z][a-zA-Z0-9_]*"
  t.type = reserved.get(t.value,'VARIABLE')
  return t
 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
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
    break      # No more input
  print(tok)