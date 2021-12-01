import ply.lex as lex
import ply.yacc as yacc
import tkinter
from tkinter import Tk

reserved = {
  #Santiago Tumbaco
    'if' : 'IF', #
    'break':'BREAK', #
    'case': 'CASE', #
    'catch': 'CATCH', #
    'continue':'CONTINUE', #
    'default':'DEFAULT', #
    'delete': 'DELETE',
    'do':'DO', #
    'else':'ELSE', #
    'finally':'FINALLY', #
    'class': 'CLASS',
    'constructor': 'CONSTRUCTOR',
  #Andrea Soriano 
    'for':'FOR', #
    'function':'FUNCTION', #
    'in':'IN', #
    'instanceof':'INSTANCEOF', #
    'new':'NEW', 
    'return':'RETURN', #
    'switch':'SWITCH', #
    'this':'THIS',
  #Kenny Yépez 
    'throw':'THROW', #
    'try':'TRY', #
    'typeof':'TYPEOF', #
    'var':'VAR', #
    'while':'WHILE', #
    'let':'LET', #
    'const':'CONST'#
}

 # List of token names.   This is always required
tokens = (
  #Santiago Tumbaco
    "VARIABLE",#
    "ENTERO",##
    "FLOAT",##
    "STRING",#
    "BOOL",#
    "SUMA",##
    "RESTA",##
    "MULTI",##
    "DIV",##
    "MOD",#
    "IGUAL",##
    "DIGUAL",##
    "NOIGUAL",##
  #Andrea Soriano
    "MAYOR",##
    "MENOR",##
    "MAYIGUAL",##
    "MENIGUAL",##
    "ISNEGADO",
    "PUNTOYCOMA",##
    "DSUMA",#
    "DRESTA",#
    "LIZQ",##
    "LDER",##
  #Kenny Yépez
    "CIZQ",#
    "CDER",#
    "PIZQ",##
    "PDER",##
    "DOSPUNTOS",#
    "COMA",##
    "DAMPERSAND",##
    "DTUBO",##
    "PUNTO"##
) + tuple(reserved.values())
 
 # Regular expression rules for simple tokens
#Santiago Tumbaco
t_STRING = r'("[^"]*"|\'[^\']*\')'
t_FLOAT = r'\d+\.\d+'
t_ENTERO = r'\d+'
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
t_DRESTA= r"\-\-"
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
t_DTUBO = r"\|\|"
t_PUNTO=r"\."


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
#data = ''' 
#  var prueba="hola"
#for (let i = 0; i < 9; i++){}
#  if 4>5 && 5<4:
#    return true || function(hola,adios)
#    4.5 +25'''
 
 # Give the lexer some input
#lexer.input(data)
 
 # Tokenize
#while True:
#  tok = lexer.token()
#  if not tok: 
#    break      # No more input
#  print(tok)

#analizador sintactico
#Andrea Soriano
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


#Kenny Yepez

def p_throw(p):
  ''' throw : THROW VARIABLE PUNTOYCOMA
  '''
  
def p_trycatch(p):
  '''trycatch : TRY LIZQ instrucciones LDER CATCH PIZQ VARIABLE PDER LIZQ instrucciones LDER
              | TRY LIZQ instrucciones LDER FINALLY LIZQ instrucciones LDER
              | TRY LIZQ instrucciones LDER CATCH PIZQ VARIABLE PDER LIZQ instrucciones LDER FINALLY LIZQ instrucciones LDER'''

def p_asignacion(p):
  '''asignacion : VARIABLE IGUAL expression
                | VARIABLE IGUAL comparacion
                | VARIABLE IGUAL valor 
                | VARIABLE IGUAL llamarfuncion
                | VARIABLE IGUAL dec_array'''


# Semántico Kenny Yépez (Creación de arrays de un mismo tipo)
def p_dec_array(p):
  '''dec_array : CIZQ array_enteros CDER
               | CIZQ array_flotante CDER
               | CIZQ array_string CDER
               | CIZQ array_boolean CDER'''

def p_array_enteros(p):
  ''' array_enteros : ENTERO
                    | ENTERO COMA array_enteros'''

def p_array_flotante(p):
  ''' array_flotante : FLOAT
                    | FLOAT COMA array_flotante'''

def p_array_string(p):
  ''' array_string : STRING
                    | STRING COMA array_string'''

def p_array_boolean(p):
  ''' array_boolean : BOOL
                    | BOOL COMA array_boolean'''

#fin de semantico Kenny Yépez

def p_comparacion(p):
  '''comparacion : expression comparador expression
                 | expression comparador expression DAMPERSAND comparacion
                 | expression comparador expression DTUBO comparacion
                 | STRING DIGUAL STRING
                 | VARIABLE comparador ENTERO
                 '''

def p_comparador(p):
  '''comparador : MAYOR
                | MENOR
                | MAYIGUAL
                | MENIGUAL
                | DIGUAL
                | NOIGUAL'''

def p_operadores(p):
  '''operadores : VARIABLE DSUMA
                | VARIABLE DRESTA '''

def p_expression_suma(p):
  '''expression : expression SUMA term
                | VARIABLE SUMA VARIABLE'''
  p[0] = p[1] + p[3]
 
def p_expression_resta(p):
  '''expression : expression RESTA term
                | VARIABLE RESTA VARIABLE'''
  p[0] = p[1] - p[3]
 
def p_expression_term(p):
  '''expression : term
                | VARIABLE'''
  p[0] = p[1]
 
def p_term_multi(p):
  '''term : term MULTI factor
          | VARIABLE MULTI VARIABLE'''
  p[0] = p[1] * p[3]
 
def p_term_div(p):
  '''term : term DIV factor
          | VARIABLE RESTA VARIABLE'''
  p[0] = p[1] / p[3]
 
def p_term_factor(p):
  'term : factor'
  p[0] = p[1]

def p_factor_num(p):
  ''' factor : ENTERO
             | FLOAT '''
  p[0] = p[1]
 
def p_expression_parentesis(p):
  'expression : PIZQ expression PDER '
  p[0] = p[2]

def p_expression_llaves(p):
  'expression : LIZQ expression LDER '

#Santiago Tumbaco

def p_funcion_conarg(p):
  '''funcion : FUNCTION VARIABLE PIZQ argumentos PDER LIZQ instrucciones LDER
             | FUNCTION VARIABLE PIZQ argumentos PDER LIZQ LDER '''

def p_funcion_sinarg(p):
  '''funcion : FUNCTION VARIABLE PIZQ PDER LIZQ instrucciones LDER
             | FUNCTION VARIABLE PIZQ PDER LIZQ LDER '''

def p_llamar_funcion(p):
  ''' llamarfuncion : VARIABLE PIZQ argumentos PDER PUNTOYCOMA
                    | VARIABLE PIZQ PDER PUNTOYCOMA '''

def p_argumentos(p):
  '''argumentos : VARIABLE
                | VARIABLE COMA argumentos '''

def p_constructor_conarg(p):
  '''constructor : CONSTRUCTOR PIZQ argumentos PDER LIZQ metodo_cuerpo_class LDER'''
  
def p_constructor_sinarg(p):
  '''constructor : CONSTRUCTOR PIZQ PDER LIZQ metodo_cuerpo_class LDER 
  | CONSTRUCTOR PIZQ PDER LIZQ LDER '''


def p_var_class(p):
  '''var_class : THIS PUNTO VARIABLE
               | THIS PUNTO VARIABLE IGUAL valor
               | THIS PUNTO VARIABLE IGUAL VARIABLE '''

def p_metodo_cuerpo_class(p):
  '''metodo_cuerpo_class : cuerpo 
                            | var_class 
                            | metodo_cuerpo_class '''

def p_metodos_class(p):
  ''' metodos_class : funcion 
                    | funcion metodos_class'''

def p_cuerpo_class(p):
  ''' cuerpo_class : metodos_class 
                   | constructor 
                   | constructor metodos_class '''

def p_def_clase(p):
  ''' def_clase : CLASS VARIABLE LIZQ cuerpo_class LDER
                |  CLASS VARIABLE LIZQ LDER'''

# Error rule for syntax errors
def p_error(p):
  print("Error sintáctico!")
 
# Build the parser
parser = yacc.yacc()
 
#while True:
#  try:
#    s = input('calc > ')
#  except EOFError:
#    break
#  if not s: continue
#  result = parser.parse(s)
#  print(result)



#print(parser.parse(s))
#while True:
#  tok = parser.token()
#  if not tok: 
#    break      # No more input
#  print(tok)

root = Tk()
root.title("Javascript")
root.geometry("500x300")  # width height root


def analyze(data, resul_text_area):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
          result_text_area.insert(tkinter.INSERT, "Error lexico\n")
          break  # No more input
        linea = str(tok)+"\n"
        result_text_area.insert(tkinter.INSERT, linea)
        print(tok)


def analyzeLexico(result_text_area):
    lista=codigo_text_area.get("1.0","end-1c").split("\n")
    result_text_area.delete("1.0", 'end-1c')
    for line in lista:
        if len(line) == 0:
            break
        print(">>>" + line)
        analyze(line, result_text_area)


def analyzeSintactico(result_text_area):
    lista=codigo_text_area.get("1.0","end-1c").split("\n")
    result_text_area.delete("1.0", 'end-1c')
    for line in lista:
        if line != "\n":
            if line[:3] == "for" or line[:5] == "while" or line[:2] == "if":
                nLine = line
                for Eline in lista:
                    nLine += " " + Eline
                    if Eline[:3] == "end":
                        break
                line = nLine
            result = parser.parse(line)
            if result is not None:
                linea = str(result) + "\n"
                result_text_area.insert(tkinter.INSERT, linea)
            else:
                linea = "Error en la sintaxis \n"
                result_text_area.insert(tkinter.INSERT, linea)


def analizador_lexico(codigo_text_area):
    if(existeCodigo(codigo_text_area)):
        analyzeLexico(result_text_area)


def analizador_sintactico(codigo_text_area):
    if (existeCodigo(codigo_text_area)):
        analyzeSintactico(result_text_area)

def existeCodigo(codigo_text_area):
    txt = codigo_text_area.get("1.0", 'end-1c')

    if txt == "":
        return False
    else:
        return True


etiqueta = tkinter.Label(root, text="Analizador JavaScript")
etiqueta.place(x=10, y=10, width=150, height=30)
codigo_text_area = tkinter.Text(root, height=7, width=30,)
codigo_text_area.configure(relief="sunken", borderwidth=1)
codigo_text_area.place(x=10, y=50, width=250, height=200)
boton_lexico = tkinter.Button(root, text=" Analizador Lexico ", padx=40, pady=30,
                              command=lambda: analizador_lexico(codigo_text_area)) 

boton_lexico.place(x=270, y=60, width=150, height=75)

boton_sintactico = tkinter.Button(root, text="Analizador Sintactico", padx=40, pady=30,
                                  command=lambda: analizador_sintactico(codigo_text_area))  # padx lo hara crecer

boton_sintactico.place(x=270, y=150, width=150, height=75)
result_text_area = tkinter.Text(root, height=5, width=40)
result_text_area.configure(relief="sunken", borderwidth=1)
result_text_area.place(x=670, y=60, width=0, height=0)


root.mainloop()