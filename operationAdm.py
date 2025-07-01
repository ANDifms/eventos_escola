import events
import includes
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
    
    while True: 
        cpf = input("Somente numeros: ").strip()
        som_select()
        if cpf.isdigit() and len(cpf) == 11:
            break
        print("Esse CPF parece Falso bonitão")

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
            "cpf": [cpf],
            "cursos_pref": [tema_desejado] # ou outra lógica se tiver múltiplos cursos
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
    print(f"Cpf: {p['cpf']} ")
    print(f"Cursos atuais: {', '.join(p['cursos_pref'])}")

    print("\n[1] Editar nome")
    print("[2] Editar email")
    print("[3] Editar CPF")
    print("[3] Editar cursos")
    print("[0] Cancelar")

    opcao = input("Escolha: ").strip()
    som_select()

    if opcao == "1":
        p["nome"] = input("Novo nome: ")
        som_select()
        print("Nome atualizado!")
    elif opcao == "2":
        p["email"] = input("Novo email: ")
        som_select()
        print("Email atualizado!")
        
    elif opcao == "3":
        p["nome"] = input("Novo CPF: ")
        som_select()
        print("CPF atualizado!")
        
    elif opcao == "4":
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
    
def editarEvento():
    print ("----- EDITAR EVENTO -----")
    
    nome_antigo = input("Digite o nome do Evento: ").strip() # lembre que deu um erro aqui pq voce transformou str em lista
    som_select()
    
    if nome_antigo not in events.eventos: # verifica se o nome existe no dicionario
        print("Tem não Paizão.")
        return
    
    # aqui ele pega dados do evento
    evento = events.eventos[nome_antigo]
    
    # aqui ele mostra todos os dados do evento
    print(f"Tema do Evento: {evento['tema']}")
    print(f"Data do Evento: {evento['data']}")
    print(f"\nHora do Evento: {evento['hora']}")
    print("-"*30)
    
    # Menuzinho de escolha de mudança
    
    print("[1] Editar nome do evento")
    print("[2] Editar data ")
    print("[3] Editar hora")
    print("[4] Editar tema ")
    print("[0] ")
    print("-" * 30)
    
    escolha = input("Escolha: ").strip()
    som_select()
    
    if escolha == "1":
        novo_nome = input("Digite Novo Nome: ").strip()
        som_select()
        
        # validação do novo nome
        if novo_nome in events.eventos:
            print("\033[31mJá tem um Evento com esse nome Paizão. \033[0m")
        else:
            # voce cria um novo evento, copiando todos parametros do antigo, só trocando a chave que é o nome do evento
            # isso por conta que o py nao permite alteração de elementos em dict
            events.eventos[novo_nome] = evento
            del events.eventos[nome_antigo] # apaga o evento antigo 
            
    # 2- editar data
    
    elif escolha == "2":
        evento["data"] = input("Nova dara (Ano-Me-Di): ").strip()
        som_select()
        print("Data Atualizada...")
        
    # 3- editar hora
    
    elif escolha == "3":
        evento["hora"] = input("Nova hora (HH:MM): ").strip()
        som_select()
        print("Hora Atualizada...")
    
    elif escolha == "4":
        evento["tema"] = input("Novo tema: ").strip()
        som_select()
        print("Data Atualizada...")
    
    elif escolha == 0:
        print("Edição Cancelada.")

    else:
        print("opção invalida")

            
def excluirEvento():
    print("Fazendo...")
    print("----- EXCLUIR EVENTO -----")
    
    nome = input("digite o nome do evento: ").strip()
    som_select()
    
    if nome not in events.eventos:
        print("\033[31mEsse evento não existe, meu chapa.\033[0m")
        return
    
    evento = events.eventos[nome]
    print(f"Você tem certeza que deseja excluir esse eventot {nome} ?")
    print(f"Data: {evento['data']}")
    print(f"Hora: {evento['hora']}")
    print(f"Tema: {evento['tema']}")
    print(f"Participantes inscritos: {len(evento['participantes'])}")
  
    confirmação = input("\n Digite 'SIM' para confirmar: ").strip().upper()
    som_select()
    
    if confirmação == "SIM":
        includes.barra_vermelha()
        del events.eventos[nome]
        print(f"\033[32mEvento '{nome}' excluído com sucesso.\033[0m")
    else:
        print("\033[33mExclusão cancelada.\033[0m")
     
    


    

 
 