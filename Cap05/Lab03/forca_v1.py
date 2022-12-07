# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman   :

    # Método Construtor
    def __init__(self, word: str):
        self.word = word
        self.correctChars = []
        self.wrongChars = []
        self.letters = '_' * len(word)

    # Método para adivinhar a letra

    def guess(self, letter: str):
        if len(letter) != 1:
            print('Insira apenasvuma letra!!')
        elif letter in self.correctChars or letter in self.wrongChars:
            print("Letra já adivinhada")
        elif letter in self.word:
            self.show_letter(letter)
            self.correctChars.append(letter)
        else:
            self.wrongChars.append(letter)
        self.print_game_status()

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return len(self.wrongChars) >= 6 or '_' not in self.letters

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        res = [bool(x in self.word) for x in self.correctChars]
        return len(self.correctChars) and all(res)

    # Método para não mostrar a letra no board
    def show_letter(self, letter: str):
        self.letters = ''.join(
            letter if self.word[x] == letter else self.letters[x] for x in range(len(self.word)))

    def print_game_status(self):
        boardVersion = len(self.wrongChars)
        print(board[boardVersion])
        print('\nPalavra: %s' % self.letters)
        print('\nLetras erradas: %s' % (' '.join(self.wrongChars)))
        print('\nLetras corretas: %s' % (' '.join(self.correctChars)))


# Função para ler uma palavra de forma aleatória do banco de palavras


def rand_word():
    with open("./palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())
    print(game.word)

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        newLetter = input('\nInsira uma letra: ')
        game.guess(newLetter)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
