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
#Biblioteca para utilizar a função encoding para utilização de caracteres especiais no ficheiro
import codecs

print("***********************************")
print("* Trabalho 1 Programação Avançada *")
print("* Nome: Nuno Cunha                *")
print("* Número: 20202457                *")
print("* Turma: G.S.C                    *")
print("***********************************")
print("\n\n")

print("****************************************************************")
print("* 1 - Noites de Cintra, by Alberto Pimentel                    *")
print("* 2 - Postumas de Braz Cubas, by Machado de Assis              *")
print("* 3 - The Adventures of Sherlock Holmes, by Arthur Conan Doyle *")
print("* 4 - The Picture of Dorian Gray, by Oscar Wilde               *")
print("* 5 - Introduzir Caminho                                       *")
print("* 6 - Sair                                                     *")
print("****************************************************************")

#Recebe a opção do utilizador
option = input(("\n\nEscolha uma das opções: "))

if option == '1':
    path = "Livros\pg34719.txt"
elif option == '2':
    path = "Livros\pg54829.txt"
elif option == '3':
    path = "Livros\pg1661-0.txt"
elif option == '4':
    path = "Livros\pg4078.txt"
elif option == '5':
    path = input("\nIntroduza o caminho e o nome do ficheiro (exemplo: c:\\teste.txt):\n")
elif option == '6':
    print("\nAté Breve")
    #Função que para a execução do programa
    exit()        
else:
    print("\nOpção inválida! O programa vai terminar")
    exit()

# O encoding permite ler texto com caracteres especiais
try:
    file = open(f"{path}", 'r',encoding='utf-8')
except:
    print("\nErro ao abrir o ficheiro. Oprograma vai terminar")
    exit()

#leitura do ficheiro para uma lista
texto = file.read().lower()

#Fecha a ligação ao ficheiro
file.close()

#Cria uma lista com caracteres
pont_list_chr=[]

def chr_list(begin, end):
    #lê um inteiro e converte em caracter, e adiciona á lista
    for i in range(begin, end):
        pont_list_chr.append(chr(i))

#Range de caracteres na tabela ASCII
chr_list(33,48)
chr_list(58,65)
chr_list(91,97)
chr_list(123,127)

#Função para remover todos os caracteres especiais
def remove_char(text):    
    for char in pont_list_chr:
            text = text.replace(char, '')
    return text

texto = remove_char(texto)

#Função para converter a String sem os caracteres especiais em lista
def convert_list(text):
    for line in text:
        line = line.strip()
    lista = list(text.split())

    return lista

lista_final = convert_list(texto)

#Função para criar um dicionario com os pares de palavras e a sua ocorrencia no texto lido
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

#Função para organizar o dicionário e fazer print ordenado
def order_score(dic):
    '''ordenação do dicionário com função lambda em que a comparação é feita com o valor x[1]
    utilizamos o reverse=True para alterar a ordem do sorted()
    referencia para a função lambda. (https://towardsdatascience.com/two-simple-method-to-sort-a-python-dictionary-a7907c266dba)'''
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    # Ciclo para percorrer o dicionario, mostra a palavras e o valor, das 20 mais utilizadas
    for i in dic[:20]:
	    print(i[0], i[1])
         
#Função para gravar um ficheiro com o resultado das ocorrências
def save_text(dic):
    new_text_file = "Output\\ocorrencias.txt"
    #TODO:validar se o ficheiro já existe
    #Método que permite controlar se a execução foi realizada com sucesso ou não, caso não seja possivel abrir o ficheiro é devolvida uma mensagem
    try:
        new_file = open(f"{new_text_file}","w", encoding='utf-8')   
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        for i in dic:
            texto = str(i[0]) + "-" + str(i[1]) + "\n"
            new_file.writelines(texto)
        new_file.close()
        print("\nFicheiro Guardado com exito. Verifique a lista completa em {}".format(new_text_file))
    except:
        print("\nErro ao Gravar o ficheiro")
        exit()
    

#Execução das funções do programa
save_text(dicionario)
order_score(dicionario)  