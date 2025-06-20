import includes
# o valor selecionado vai ser a função que vai ser executada
from operations import(
    listar_eventos,
    listar_participantes_evento,
    buscar_participante,
    participantes_ativos,
    temas_frequentes,
    login_Adm,
    sair
)

def menu_principal():
    menu_opcoes ={
        "1": listar_eventos,
        "2": listar_participantes_evento,
        "3": buscar_participante,
        "4": participantes_ativos,
        "5": temas_frequentes,
        "6": login_Adm,
        "0": sair
    }

    while True:
        print("--- MENU PRINCIPAL DO EVENTO ---")
        print("[1] - Listar todos os eventos  ")
        print("[2] - Listar participantes de um evento  ")
        print("[3] - Buscar participante")
        print("[4] - Mostrar participantes mais ativos ")
        print("[5] - Mostrar temas mais frequentes ")
        print("[6] ADM")
        print("[0] - Sair ")
        
        #funcao get serve para acessar um valor de uma chave em um dicionario
        escolha = input("Qual sua escolha: ")
        includes.som_select()
    
        funcao = menu_opcoes.get(escolha)
        
        
        #validação -----
        if funcao:
            funcao()
        else:
            print("Calma la paizao, tem não")
            
if __name__ == "__main__":
    menu_principal()