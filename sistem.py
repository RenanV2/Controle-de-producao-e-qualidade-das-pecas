# Inicio


piece_id = "P" + str (1)
""" Variável que armazena o id da peça, iniciando em 1."""

def register_piece ():
  """ Função que registra as informações da peça, incluindo peso, cor e comprimento."""
   
  weight = float (input("Digite o peso: "))
   # Variável que armazena o peso da peça
   
  color = input ("Digite a cor da peça: ").lower ()
   # Variável que armazena a cor da peça
   
  length = float (input("Digite o comprimento da peça: "))
    # Variável que armazena o comprimento da peça

  return weight, color, length

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

def create_piece (piece_id):
  """ Função que cria a peça, chamando a função de registro de peça. """

  weight, color, length = register_piece()
  
  rejection_reasons = get_rejection_reasons (weight, color, length)

  status = check_all (weight, color, length)
   
  piece = {
    #Dicionário que armazena as informações da peça, incluindo id, peso, cor, comprimento e status (aprovada ou reprovada). 
    
    "id": piece_id,
    "weight": weight,
    "color": color,
    "length": length,
    "status": status,
    "rejection_reasons": rejection_reasons
  }

  return piece

def store_piece (piece, current_box, approved_pieces, reproved_pieces, boxes, box_capacity):
  """Função que armazena as informações da peças no local correto"""
  
  if piece["status"] == "Peça Aprovada":

    approved_pieces.append(piece)

    current_box.append(piece)

    if len(current_box) == box_capacity:
        boxes.append(current_box)
        
        current_box = []

  else:
    reproved_pieces.append(piece)

  return current_box

def list_pieces (approved_pieces, reproved_pieces):
  """Função que listará todas as peças aprovadas e reprovadas"""

  print ("\n--- Peças Aprovadas ---")
  
  if not approved_pieces:
    print("Não há peças aprovadas")
  else:  

    for piece in approved_pieces:

      print (f"Id: {piece['id']}")
      print (f"Peso: {piece['weight']}")
      print (f"Cor: {piece['color']}")
      print (f"Comprimento: {piece['length']}")
      print ()

  print ("\n--- Peças Reprovadas ---")

  if not reproved_pieces:
      print ("Não há peças reprovadas")
  
  else:
    for piece in reproved_pieces:

      print (f"Id: {piece['id']}")
      print (f"Peso: {piece['weight']}")
      print (f"Cor: {piece['color']}")
      print (f"Comprimento: {piece['length']}")
      print (f"Motivo de Rejeição: {piece['rejection_reasons']}")

def list_boxes (boxes, current_box):
  """Função que listará todas as caixas completas."""
  
  print ("\n--- Caixas Completas ---")

  if not boxes:

    print ("Não Possui nenhuma caixa fechada")

  else:
    for box_number, box in enumerate (boxes, start = 1):
      print (f"\nCaixa {box_number}")
      print (f"Quantidade de peças: {len(box)}")

      for piece in box:
        print(f"- {piece['id']}")

  print ("\n --- Caixas Incompleta ---")

  if not current_box:
    print ("Não possui nenhuma caixa incompleta")
  
  else:
    for piece in current_box:
      print (f"- {piece['id']}")

def remove_pieces (piece_id, approved_pieces, reproved_pieces, current_box, boxes, box_capacity):

  for piece in approved_pieces:

    if piece ["id"] == piece_id:

      approved_pieces.remove (piece)

      if piece in current_box :

        current_box.remove (piece)

      else:

        for box in boxes:

          if piece in box:

            box.remove (piece)

            boxes.remove (box)

            current_box.extend (box)

            if len (current_box) >= box_capacity:

              boxes.append (current_box[:box_capacity])
              del current_box[:box_capacity]

            break

      print (f"Sua peça {piece['id']} foi removida com sucesso")

      return True

  for piece in reproved_pieces:

    if piece ["id"] == piece_id:

      reproved_pieces.remove (piece)

      print (f"Sua peça {piece['id']} foi removida com sucesso")

      return True

  print ("Sua peça não foi removida verifique se existe a peça escolhida e tente novamente")
  
  return False 

approved_pieces = []
""" Lista que armazena as peças aprovadas. """

reproved_pieces = []
"""" Lista que armazena as peças reprovadas. """

boxes = []
""" Lista que armazena apenas as caixas fechadas. """

current_box = []
""" Lista que armazena a caixa que ainda não está fechada. """

box_capacity = 2
""" Variável que armazena a capacidade máxima de peças por caixa. """

# Chamando as funcões create_piece e current_box
#piece = create_piece (piece_id)
#current_box = store_piece (piece, current_box, approved_pieces, reproved_pieces, boxes, box_capacity)

def show_menu (piece_id, approved_pieces, reproved_pieces, current_box, boxes, box_capacity):

  chose_option = -1

  while chose_option != 0:

    print ("\n --- Controle de qualidade ---" \
    "\n\n 1 - Cadastrar nova peça " \
    "\n 2 - Listar peças aprovadas/reprovadas" \
    "\n 3 - Remover peça cadastrada" \
    "\n 4 - Listar caixas fechadas" \
    "\n 5 - Gerar relatório final" \
    "\n 0 - Sair ")

    chose_option = int (input ("\n Escolha uma opção: "))

    if chose_option == 1:

      piece = create_piece (piece_id)

      current_box = store_piece (piece, current_box, approved_pieces, reproved_pieces, boxes, box_capacity)

      piece_id = "P" + str (int (piece_id[1:]) + 1)

    elif chose_option == 2:

      list_pieces (approved_pieces, reproved_pieces)

    elif chose_option == 3:

      piece_id_to_remove = input ("Digite o ID da peça que deseja remover: ").upper()

      removed = remove_pieces (piece_id_to_remove, approved_pieces, reproved_pieces, current_box, boxes, box_capacity)

    elif chose_option == 4:

      list_boxes (boxes, current_box)

    elif chose_option == 5:

      ()

    elif chose_option == 0:

      print("Programa encerrado.")

    else:

      print ("\n Opção Inválida")


show_menu (piece_id, approved_pieces, reproved_pieces, current_box, boxes, box_capacity)

# list_pieces(approved_pieces, reproved_pieces)
# list_boxes (boxes, current_box)

# # Criando laço de repetição enquanto a resposta for "s"
# repeat = input ("Deseja cadastrar outra peça? (s/n): ").lower ()

# while repeat == "s":

#   piece_id = "P" + str (int (piece_id[1:]) + 1)

#   want_to_remove = input ("Você deseja remover alguma peça? ").lower()

#   if want_to_remove == "s":

#     piece_id_to_remove = input ("Digite o ID da peça que deseja remover: ").upper()

#     removed = remove_pieces (piece_id_to_remove, approved_pieces, reproved_pieces, current_box, boxes, box_capacity)

    
#     if removed:
#           print ("Peça removida com sucesso.")
#     else: ("Peça não encontrada.")

  
#   piece = create_piece (piece_id)

#   current_box = store_piece (
#   piece, 
#   current_box, 
#   approved_pieces, 
#   reproved_pieces, 
#   boxes, 
#   box_capacity
#   )

#   list_pieces(approved_pieces, reproved_pieces)
#   list_boxes(boxes, current_box)

#   repeat = input ("Deseja cadastrar outra peça? (s/n): ").lower () 