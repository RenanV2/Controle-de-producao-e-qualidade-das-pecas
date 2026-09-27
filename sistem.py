# Inicio

piece_id = "P" + str (1)
""" Variável que armazena o id da peça, iniciando em 1."""

def register_piece ():
    # Função que registra as informações da peça, incluindo peso, cor e comprimento.
   
   weight = float (input("Digite o peso: "))
    # Variável que armazena o peso da peça
   
   color = input ("Digite a cor da peça: ").lower ()
    # Variável que armazena a cor da peça
   
   length = float (input("Digite o comprimento da peça: "))
    # Variável que armazena o comprimento da peça

   return weight, color, length

weight, color, length = register_piece ()


def check_weight (weight):
  """ Função que verifica se o peso da peça está dentro do intervalo permitido (95 a 105). """

  if 95 <= weight <= 105:
    return True
  else:
      return "Peso fora do intervalo"
  
def check_color (color):
    """ Função que verifica se a cor da peça está dentro do intervalo permitido (azul ou verde). """

    if color == "azul" or color == "verde":
     return True
    else:
        return "Cor fora do intervalo"

def check_length (length):
  """ Função que verifica se o comprimento da peça está dentro do intervalo permitido (10 a 20). """

  if 10 <= length <= 20:
    return True
  else:
     return "Comprimento fora do intervalo"

def check_all (weight, color, length):
  """ Função que verifica se a peça está aprovada ou reprovada, passando pelas funções de verificação de peso, cor e comprimento. """

  if check_weight (weight) == True and check_color (color) == True and check_length (length) == True:
    return "Peça Aprovada"
  else:
    return "Peça Reprovada"
 
def get_rejection_reasons (weight, color, length):
    """ Função que verifica se a peça tem algum motivo de rejeição. Caso haja, ele é adicionado à lista de motivos de rejeição. """

    rejection_reasons = []

    if check_weight (weight) is not True:
      rejection_reasons.append (check_weight (weight))

    if check_color (color) is not True:
      rejection_reasons.append (check_color (color))

    if check_length (length) is not True:
      rejection_reasons.append (check_length (length))
   
    return rejection_reasons

rejection_reasons = get_rejection_reasons (weight, color, length)

piece = {
   #Dicionário que armazena as informações da peça, incluindo id, peso, cor, comprimento e status (aprovada ou reprovada). 
   

   "id": piece_id,
   "weight": weight,
   "color": color,
   "length": length,
   "status": check_all (weight, color, length),
   "rejection_reasons": rejection_reasons
}

approved_pieces = []
""" Lista que armazena as peças aprovadas. """

reproved_pieces = []
"""" Lista que armazena as peças reprovadas. """

boxes = []
""" Lista que armazena apenas as caixas fechadas. """

current_box = []
""" Lista que armazena a caixa que ainda não está fechada. """

box_capacity = 10
""" Variável que armazena a capacidade máxima de peças por caixa. """


# Verifica se a peça está aprovada ou reprovada e adiciona à lista correspondente. 
if check_all (weight, color, length) == "Peça Aprovada":
    
    approved_pieces.append(piece)
    current_box.append(piece)
 
    if len(current_box) == box_capacity:
       boxes.append(current_box)
       current_box = []
else:
    reproved_pieces.append(piece)

print (f"Motivos de rejeição: {rejection_reasons}")
print (f"Peças aprovadas: {approved_pieces}")
print (f"Peças reprovadas: {reproved_pieces}")

repeat = input ("Deseja cadastrar outra peça? (s/n): ").lower ()
""" Loop que permite cadastrar várias peças, enquanto o usuário desejar. """

while repeat == "s":

    piece_id = "P" + str (int (piece_id[1:]) + 1)
    
    weight, color, length = register_piece ()

    rejection_reasons = get_rejection_reasons(weight, color, length)  
    
    piece = {
        "id": piece_id,
        "weight": weight,
        "color": color,
        "length": length,
        "status": check_all (weight, color, length),
        "rejection_reasons": rejection_reasons
    }

    if check_all (weight, color, length) == "Peça Aprovada":
        
        approved_pieces.append (piece)
        current_box.append (piece)

        if len (current_box) == box_capacity:
           boxes.append(current_box)
           current_box = []

    else:
        reproved_pieces.append (piece)

    print (f"Motivos de rejeição: {rejection_reasons}")
    print (f"Peças aprovadas: {approved_pieces}")
    print (f"Peças reprovadas: {reproved_pieces}")
    print (f"Caixas fechadas: {boxes}")
    print (f"Caixa atual: {current_box}")
    repeat = input ("Deseja cadastrar outra peça? (s/n): ").lower ()  