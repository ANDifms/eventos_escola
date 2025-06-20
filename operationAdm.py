import events
from includes import som_select


def adicionarParticipante():
    print(" -- Adicionar Participante --")
    
    print("\n ---- ADICIONAR NOVO PARTICIPANTE -----")
    
#----------------------------- Gera um novo codigo 
    if events.participantes: # ve se a participantes no dict
        ultimo_cod = max(int(cod[4:]) for cod in events.participantes.keys()) #cod > chave de cada dict, cod[4] tira as 4 letras e pega um numeros, int transforma em inteiro
        novo_cod = f"USER{ultimo_cod + 1}" # pega o valor do ultimo codigo e acrecenta + 1
    else:
        novo_cod = "USER001" #se nao tiver nenhum codigo ele começa com esse User
    
    nome = input("Nome: ")
    som_select()

    email = input("Email: ")
    som_select()

    

    
    # ---------- mostrar cursos
    
    print("\n Eventos disponiveis: ")
    temas_disponiveis = set(evento["tema"] for evento in events.eventos.values())
    for tema in sorted(temas_disponiveis):
        print(f"- {tema}")
        
    tema_desejado = input("Digite o Evento que quer participar: ")
    som_select()
    
    eventos_tema = {nome: dados for nome, dados in events.eventos.items() if dados["tema"].lower() == tema_desejado.lower()} # cria um dicionario de comprenção, percorre todo o dicionario e volta com dois valores (nome_evento dado evento)
    
    if not eventos_tema:
        print("Tem esse evento nao Paizão, Participante salvo sem evento")
        return
    
    #com ele aqui fora salva só uma vez
    events.participantes[novo_cod] = {
            "nome": nome,
            "email": email,
            "cursos_pref": [tema_desejado]  # ou outra lógica se tiver múltiplos cursos
        }

    print("\n Eventos disponiveis com esse tema:")
    for nome_evento in eventos_tema:
        print(f"- {nome_evento}")
        
        escolha_evento = input("Digite nome do evento: ").strip()
    
   
        evento_encontrado = None
        for nome_evento in eventos_tema:
            if nome_evento.lower() == escolha_evento.lower():
                evento_encontrado = nome_evento
                break
            
        
        if evento_encontrado:
            events.eventos[evento_encontrado]["participantes"].append(novo_cod)
            print(f"\nParticipante {nome} adicionado com sucesso ao evento '{evento_encontrado}'!")
            print(f"\033[32m\nParticipante {nome} adicionado com sucesso!! \033[0m")
        else:
            print("")
            print("\033[31mEvento não encontrado. Participante salvo, mas sem evento.\033[0m")

                
            
    
        
def editarParticipante():
    print("---- Editar Participante ----")
    
    codigo = input("Digite o código do participante (ex: USER254): ").strip().upper()
    som_select()

    if codigo not in events.participantes:
        print("Participante não encontrado.")
        return

    p = events.participantes[codigo]

    print(f"\nNome atual: {p['nome']}")
    print(f"Email atual: {p['email']}")
    print(f"Cursos atuais: {', '.join(p['cursos_pref'])}")

    print("\n[1] Editar nome")
    print("[2] Editar email")
    print("[3] Editar cursos")
    print("[0] Cancelar")

    opcao = input("Escolha: ").strip()
    som_select()

    if opcao == "1":
        p["nome"] = input("Novo nome: ")
        som_select()
        print("Nome atualizado.")
    elif opcao == "2":
        p["email"] = input("Novo email: ")
        som_select()
        print("Email atualizado.")
    elif opcao == "3":
        novos_cursos = []
        while True:
            curso = input("Digite um curso (ou 'fim' para encerrar): ").strip()
            if curso.lower() == "fim":
                break
            novos_cursos.append(curso)
        p["cursos_pref"] = novos_cursos
        print("Cursos atualizados.")
    elif opcao == "0":
        print("Edição cancelada.")
    else:
        print("Opção inválida.")
        
            
def excluirParticipante():
    print("---- Excluir Participante ----")

    codigo = input("Código do participante (ex: USER254): ").strip().upper()
    som_select()

    if codigo not in events.participantes:
        print("Participante não encontrado.")
        return

    # Remove dos eventos
    for evento in events.eventos.values():
        if codigo in evento["participantes"]:
            evento["participantes"].remove(codigo)

    # Remove do dicionário principal
    del events.participantes[codigo]

print("\033[32mParticipante excluído com sucesso.\033[0m") # imprime o resultado e deixa verde

def voltar():
    print("[0] < voltar")
    
    
    



    

 