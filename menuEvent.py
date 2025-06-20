import events
from includes import som_select

def adicionarEvento():
    print(" -- Adicionar Evento --")
    print("\n ---- ADICIONAR NOVO EVENTO -----")

    nome_evento = input("Nome do evento: ").strip()
    som_select()

    data = input("Data do evento (YYYY-MM-DD): ").strip()
    som_select()

    hora = input("Hora do evento (HH:MM): ").strip()
    som_select()

    tema = input("Tema do evento: ").strip()
    som_select()

    # Inicializa a lista de participantes vazia
    participantes = []

    if nome_evento in events.eventos:
        print("\033[31mEvento já existe. Tente outro nome.\033[0m")
        return

    # Adiciona o novo evento ao dicionário
    events.eventos[nome_evento] = {
        "data": data,
        "hora": hora,
        "tema": tema,
        "participantes": participantes
    }

    print(f"\033[32mEvento '{nome_evento}' adicionado com sucesso!\033[0m")