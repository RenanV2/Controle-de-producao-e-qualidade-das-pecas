# Início

piece_id = "P1"


def register_piece():
    """Registra o peso, a cor e o comprimento da peça."""

    weight = float(input("Digite o peso: "))

    color = input("Digite a cor da peça: ").lower()

    length = float(input("Digite o comprimento da peça: "))

    return weight, color, length


def check_weight(weight):
    """Verifica se o peso está dentro do intervalo permitido."""

    if 95 <= weight <= 105:
        return True
    else:
        return "Peso fora do intervalo"


def check_color(color):
    """Verifica se a cor está dentro das opções permitidas."""

    if color == "azul" or color == "verde":
        return True
    else:
        return "Cor fora do intervalo"


def check_length(length):
    """Verifica se o comprimento está dentro do intervalo permitido."""

    if 10 <= length <= 20:
        return True
    else:
        return "Comprimento fora do intervalo"


def check_all(weight, color, length):
    """Verifica se a peça foi aprovada ou reprovada."""

    if (
        check_weight(weight) is True
        and check_color(color) is True
        and check_length(length) is True
    ):
        return "Peça Aprovada"
    else:
        return "Peça Reprovada"


def get_rejection_reasons(weight, color, length):
    """Identifica e armazena os motivos de rejeição da peça."""

    rejection_reasons = []

    if check_weight(weight) is not True:
        rejection_reasons.append(check_weight(weight))

    if check_color(color) is not True:
        rejection_reasons.append(check_color(color))

    if check_length(length) is not True:
        rejection_reasons.append(check_length(length))

    return rejection_reasons


def create_piece(piece_id):
    """Cria uma peça com seus dados, status e motivos de rejeição."""

    weight, color, length = register_piece()

    rejection_reasons = get_rejection_reasons(
        weight,
        color,
        length
    )

    status = check_all(weight, color, length)

    piece = {
        "id": piece_id,
        "weight": weight,
        "color": color,
        "length": length,
        "status": status,
        "rejection_reasons": rejection_reasons
    }

    return piece


def store_piece(
    piece,
    current_box,
    approved_pieces,
    reproved_pieces,
    boxes,
    box_capacity
):
    """Armazena a peça na lista correspondente e controla as caixas."""

    if piece["status"] == "Peça Aprovada":

        approved_pieces.append(piece)

        current_box.append(piece)

        if len(current_box) == box_capacity:
            boxes.append(current_box)

            current_box = []

    else:
        reproved_pieces.append(piece)

    return current_box


def list_pieces(approved_pieces, reproved_pieces):
    """Lista todas as peças aprovadas e reprovadas."""

    print("\n--- Peças Aprovadas ---\n")

    if not approved_pieces:
        print("Não há peças aprovadas.")
    else:
        for piece in approved_pieces:
            print(f"ID: {piece['id']}")
            print(f"Peso: {piece['weight']}")
            print(f"Cor: {piece['color']}")
            print(f"Comprimento: {piece['length']}")
            print()

    print("\n--- Peças Reprovadas ---\n")

    if not reproved_pieces:
        print("Não há peças reprovadas.")
    else:
        for piece in reproved_pieces:
            print(f"ID: {piece['id']}")
            print(f"Peso: {piece['weight']}")
            print(f"Cor: {piece['color']}")
            print(f"Comprimento: {piece['length']}")
            print(f"Motivo de rejeição: {piece['rejection_reasons']}")
            print()


def list_boxes(boxes, current_box):
    """Lista as caixas fechadas e a caixa que está incompleta."""

    print("\n--- Caixas Completas ---\n")

    if not boxes:
        print("Não possui nenhuma caixa fechada.")
    else:
        for box_number, box in enumerate(boxes, start=1):
            print(f"\nCaixa {box_number}")
            print(f"Quantidade de peças: {len(box)}")

            for piece in box:
                print(f"- {piece['id']}")

    print("\n--- Caixa Incompleta ---\n")

    if not current_box:
        print("Não possui nenhuma caixa incompleta.")
    else:
        print(f"Quantidade de peças: {len(current_box)}")

        for piece in current_box:
            print(f"- {piece['id']}")


def remove_pieces(
    piece_id,
    approved_pieces,
    reproved_pieces,
    current_box,
    boxes,
    box_capacity
):
    """Remove uma peça e reorganiza as caixas quando necessário."""

    for piece in approved_pieces:

        if piece["id"] == piece_id:

            approved_pieces.remove(piece)

            if piece in current_box:

                current_box.remove(piece)

            else:

                for box in boxes:

                    if piece in box:

                        box.remove(piece)

                        boxes.remove(box)

                        current_box.extend(box)

                        if len(current_box) >= box_capacity:
                            boxes.append(current_box[:box_capacity])
                            del current_box[:box_capacity]

                        break

            print(
                f"Sua peça {piece['id']} foi removida com sucesso."
            )

            return True

    for piece in reproved_pieces:

        if piece["id"] == piece_id:

            reproved_pieces.remove(piece)

            print(
                f"Sua peça {piece['id']} foi removida com sucesso."
            )

            return True

    print(
        "Sua peça não foi removida. "
        "Verifique se o ID informado existe e tente novamente."
    )

    return False


approved_pieces = []

reproved_pieces = []

boxes = []

current_box = []

box_capacity = 10


def generate_report(
    approved_pieces,
    reproved_pieces,
    current_box,
    boxes
):
    """Gera o relatório final do sistema."""

    print("\n=== Relatório Final ===\n")

    total_approved = len(approved_pieces)
    total_reproved = len(reproved_pieces)

    print(
        f"Quantidade de peças aprovadas: {total_approved}\n"
        f"Quantidade de peças reprovadas: {total_reproved}"
    )

    print("\n--- Motivos de Reprovação ---\n")

    if total_reproved:

        for piece in reproved_pieces:

            print(f"\n{piece['id']}:")

            for reason in piece["rejection_reasons"]:
                print(f"- {reason}")

    else:
        print("Não existem peças reprovadas.")

    print("\n--- Caixas Utilizadas ---\n")

    total_box = len(boxes)

    if current_box:

        # A caixa incompleta também é considerada uma caixa utilizada.
        total_box += 1

        print(
            f"Quantidade de caixas utilizadas: {total_box}\n"
            f"Caixas fechadas: {total_box - 1}\n"
            f"Caixa incompleta: 1"
        )

    else:

        print(
            f"Quantidade de caixas utilizadas: {total_box}\n"
            f"Caixas fechadas: {total_box}\n"
            f"Caixa incompleta: 0"
        )


def show_menu(
    piece_id,
    approved_pieces,
    reproved_pieces,
    current_box,
    boxes,
    box_capacity
):
    """Exibe o menu e controla o fluxo principal do sistema."""

    selected_option = -1

    while selected_option != 0:

        print(
            "\n=== Controle de Qualidade ==="
            "\n\n1 - Cadastrar nova peça"
            "\n2 - Listar peças aprovadas/reprovadas"
            "\n3 - Remover peça cadastrada"
            "\n4 - Listar caixas fechadas"
            "\n5 - Gerar relatório final"
            "\n0 - Sair"
        )

        selected_option = int(
            input("\nEscolha uma opção: ")
        )

        if selected_option == 1:

            piece = create_piece(piece_id)

            current_box = store_piece(
                piece,
                current_box,
                approved_pieces,
                reproved_pieces,
                boxes,
                box_capacity
            )

            piece_id = "P" + str(int(piece_id[1:]) + 1)

        elif selected_option == 2:

            list_pieces(
                approved_pieces,
                reproved_pieces
            )

        elif selected_option == 3:

            piece_id_to_remove = input(
                "Digite o ID da peça que deseja remover: "
            ).upper()

            remove_pieces(
                piece_id_to_remove,
                approved_pieces,
                reproved_pieces,
                current_box,
                boxes,
                box_capacity
            )

        elif selected_option == 4:

            list_boxes(
                boxes,
                current_box
            )

        elif selected_option == 5:

            generate_report(
                approved_pieces,
                reproved_pieces,
                current_box,
                boxes
            )

        elif selected_option == 0:

            print("\nPrograma encerrado.")

        else:

            print("\nOpção inválida.")


show_menu(
    piece_id,
    approved_pieces,
    reproved_pieces,
    current_box,
    boxes,
    box_capacity
)