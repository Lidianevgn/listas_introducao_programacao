#crie um jogo da forca informando ao usuário alguns temas(no máximo 5)
#Dentro desses temas devem constar as palavras que farão parte do jogo
#A cada letra errada o programa deve armazenar essa letra, caso o usuário jogue ela novamente não poderá ser usada.
#A cada letra errada o programa "printa" uma parte do corpo até que o usuário erre ou acerte todas as letras da palavra.

print(""" ------------------------------------------------------------------------------------------------------------------------
      **   *******     ********    *******     *******       **       ********   *******   *******     ******      **    
     /**  **/////**   **//////**  **/////**   /**////**     ****     /**/////   **/////** /**////**   **////**    ****   
     /** **     //** **      //  **     //**  /**    /**   **//**    /**       **     //**/**   /**  **    //    **//**  
     /**/**      /**/**         /**      /**  /**    /**  **  //**   /******* /**      /**/*******  /**         **  //** 
     /**/**      /**/**    *****/**      /**  /**    /** **********  /**////  /**      /**/**///**  /**        **********
 **  /**//**     ** //**  ////**//**     **   /**    ** /**//////**  /**      //**     ** /**  //** //**    **/**//////**
//*****  //*******   //********  //*******    /*******  /**     /**  /**       //*******  /**   //** //****** /**     /**
 /////    ///////     ////////    ///////     ///////   //      //   //         ///////   //     //   //////  //      // """)
print("""Bem vindo ao Jogo da Forca!
Você tem o objetivo de acertar a palavra escondida.
Tente uma letra por vez!
Acertando, ela será encaixada na sua palavra!
Errando, você perde uma chance e corre o risco de ser enforcado!
Cuidado, você tem no máximo 6 chances para errar.
As palavras estão entre três tema: cores, circo e tecnologia
Boa Diversão!!!""")

import random
import string

temas = {
    'cores':['azul', 'laranja', 'fucsia', 'anil', 'roial', 'ambar',],
    'circo':['malabarismo', 'palhaço', 'picadeiro', 'pipoca'],
    'tecnologia':['python', 'algoritmo', 'internet', 'celular', 'computador']
}
tema = random.choice(list(temas.keys()))
palavra = random.choice(temas[tema])
letras_erradas = []
letras_certas = []
max_tentativas = 6
while True:
    palavra_secreta = ''
    for letra in palavra:
        if letra in letras_certas:
            palavra_secreta += letra
        else:
            palavra_secreta += '_'
    print(palavra_secreta)
    if letras_erradas:
        print('Letras erradas: ' + ' '.join(letras_erradas))
    letra = input('Digite uma letra: ').lower()
    if letra in letras_erradas or letra in letras_certas:
        print('Você já jogou essa letra antes. Tente outra.')
        continue
    if letra in palavra:
        letras_certas.append(letra)
        print('Parabéns, você acertou uma letra!')
    else:
        letras_erradas.append(letra)
        print('Que pena, essa letra não está na palavra.')
        if len(letras_erradas) == 1:
            print('  O  ')
        elif len(letras_erradas) == 2:
            print('  O  ')
            print('  |  ')
        elif len(letras_erradas) == 3:
            print('  O  ')
            print(' \|  ')
            print('  |  ')
        elif len(letras_erradas) == 4:
            print('  O  ')
            print(' \|/ ')
            print('  |  ')
        elif len(letras_erradas) == 5:
            print('  O  ')
            print(' \|/ ')
            print('  |  ')
            print(' /   ')
        elif len(letras_erradas) == 6:
            print('  O  ')
            print(' \|/ ')
            print('  |  ')
            print(' / \ ')
            print('/   \\')
            print('Eita! Peerrrrrdeeeeuuuuu! Você foi enforcado! A palavra era "{}".'.format(palavra))
            break
    if all(letra in letras_certas for letra in palavra):
        print('Você é fera mesmo! Parabéns, você acertou a palavra "{}"!'.format(palavra))
        break
    if len(letras_erradas) == max_tentativas:
        print('Ixi!Você atingiu o limite máximo de tentativas. A palavra era "{}".'.format(palavra))
        break



