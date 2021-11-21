'''
O objetivo deste trabalho é desenvolver um programa em Python 3 que apresente dados estatísticos de número de ocorrência de palavras para um dado texto proveniente de um ficheiro.
O texto pode ser um livro e, a partir deste programa, poderia ser analisado de acordo com a ocorrência de palavras (por exemplo, gerar nuvem de palavras, calcular a similaridade de textos,
classificar a autoria de uma parte de texto, ...).
Para testar, utilize livros no formato txt.
Alguns exemplares podem ser baixados gratuitamente do Projeto Gutenberg: https://www.gutenberg.org/ebooks/.

'''

#TODO:1) O programa deve obter texto de um ficheiro;
    #TODO:1.1 O nome do ficheiro deve ser dado pelo usuário.
#TODO:2) O programa deve separar as palavras de modo a remover elementos de pontuação (pontos, vírgulas, exclamações, interrogações, travessões, ...);
    #TODO:2.1 A separação das palavras não deve ser case-sensitive (exemplo: 'casa' e 'Casa' devem ser tratadas como iguais).
    #TODO:2.2 Não há necessidade de separar radicais ou remover prefixos ou sufixos das palavras (exemplo: 'casa' e 'casas' pode ser consideradas como palavras diferentes).
    #Algumas facilidades podem ser assumidas, desde que devidamente indicadas por comentário no código ou alguma outra documentação do trabalho. Por exemplo, o(a) aluno(a) pode manter o texto de identificação do projeto no início e fim do ficheiro, mesmo que este texto não faça parte do texto do autor (assume-se, a princípio, que isto não trará graves problemas para a contagem de palavras de modo geral).
#TODO:3) Como saída do programa, deve ser gerado um novo ficheiro contendo cada palavra e seu respectivo número de ocorrências (ou percentual de ocorrência).
#TODO:4) Uma outra saída esperada do programa é a apresentação (print no console) das 20 palavras mais utilizadas no texto.
#TODO:5) As partes importantes do código devem ser comentadas (descrever o que está sendo feito).
#TODO:6) O programa deve ser organizado em módulos (funções e procedimentos).

'''
Observações:

Haverá um decréscimo na nota (20%) para cada dia ou fração de atraso.
Alguns exemplares de livros em Português:
https://www.gutenberg.org/cache/epub/34719/pg34719.txt
https://www.gutenberg.org/files/62624/62624-0.txt
https://www.gutenberg.org/cache/epub/24401/pg24401.txt
https://www.gutenberg.org/cache/epub/54829/pg54829.txt
Alguns exemplares de livros em Inglês:
https://www.gutenberg.org/files/11/11-0.txt
https://www.gutenberg.org/files/1661/1661-0.txt
https://www.gutenberg.org/cache/epub/4078/pg4078.txt

'''
#import para utilizar a função encoding para utilização de caracteres especiais
import codecs

#TODO: 1.1
path = input("\nIntroduza o caminho e o nome do ficheiro (exemplo: c:\\teste.txt):\n")
path = 'text.txt'

# o encoding permite ler texto com caracteres especiais
file = open(f"{path}", 'r',encoding='utf-8')

#TODO: 1
#leitura do ficheiro para uma lista
texto = file.read()

#Cria uma lista com caracteres
pont_list_chr=[]

def chr_list(begin, end):

    #lê um inteiro e converte em caracter, e adiciona á lista
    for i in range(begin, end):
        pont_list_chr.append(chr(i))

chr_list(33,48)
chr_list(58,65)
chr_list(91,97)
chr_list(123,127)

#função para remover todos os caracteres especiais
def remove_char(text):
    
    for char in pont_list_chr:
            text = text.replace(char, '')
    return text

texto = remove_char(texto)

def convert_list(text):

    for line in text:
        line = line.strip()
    lista = list(text.split())

    return lista

lista_final = convert_list(texto)

# print(lista_final)


def get_words_count(lista):
    dic = {}
    counter = 0
    for word in lista:
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1
    
    return dic

dicionario = get_words_count(lista_final)

# print(dicionario)

#TODO:4
#função para organizar o dicionário e faz print
def order_score(dic):

    '''ordenação do dicionário com função lambda em que a comparação é feita com o valor x[1]
    utilizamos o reverse=True para alterar a ordem do sorted(),
    esta foi a unica forma que encontrei para fazer o sort do dicionário
    referencia para a função lambda. (https://towardsdatascience.com/two-simple-method-to-sort-a-python-dictionary-a7907c266dba)'''
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    # ciclo para percorrer o dicionario, mostra a palavras e o valor, das 20 mais utilizadas
    for i in dic[:20]:
	    print(i[0], i[1])

         


def save_text(dic):

    new_file = open("newTextFile.txt","w")   

    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    # ciclo para percorrer o dicionario, mostra a palavras e o valor, das 20 mais utilizadas
    for i in dic[:20]:
	    new_file.write(i[0], i[1])

    # new_file.write(text) 


save_text(dicionario)
order_score(dicionario)  

#Fecha a ligação ao ficheiro
file.close()

