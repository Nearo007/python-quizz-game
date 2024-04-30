# Leandro 24-04 final

import threading
import random

def main():
    while True:
        try:
            class Pergunta:
                def __init__(self, pergunta, dica, resposta, dificuldade, categoria):
                    self.pergunta = pergunta
                    self.dica = dica
                    self.resposta = resposta
                    self.dificuldade = dificuldade
                    self.categoria = categoria

            def selecionar_perguntas(lista_de_perguntas):
                perguntas_respostas_todas = []
                perguntas_respostas_final = []

                if modo_categoria == 2:
                    for p in lista_de_perguntas:  # filtra as pergunta de acordo com a dificuldade e categoria
                        if p.dificuldade == modo_dificuldade and p.categoria == pergunta_categoria:
                            perguntas_respostas_todas.append(p)
                else:
                    for p in lista_de_perguntas:  # filtra as pergunta de acordo com dificuldade
                        if p.dificuldade == modo_dificuldade:
                            perguntas_respostas_todas.append(p)

                random.shuffle(perguntas_respostas_todas)

                for i in range(5):
                    perguntas_respostas_final.append(perguntas_respostas_todas[i])

                return perguntas_respostas_final

            def selecionar_dificuldade(dificuldade):
                tempo_resposta = 10

                if dificuldade == 2:
                    tempo_resposta = 12

                elif dificuldade == 3:
                    tempo_resposta = 15

                return tempo_resposta

            modo_player = int(input("\nBem-vindo ao jogo de perguntas e respostas!\nQuantos jogadores:\n"))
            modo_dificuldade = int(input("Dificuldade: 1, 2 ou 3?\n"))
            modo_dificuldade_adaptativa = int(input("Dificuldade adaptativa: 1 (DESATIVADO) ou 2 (ATIVADO)?\n"))
            modo_dica = int(input("Dicas: 1 (DESATIVADO) ou 2 (ATIVADO)?\n"))
            modo_estudo = int(input("Deseja ativar o modo treinamento? 1 (DESATIVADO) ou 2 (ATIVADO)\n"))
            modo_categoria = int(input("Deseja uma categoria especifica? 1 (DESATIVADO) ou 2 (ATIVADO)?\n"))

            if modo_categoria == 2:
                pergunta_categoria = str(input("Qual categoria? (Ciência, História, Matemática, Português)\n"))
                pergunta_categoria = pergunta_categoria.lower().strip()

            tempo_resposta = selecionar_dificuldade(modo_dificuldade)

            perguntas_respostas_sem_filtro = [
                    # Perguntas portugues facil
                    Pergunta("Qual é o antônimo de feliz?", "Antônimo é o oposto", "Triste", 1, "português"),
                    Pergunta("Qual o plural de cachorro?", "Plural indica mais de um", "Cachorros", 1, "português"),
                    Pergunta("Quantas sílabas tem a palavra: Paralelepípedo?", "Som que se pronuncia de uma vez só", "7", 1, "português"),
                    Pergunta("Qual é a primeira pessoa do singular?", "Possui duas letras", "Eu", 1, "português"),
                    Pergunta("Qual é o antônimo de 'bom'?", "Palavra que indica algo ruim", "Ruim", 1, "português"),
                    Pergunta("Qual é a cor oposta ao preto?", "Cor que reflete todas as outras", "Branco", 1, "português"),
                    Pergunta("Quantas patas tem um quadrúpede?", "Uma gato é um quadrúpede", "4", 1, "português"),
                    Pergunta("O que é uma vogal?", "Tipo de fonema com som aberto", "Fonema", 1, "português"),
                    Pergunta("Qual é o antônimo de 'alto'?", "Oposto de 'elevado'", "Baixo", 1, "português"),
                    Pergunta("Qual o tempo verbal: 'Ela estudava'?\na) Passado.\nb) Presente.\nc) Futuro.",
                             "Observe a conjugação do verbo", "A", 1, "português"),
                    # Peguntas portugues medio
                    Pergunta("Qual plural de lápis?", "Plural indica mais de um", "Lápis", 2, "português"),
                    Pergunta("Qual é o sujeito da frase 'Os pássaros cantam pela manhã.'?", "O sujeito é quem executa o verbo", "Pássaros", 2, "português"),
                    Pergunta("Qual das palavras NÂO é um verbo na frase: 'Estou indo jogar bola.'?", "Verbo é a ação", "bola", 2, "português"),
                    Pergunta("Qual é o adjetivo da frase 'Hoje ela está muito linda.'?", "Acrescenta característica", "Linda", 2, "português"),
                    Pergunta("Qual é o plural de livro?", "Plural indica mais de um", "Livros", 2, "português"),
                    Pergunta("Qual é o objeto direto da frase 'Eu comprei um carro novo'?", "Recebe a ação do verbo diretamente", "Carro", 2, "português"),
                    Pergunta("Qual das palavras é um substantivo na frase: 'Ela gosta de nadar na piscina.'?", "Substantivo é um nome", "piscina", 2, "português"),
                    Pergunta("Qual é o antônimo de 'bem'?", "Palavra com significado oposto", "Mal", 2, "português"),
                    Pergunta("Qual é a conjunção na frase 'Ela estudou bastante, mas não passou no exame'?", "Conjunção une elementos da frase", "Mas", 2, "português"),
                    Pergunta("Qual é a sílaba tônica de uma palavra proparoxítona?\na) Antepenúltima.\nb) Penúltima.\nc) Última.",
                            "Sílaba onde está o acento", "A", 2, "português"),
                    # Perguntas portugues dificil
                    Pergunta("Qual é a função sintática da palavra 'com' na frase 'Ela saiu com pressa.'?", "O que ela está fazendo com as outras palavras?", "Preposição", 3, "português"),
                    Pergunta("Qual antônimo de 'efervescente'?", "Antônimo é o oposto", "Inerte", 3, "português"),
                    Pergunta("Qual é o sinônimo de 'alegre'?", "Palavra com significado similar", "Feliz", 3, "português"),
                    Pergunta("Qual é o antônimo de 'externo'?", "Palavra com significado oposto", "Interno", 3, "português"),
                    Pergunta("Qual é a função da vírgula na frase 'O menino, que estava cansado, dormiu cedo'?", "Indica uma pausa na frase", "Indicação", 3, "português"),
                    Pergunta("O que é uma interjeição?", "Palavra que expressa emoção ou sentimento", "Expressão", 3, "português"),
                    Pergunta("O que é uma metáfora?", "Figura de linguagem que estabelece uma relação de semelhança entre dois termos", "Comparação", 3, "português"),
                    Pergunta("O que é uma prosopopeia?", "Figura de linguagem que atribui características humanas a seres inanimados", "Personificação", 3, "português"),
                    Pergunta("Qual o masculino de baleia?", "É uma palavra paroxítona", "Caxarela", 3, "português"),
                    Pergunta("Qual o plural de cônsul?\na) Cônsulos.\nb) Cônsules.\nc) Cônsulas.",
                            "É uma palavra paroxítona", "B", 3, "português"),
                    # Perguntas matematica facil
                    Pergunta("Qual a raiz quadrada de 144?", "Menor que 15", "12", 1, "matemática"),
                    Pergunta("Qual a raiz quadrada de 49?", "Entre 5 e 9", "7", 1, "matemática"),
                    Pergunta("Quanto é 45 + 60?", "Entre 100 e 110", "105", 1, "matemática"),
                    Pergunta("Quanto é 10²?", "Entre 50 e 150", "100", 1, "matemática"),
                    Pergunta("Qual é o próximo número da sequência: 2, 4, 6, 8, ?", "Sequência de números pares", "10", 1, "matemática"),
                    Pergunta("Quanto é 20 dividido por 5?", "Entre 3 e 5", "4", 1, "matemática"),
                    Pergunta("Qual é o dobro de 8?", "Maior que 10", "16", 1, "matemática"),
                    Pergunta("Quanto é 3 x 4?", "Entre 10 e 15", "12", 1, "matemática"),
                    Pergunta("Quanto é 25 x 5?", "Entre 120 e 130", "125", 1, "matemática"),
                    Pergunta("Qual desses NÃO é primo?\na) 5.\nb) 7.\nc) 9.",
                             "Possui raiz quadrada", "C", 1, "matemática"),
                    # Perguntas matematica medio
                    Pergunta("Qual a área de um quadrado com lado de 14?", "Todos os lados possuem o mesmo comprimento", "196", 2, "matemática"),
                    Pergunta("Qual é a soma dos ângulos internos de um triângulo?", "Não depende da forma ou tamanho do triângulo", "180", 2, "matemática"),
                    Pergunta("Quanto é 115 - 75?", "entre 35 e 45", "40", 2, "matemática"),
                    Pergunta("Quanto é 40 x 8", "entre 300 e 350", "320", 2, "matemática"),
                    Pergunta("Quanto é 33 + 77?", "Entre 90 e 120", "110", 2, "matemática"),
                    Pergunta("Qual é a raiz quadrada de 144?", "É um número inteiro", "12", 2, "matemática"),
                    Pergunta("Quanto é 20 dividido por 4?", "Entre 3 e 5", "5", 2, "matemática"),
                    Pergunta("Quanto é 25 menos 12?", "Entre 10 e 20", "13", 2, "matemática"),
                    Pergunta("Quanto é 30 dividido por 3?", "Entre 5 e 10", "10", 2, "matemática"),
                    Pergunta("Quanto é 15 elevado a 0?\na) 1.\nb) 15.\nc) 0.",
                             "Há uma regra especifica para essa potencia", "A", 2, "matemática"),
                    # Perguntas matematica dificil
                    Pergunta("Um número é aumentado em 20%, o resultado é 180. Qual é esse número?", "Menor que o resultado", "150", 3, "matemática"),
                    Pergunta("Se um triângulo equilátero tem um perímetro de 36, qual é o comprimento de cada lado?", "Todos os lados possuem a mesmo comprimento", "12", 3, "matemática"),
                    Pergunta("Quanto é (20 x 8) - 40?", "Entre 100 e 150", "120", 3, "matemática"),
                    Pergunta("Quanto é a metade de (√144) x 5?", "Entre 10 e 75", "30", 3, "matemática"),
                    Pergunta("Qual é o dobro da raiz quadrada de 81?", "É um número inteiro", "18", 3, "matemática"),
                    Pergunta("Quanto é 3 x 45?", "É a metade de 270", "135", 3, "matemática"),
                    Pergunta("Qual é o triplo do logaritmo de 1?", "Resultado é menor que o número original", "0", 3, "matemática"),
                    Pergunta("Qual é o valor do seno de 90 graus?", "Valor máximo", "1", 3, "matemática"),
                    Pergunta("Qual é a derivada de x^2?", "Função quadrática", "2x", 3, "matemática"),
                    Pergunta("Uma loja vende camisetas a 20 cada. Se a loja oferece um desconto de 25%, quanto irá custar 5 camisetas?\na) 85.\nb) 90.\nc) 75.",
                             "'25%' equivale a 1 quarto", "C", 3, "matemática"),
                    # Perguntas historia facil
                    Pergunta("Aonde foram construídas as pirâmides de Gizé?", "Perto do rio Nilo", "Egito", 1, "história"),
                    Pergunta("Quem escreveu 'A origem das Espécies'?", "Autor da teoria da evolução", "Charles Darwin", 1, "história"),
                    Pergunta("Qual o nome do criador da teoria da relatividade?", "Físico mais conhecido do mundo", "Albert Einstein", 1, "história"),
                    Pergunta("De quem é a frase 'Só sei que nada sei'?", "Filósofo", "Sócrates", 1, "história"),
                    Pergunta("Qual foi o nome do primeiro homem a pisar na Lua?", "Astronauta da missão Apollo 11", "Neil Armstrong", 1, "história"),
                    Pergunta("Quem foi o fundador da cidade de Roma, segundo a lenda romana?", "Figura mitológica", "Rômulo", 1, "história"),
                    Pergunta("Qual era o nome do navio de Cristóvão Colombo em sua primeira viagem às Américas?", "Navegação para as Índias", "Santa Maria", 1, "história"),
                    Pergunta("Quem foi o primeiro presidente do Brasil?", "Líder da proclamação da República", "Marechal Deodoro", 1, "história"),
                    Pergunta("Quem foi a rainha da Inglaterra durante a época da Armada Espanhola?", "Conhecida como a 'Rainha Virgem'", "Elizabeth I", 1, "história"),
                    Pergunta("Qual o primeiro nome do presidente do Brasil?\na) Jair\nb) Luiz\nc) Luciano",
                             "Só consegue contar até 9", "B", 1, "história"),
                    # Perguntas historia medio
                    Pergunta("Quem foi o primeiro presidente dos Estados Unidos?", "Conhecido como 'Pai da Nação'", "George Washington", 2, "história"),
                    Pergunta("Quem foi o líder da Revolução Cubana?", "Famoso guerrilheiro latino-americano", "Fidel Castro", 2, "história"),
                    Pergunta("Qual civilização antiga construiu as pirâmides no Egito?", "Civilização do rio Nilo", "Egípcios", 2, "história"),
                    Pergunta("Quem foi o imperador romano conhecido por ter incendiado Roma?", "Imperador notório da Roma Antiga", "Nero", 2, "história"),
                    Pergunta("Qual foi o evento que marcou o início da Segunda Guerra Mundial?", "Invasão de um país europeu", "Invasão da Polônia", 2, "história"),
                    Pergunta("Quem foi o líder da resistência pacífica na Índia contra o domínio britânico?", "Líder espiritual e político", "Mahatma Gandhi", 2, "história"),
                    Pergunta("Quem inventou o avião?", "Existe um aeroporto com seu nome", "Santos Dumont", 2, "história"),
                    Pergunta("Quem descobriu o Brasil?", "em 1500", "Pedro Álvares Cabral", 2, "história"),
                    Pergunta("Quando acabou a Segunda Guerra Mundial?", "Entre 1943 e 1947", "1945", 2, "história"),
                    Pergunta("Qual a razão para as Cruzadas?\na) Dinheiro\nb) Religião\nc) Território",
                            "Palestina e Jerusalém eram o alvo", "B", 2, "história"),
                    # Perguntas historia dificil
                    Pergunta("Qual era o nome do líder militar espartano na Batalha das Termópilas?", "conhecido por sua coragem e lealdade à sua pátria", "Leônidas", 3, "história"),
                    Pergunta("Qual era o nome da dinastia que governou a China por mais de 2.000 anos", "O governo durou até o fim do século XX", "Qing", 3, "história"),
                    Pergunta("Qual foi o nome do primeiro faraó do Egito?", "Unificador do Alto e Baixo Egito", "Narmer", 3, "história"),
                    Pergunta("Quem foi o primeiro homem a circum-navegar o globo?", "Navegador português", "Fernão de Magalhães", 3, "história"),
                    Pergunta("Qual foi a capital do Império Romano do Ocidente?", "Cidade eternizada por seu Coliseu", "Roma", 3, "história"),
                    Pergunta("Quem foi o fundador do Império Mongol?", "Conquistador asiático", "Genghis Khan", 3, "história"),
                    Pergunta("Qual foi o evento que marcou o fim da Primeira Guerra Mundial?", "Tratado que encerrou o conflito", "Tratado de Versalhes", 3, "história"),
                    Pergunta("Quem foi o líder militar francês que se tornou imperador?", "Vitorioso na Batalha de Austerlitz", "Napoleão Bonaparte", 3, "história"),
                    Pergunta("Quem inventou o telefone?\na) Nikola Tesla. \nb) Marie Curie. \nc) Alexander Graham Bell.",
                        "Cientista de origem escocesa", "C", 3, "história"),
                    Pergunta("Qual o líder político liderou a União Soviética durante a Guerra Fria?\na) Stalin.\nb) Hitler.\nc) Putin.",
                            "Conhecido por sua liderança autoritária", "A", 3, "história"),
                    # Perguntas ciencia facil
                    Pergunta("Quantos planetas existem no sistema solar?", "Mais do que 7 planetas", "8", 1, "ciência"),
                    Pergunta("Qual é o menor planeta do sistema solar?", "Começa com M", "Mercúrio", 1, "ciência"),
                    Pergunta("Qual é o planeta conhecido como o 'gigante gasoso'?", "Começa com J", "Júpiter", 1, "ciência"),
                    Pergunta("Qual é o planeta mais próximo do Sol?", "Começa com M", "Mercúrio", 1, "ciência"),
                    Pergunta("Qual é o planeta conhecido como o 'planeta vermelho'?", "Começa com M", "Marte", 1, "ciência"),
                    Pergunta("Qual é o maior planeta do sistema solar?", "Começa com J", "Júpiter", 1, "ciência"),
                    Pergunta("Qual é o planeta conhecido como o 'planeta dos anéis'?", "Começa com S", "Saturno", 1, "ciência"),
                    Pergunta("Qual é o único planeta do sistema solar que possui vida conhecida?", "Planeta água", "Terra", 1, "ciência"),
                    Pergunta("Qual desses minérios é um combustível fóssil?\na) Bronze.\nb) Carvão Mineral.\nc) Ferro.", "Fonte de energia não renovável", "B", 1, "ciência"),
                    Pergunta("Qual desses animais produz o mel?\na) Abelha.\nb) Borboleta.\nc) Formiga.",
                            "Inceto que vive em uma colméia", "A", 1, "ciência"),
                    # Perguntas ciencia medio
                    Pergunta("Qual é o processo pelo qual as plantas convertem a luz solar em energia química?", "Processo fundamental para as plantas", "Fotossíntese", 2, "ciência"),
                    Pergunta("Qual elemento químico é representado pelo símbolo 'He'?", "É um gás nobre", "Hélio", 2, "ciência"),
                    Pergunta("Qual é o nome dado à menor unidade estrutural e funcional de um organismo vivo?", "Constitui os blocos de construção dos seres vivos", "Célula", 2, "ciência"),
                    Pergunta("Qual é o ácido presente nas frutas cítricas?", "Contribui para o sabor azedo", "Cítrico", 2, "ciência"),
                    Pergunta("Quantos ossos tem o corpo humano adulto?", "É mais de 200", "206", 2, "ciência"),
                    Pergunta("Qual é a unidade básica de medida de tempo no sistema internacional?", "É uma fração de um dia", "Segundo", 2, "ciência"),
                    Pergunta("Qual é a força que atrai dois corpos massivos um para o outro?", "Importante na mecânica celeste", "Gravidade", 2, "ciência"),
                    Pergunta("O que é um exoplaneta?", "Planeta fora do nosso sistema solar", "Exoplaneta", 2, "ciência"),
                    Pergunta("Qual a fórmula química da água oxigenada?\na) H2O\nb) H2O2\nc) H2O3",
                              "Mesma quantidade de cada elemento", "B", 2, "ciência"),
                    Pergunta("Qual o valor de 1 mol?\na) 6,02 x 10²¹\nb) 6,02 x 10²²\nc) 6,02 x 10²³",
                             "A unidade de mol se refere ao número de moléculas, íons e átomos, segundo os químicos.", "C", 2, "ciência"),
                    # Perguntas ciencia dificil
                    Pergunta("Qual é a força fundamental que mantém os elétrons orbitando ao redor do núcleo de um átomo?", "Responsável por manter a coesão entre partículas carregadas eletricamente", "Eletromagnética", 3, "ciência"),
                    Pergunta("Qual é o nome da unidade de medida de energia no sistema internacional de unidades (SI)?", "Começa com J", "Joule", 3, "ciência"),
                    Pergunta("Qual é a unidade de medida de corrente no sistema internacional de unidades (SI)?", "Começa com A", "Ampere", 3, "ciência"),
                    Pergunta("Qual é a unidade de medida de massa no sistema internacional de unidades (SI)?", "Uma das unidades fundamentais de medida", "Quilograma", 3, "ciência"),
                    Pergunta("Como é chamado o estudo das interações entre os organismos e o seu ambiente físico?", "Envolve as relações entre seres vivos e o meio em que vivem", "Ecologia", 3, "ciência"),
                    Pergunta("Qual é o nome do processo pelo qual o DNA é copiado?", "Processo essencial para a replicação do material genético", "Replicação", 3, "ciência"),
                    Pergunta("Qual é o nome do processo onde o calor é transferido de um corpo para outro pela à diferença de temperatura?", "Pode ocorrer por condução, convecção ou radiação", "Transferência", 3, "ciência"),
                    Pergunta("Qual é o nome da substância química que é liberada pelos neurônios para transmitir sinais para outras células?", "Comunicação entre células nervosas", "Neurotransmissor", 3, "ciência"),
                    Pergunta("Qual é o nome da teoria que descreve a evolução das espécies por meio da seleção natural?", "Proposta por Charles Darwin", "Darwinismo", 3, "ciência"),
                    Pergunta("O que é responsável pela transmissão de características genéticas?\na) Cromossomo\nb) Gênes\nc) DNA",
                            "Unidade da hereditariedade", "B", 3, "ciência")]

            perguntas_respostas = selecionar_perguntas(perguntas_respostas_sem_filtro)

            for vez in range(modo_player):
                def obter_resposta():
                    respostas_usuario.append(input("\nSua resposta: "))

                pontos = 0 # Zera os pontos
                acertos = 0 # Zera os acertos
                erros = 0 # Zera os erros

                if modo_player == 1:
                    print(f"Você tem {tempo_resposta} segundos para cada pergunta:\n")
                else:
                    print(f"PLAYER {vez + 1}\nVocê tem {tempo_resposta} segundos para cada pergunta:\n")

                for p in range(len(perguntas_respostas)):
                    print(perguntas_respostas[p].pergunta)

                    if modo_dica == 2:
                        print(f"Dica: {perguntas_respostas[p].dica}")

                    respostas_usuario.clear()  # limpa a lista de resposta

                    t = threading.Thread(target=obter_resposta)
                    t.start()
                    t.join(timeout=tempo_resposta)  # espera 10 segundo pra resposta

                    if respostas_usuario:
                        palpite = respostas_usuario[0].strip().lower()
                        if palpite == perguntas_respostas[p].resposta.lower():
                            erros = 0                    
                            if acertos < 2:
                                acertos += 1
                            pontos += 1
                            if modo_estudo == 2:
                                print("Correto!\n")
                            else:
                                print("Correto! Ganhou um ponto.\n")

                        elif palpite != perguntas_respostas[p].resposta.lower():
                            acertos = 0
                            if erros < 2:
                                erros += 1
                            if pontos > 0:
                                pontos -= 1
                            if modo_estudo == 2:
                                print(f"Incorreto! A resposta era {perguntas_respostas[p].resposta}.\n")
                            else:
                                print(f"Incorreto! Perdeu um ponto.\n")
                    else:
                        acertos = 0
                        if erros < 2:
                            erros += 1  
                        if modo_estudo == 2:
                            print(f"\nTempo esgotado! A resposta era {perguntas_respostas[p].resposta}.\n")
                        else:
                            print("\nTempo esgotado! Você não respondeu a tempo.\n")

                    if modo_dificuldade_adaptativa == 2 and acertos == 2 and modo_dificuldade < 3:
                        acertos = 0
                        modo_dificuldade += 1
                        perguntas_respostas = selecionar_perguntas(perguntas_respostas_sem_filtro)
                        print("\nDificuldade aumentada!\n")

                    if modo_dificuldade_adaptativa == 2 and erros == 2 and modo_dificuldade > 1:
                        erros = 0
                        modo_dificuldade -= 1
                        perguntas_respostas = selecionar_perguntas(perguntas_respostas_sem_filtro)
                        print("\nDificuldade diminuida!\n")

                    tempo_resposta = selecionar_dificuldade(modo_dificuldade)

                if modo_player == 1:
                    if modo_estudo != 2:
                        print(f"\nSua pontuação é {pontos}/{len(perguntas_respostas)}")
                else:
                    if modo_estudo != 2:
                        print(f"\nPontuação do player {vez + 1} : {pontos}/{len(perguntas_respostas)}\n")
            break
        except:
            print("Entrada inválida, por favor tente novamente.\n\n")
if __name__ == "__main__":
    respostas_usuario = []
    main()