import sys
import time

from playsound import playsound
#pip playsound instalado

def som_select():
    playsound("arq/ps2-select.mp3")
    
def som_exit():
    playsound("arq/ps2-exit.mp3")
    
    
def barra_progresso(mensagem="Carregando", tamanho=20, duracao=1.5):
    print(f"\n{mensagem}: ", end=" ", flush=True)
    for i in range(tamanho):
        time.sleep(duracao/tamanho)
        sys.stdout.write("█")
        sys.stdout.flush()
    print(" ✔️")
    
def barra_vermelha(mensagem= "Apagando dados...", duracao=2):
    print(f"\n\033[31m{mensagem}\033[0m")

    barra_total = 20
    tempo_por_passo = duracao / barra_total
    
    for i in range(barra_total + 1):
            barra = "█" * i + "-" * (barra_total - i)
            sys.stdout.write(f"\r\033[41m {barra} \033[0m {int(i/barra_total*100)}%")
            sys.stdout.flush()
            time.sleep(tempo_por_passo)
            

def popularidade_dos_eventos(eventos):
    print("\n\033[36m------ Popularidade dos Eventos ------\033[0m\n")

    # Faz a soma total de todos os participantes
    total = sum(len(evento["participantes"]) for evento in eventos.values())

    if total == 0:
        print("Ainda não tem participantes nos eventos.")
        return
    
    for nome, dados in eventos.items():
        inscritos = len(dados["participantes"])   # conta da quantidade de inscritos no evento atual
        porcentagem = int((inscritos/ total) * 100) # faz a porcentagem
        barra_tamanho = 20
        preenchido = int((porcentagem/100) * barra_tamanho) # quanto a barra deve ter preenchido, por base a porcentagem
        barra = "█" * preenchido + "-" * (barra_tamanho - preenchido)

        if porcentagem >= 60:
            cor = "\033[42m"
            # verde
        elif porcentagem >= 40:
            cor = "\033[43m"
            #amarelo
        else:
            cor = "\033[41m"
            #vermelho
        

        print(f"{nome.ljust(20)} | {cor}{barra}\033[0m {porcentagem}% ({inscritos} pessoas)")
        # a variavel cor é colocada aqui pelo {cor} - o \033[0m serve para excluir a cor no final da execução
        # ljust deixa as barrinhas alinhadas a direita    
            