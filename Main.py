#Biblioteca para utilizar a função encoding para utilização de caracteres especiais no ficheiro
import codecs

#Biblioteca para trabalhar com datas e horas
import datetime

#Função principal que vai ser chamada no menu no final do programa
def main(path):
    #Abertura do ficheiro, o bloco Try permite que o utilizador receba uma mensagem personalizada caso não seja possivel abrir o ficheiro
    try:
        file = open(f"{path}", 'r',encoding='utf-8')
    except:
        print("\nErro ao abrir o ficheiro, O programa vai terminar")
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

    #Atribui a string a variavel texto mas sem os caracteres especiais
    texto = remove_char(texto)

    #Função para converter a String sem os caracteres especiais em lista
    #A função strip() remove os espaços no inicio e fim da string
    def convert_list(text):

        for line in text:
            line = line.strip()
        lista = list(text.split())
        return lista

    #Cria uma lista de palavras separadas por espaço
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

    #Cria um novo dicionário com a contagem das palavras
    dicionario = get_words_count(lista_final)

    #Função para organizar o dicionário e fazer print ordenado
    def order_score(dic):
        '''ordenação do dicionário com função lambda em que a comparação é feita com o valor x[1]
        utilizamos o reverse=True para alterar a ordem do sorted()
        referencia para a função lambda. (https://docs.python.org/3/reference/expressions.html#lambda) 
        (https://towardsdatascience.com/two-simple-method-to-sort-a-python-dictionary-a7907c266dba)'''

        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        # Ciclo para percorrer o dicionario, mostra a palavras e o valor, das 20 mais utilizadas
        lugar = 1
        while lugar < 20:
            for i in dic[:20]:        
                print(lugar,"ª -",i[0], i[1])
                lugar += 1    


    #Função para gravar um ficheiro com o resultado das ocorrências
    def save_text(dic):

        date = datetime.date.today()
        new_text_file = f"Output\\ocorrencias_{str(date)}.txt"
        #Permite controlar se a execução foi realizada com sucesso ou não, caso não seja possivel abrir o ficheiro é devolvida uma mensagem
        try:
            new_file = open(f"{new_text_file}","w", encoding='utf-8')   
            dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
            lugar = 1

            #Percorre o dicionário de palavras e guarda no ficheiro por ordem
            while lugar < 20:
                for i in dic:
                    #Variavel para guardar no ficheiro a string com toda a informação que precisamos, lugar, palavra e nº de ocorrência
                    texto = str(lugar)+ " ª - " + str(i[0]) + "-" + str(i[1]) + "\n"
                    new_file.writelines(texto)
                    lugar += 1
            new_file.close()
            print("\nFicheiro Guardado com exito. Verifique a lista completa em {}\n".format(new_text_file))
        except:
            print("\nErro ao Gravar o ficheiro, o programa vai terminar.")
            exit()
        

    #Execução das funções do programa
    save_text(dicionario)
    order_score(dicionario)  

print("***********************************")
print("* Trabalho 1 Programação Avançada *")
print("* Nome: Nuno Cunha                *")
print("* Número: 20202457                *")
print("* Turma: G.S.C                    *")
print("***********************************")
print("\n")

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

while True:    

    if option == '1':
        path = "Livros\pg34719.txt"
        main(path)
        break
    elif option == '2':
        path = "Livros\pg54829.txt"
        main(path)
        break
    elif option == '3':
        path = "Livros\pg1661-0.txt"
        main(path)
        #Função que para a execução do programa
        break
    elif option == '4':
        path = "Livros\pg4078.txt"
        main(path)
        break
    elif option == '5':
        path = input("\nIntroduza o caminho e o nome do ficheiro (exemplo: c:\\teste.txt):\n")
        main(path)
        break
    elif option == '6':
        print("\nAté Breve")
        #Função que termina a execução do programa
        exit()        
    else:
        print("\nOpção inválida!") 
        option = input(("Escolha outra opção: "))