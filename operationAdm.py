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
    
    print("\n Eventos disponiveis com esse tema:")
    for nome_evento in eventos_tema:
        print(f"- {nome_evento}")
        
    escolha_evento = input("Digite nome do evento: ").strip()
    
    evento_encontrado = None
    for nome_evento in eventos_tema:
        if nome_evento.lower() == escolha_evento.lower():
            evento_encontrado = nome_evento
            break
        
    events.participantes[novo_cod] = {
        "nome": nome,
        "email": email,
        "cursos_pref": [tema_desejado]  # ou outra lógica se tiver múltiplos cursos
    }

    if evento_encontrado:
        events.eventos[evento_encontrado]["participantes"].append(novo_cod)
        print(f"\nParticipante {nome} adicionado com sucesso ao evento '{evento_encontrado}'!")
    else:
        print("Evento não encontrado. Participante salvo, mas sem evento.")
            
            
    
        
def editarParticipante():
    print("edtar Participante")
    
def excluirParticipantes():
    print("Excluir Participante")

def voltar():
    print("[0] < voltar")
    
    
    



    

 