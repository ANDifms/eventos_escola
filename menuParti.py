import includes


from operationAdm import(
    adicionarParticipante,
    editarParticipante,
    excluirParticipantes
    # voltar
)

menu_opcoes = {
    "1": adicionarParticipante,
    "2": editarParticipante,
    "3": excluirParticipantes,
    # "0": voltar
}

def menu_adm_participantes():
    while True:
        print("\n ----- GERENCIAR PARTICIPANTES -----")
        print("[1] Adicionar Participante")
        print("[2] edtar Participante")
        print("[3] Excluir Participante")
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
        