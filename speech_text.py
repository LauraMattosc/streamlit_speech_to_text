import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import words

# Download the words corpus if necessary
nltk.download('words')

# Get a set of English words from the corpus
english_words = set(words.words())

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')
        print("Você disse: " + frase)
        
        # Lista de palavras a serem verificadas
        palavras = ["sereia", "árvore", "gato"]

        # Cria uma lista com as palavras reconhecidas
        palavras_reconhecidas = frase.split()

        # Inicia as variáveis de contagem
        acertos = 0
        erros = 0

        # Verifica cada palavra reconhecida
        for palavra in palavras_reconhecidas:
            # Se a palavra estiver na lista de palavras corretas, conta como acerto
            if palavra in palavras:
                acertos += 1
                print(palavra, "- correta")
            # Se não estiver na lista, conta como erro
            else:
                erros += 1
                print(palavra, "- incorreta")

        # Exibe a mensagem de resultado
        if erros > 0:
            print("Você acertou", acertos, "palavra(s) e errou", erros, "palavra(s)")
        else:
            print("Parabéns, você acertou todas as palavras!")
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
    except sr.RequestError as e:
        print("Não foi possível completar a requisição; {0}".format(e))

ouvir_microfone()
