from events import eventos
from events import participantes

def listar_eventos():
    print("Lista de Eventos...")
    
    for nome, info in eventos.items():
        print()
        print(f"Evento: {nome}")
        print(f"Data: {info['data']} ás {info['hora']}")
        print(f"Tema: {info['tema']}")
        print(f"participantes: {len(info['participantes'])}\n") # info é um dicionario com os dados de um evento
    
    
def listar_participantes_evento():
    
    buscar_tema = input("digite o nome do curso-: ").strip()

    codigo_encontrados = set() # tira os codigos duplicados
    
    for nome_evento, info in eventos.items(): # items serve para acessar pares de chaves e o valor ao mesmo tempo de dict
        if info['tema'].lower() == buscar_tema.lower(): # ve se existe o tema digitado com o tema ja existente no banco
            codigo_encontrados.update(info["participantes"]) #adiciona todos os participantes ao conjunto codigo_encontrados
            
    if codigo_encontrados:
        print(f"\nParticipante do curso de {buscar_tema}: \n")
        
        for codigo in codigo_encontrados:
            if codigo in participantes:
                p = participantes[codigo]
                print(f"Nome - {p['nome']}")
                print(f"Email - {p['email']}")
                print(f"Cursos de Preferencia: {', '.join(p['cursos_pref'])}")
                print("-" *30)
    else:
        print(f"\n Tem esse curso não Calabrezo")
            
    
    
    
    
def buscar_participante():
    
    print("Por favor digite o codigo do participante: ")
    res_user = input("-").strip() # resposta do usuario
    
    if res_user in participantes:
        print("----- Matricula ----- ")
        p = participantes[res_user] # p vai armazenar os dados do cliente no caso vai puxar do banco a tag - "codigo"
        print(f"Nome - {p['nome']}")
        print(f"Email - {p['email']}")
        print(f"Cursos de Preferencia: {', '.join(p['cursos_pref'])}")
        print("")
        
    else:
        achados = [ ]
        for codigo, dados in participantes.items(): # vai dentro do events acessa o banco participantes e procura o codigo e os dados igual informado
            if res_user.lower() in dados['nome'].lower(): #pega a resposta e procura em cada dado usando o nome parcial usando o dados > nome
                achados.append((codigo, dados )) # encontra os dados e armazena no achados
        
        
        if achados:
            for codigo, p in achados:
                print("----- Matricula ----- ")
                print(f"ID {codigo}")
                print(f"Nome - {p['nome']}")
                print(f"Email - {p['email']}")
                print(f"Cursos de Preferencia: {', '.join(p['cursos_pref'])}")
                print("")
        else:
            print("Achamo não Paizão")


   

def participantes_ativos():
    print("Mostra os participantes ativos")
    
    contagem = {} # serve para contar quantasd vezes o participante apasrece
    datas_por_curso= {} #guarda as datas
    for evento in eventos.values(): # o for percorre todos os eventos 
        data = evento["data"]
        for codigo in evento["participantes"]: #dentro de cada evento acessamos a cada participantes
            if codigo in contagem: # ve se o codigo ja apareceu no contagem
                contagem[codigo] += 1
            else:
                contagem[codigo] = 1
                
            #sisteminha de datas
            if codigo in datas_por_curso:
                datas_por_curso[codigo].add(data)
            else:
                datas_por_curso[codigo] = {data} 
                
    if not contagem: # caso nao tenha participantes cadastrados
        print("O curso ainda nao possui participantes cadastrados")
        return

#clasifica os participantes mais ativos do maior para o menor
#contagem.items é responsavel por transformar o dicionario contagem em lista de tuplas
    melhores = sorted(contagem.items(), key=lambda item: item[1], reverse=True)

    print("\n ---- Participantes mais ativos ----\n")
    for lugar, (codigo, total) in enumerate(melhores, start=1): # responsavel por percorrer a funcao melhores | enumerate serve para dar numero de posição para cada tupla
        p = participantes.get(codigo, {}) # procura a base de bd do participante, caso contrario tem o {} para evitar erro
        nome = p.get("nome", "Desconhecido")
        email = p.get("email", "sem e-mail")
        datas = sorted(datas_por_curso.get(codigo, [])) # pega a data de cada participante
        print(f"{lugar}. {nome} ({codigo}) - Participou de {total} evento(s) na data {', ' .join(datas)}| {email}")
            
        
    
    
    
    
def temas_frequentes():
    print("Mostra temas mais frequentes ")
    
def sair():
    print("Saindo do sistema...")
    exit()