import ply.lex as lex
 
reserved = {
  
  
}

 # List of token names.   This is always required
tokens = (
 
) + tuple(reserved.values())
 
 # Regular expression rules for simple tokens



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
for (let i = 0; i < 9; i++){}
  if 4>5 && 5<4:
    return true
    4.5 +25'''
 
 # Give the lexer some input
lexer.input(data)
 
 # Tokenize
while True:
  tok = lexer.token()
  if not tok: 
    break      # No more input
  print(tok)