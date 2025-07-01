import includes
#import operationAdm


from operationAdm import(
    adicionarEvento,
    editarEvento,
    excluirEvento
    # voltar
)

menu_opcoes = {
    "1": adicionarEvento,
    "2": editarEvento,
    "3": excluirEvento,
    # "0": voltar
}

def menu_adm_eventos():
    while True:
        print("\n ----- GERENCIAR EVENTOS -----")
        print("[1] Adicionar Evento")
        print("[2] edtar Evento")
        print("[3] Excluir Evento")
        print("[0] < voltar")
        
        escolha = input("Qual sua escolha: ")
        includes.som_select()
        
        if escolha == "0":
            break

    
        funcao = menu_opcoes.get(escolha)
        
        if funcao:
            funcao()
        else:
            print("Tem não Patrão")
        