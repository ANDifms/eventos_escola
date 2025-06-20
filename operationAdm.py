from events import eventos
from events import participantes
import includes



def adicionarParticipante():
    print(" -- Adicionar Participante --")
    
    print("\n ---- ADICIONAR NOVO PARTICIPANTE -----")
    
#----------------------------- Gera um novo codigo 
    if participantes: # ve se a participantes no dict
        ultimo_cod = max(int(cod[4:]) for cod in participantes.keys()) #cod > chave de cada dict, cod[4] tira as 4 letras e pega um numeros, int transforma em inteiro
        novo_cod = f"USER{ultimo_cod + 1}" # pega o valor do ultimo codigo e acrecenta + 1
    else:
        novo_cod = "USER001" #se nao tiver nenhum codigo ele começa com esse User
    
    nome = input("Nome: ")
    includes.som_select()

    email = input("Email: ")
    includes.som_select()

    
    cursos = []
    while True:
        curso = input("Qual seu curso de interesse - (fim para encerrar):")
        includes.som_select()
        if curso.lower() == "fim":
            break
        cursos.append(curso)
    
    participantes[novo_cod] = {
        "nome": nome,
        "email": email,
        "cursos_pref": cursos
    }

def editarParticipante():
    print("edtar Participante")
    
def excluirParticipantes():
    print("Excluir Participante")

def voltar():
    print("[0] < voltar")
    
    
    



    

 