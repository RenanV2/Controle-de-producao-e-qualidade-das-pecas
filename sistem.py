# Inicio

rejection_reasons = []
""" Variável que armazena os motivos de rejeição da peça, caso haja algum."""

Weight = float(input("Digite o peso: "))
""" Variável que armazena o peso da peça"""

Color = input("Digite a cor da peça: ").lower()
""" Variável que armazena a cor da peça"""

Length = float(input("Digite o comprimento da peça: "))
""" Variável que armazena o comprimento da peça"""

def check_weight ():
  """ Função que verifica se o peso da peça está dentro do intervalo permitido (95 a 105)."""
  if 95 <= Weight <= 105:
    return True
  else:
      return "Peso fora do intervalo"
  
def check_color():
    """ Função que verifica se a cor da peça está dentro do intervalo permitido (azul ou verde)."""
    if Color == "azul" or Color == "verde":
     return True
    else:
        return "Cor fora do intervalo"

def check_length():
  """ Função que verifica se o comprimento da peça está dentro do intervalo permitido (10 a 20)."""
  if 10 <= Length <= 20:
    return True
  else:
     return "Comprimento fora do intervalo"

def checkAll ():
  """ Função que verifica se a peça está aprovada ou reprovada, passando pelas funções de verificação de peso, cor e comprimento."""
  if check_weight() == True and check_color() == True and check_length() == True:
    return "Peça Aprovada"
  else:
    return "Peça Reprovada"
 
def checkResult():
    """ Função que verifica se a peça tem algum motivo de rejeição. Caso haja, ele é adicionado à lista de motivos de rejeição."""
    if check_weight() is not True:
      rejection_reasons.append(check_weight())
    if check_color() is not True:
      rejection_reasons.append(check_color())
    if check_length() is not True:
      rejection_reasons.append(check_length())

checkResult()
print(checkAll())
print(rejection_reasons)