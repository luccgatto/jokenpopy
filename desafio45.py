import random

jokenpo = random.choice(['Pedra', 'Papel', 'Tesoura'])

escolha = str(input('Digite se você escolhe Pedra, Papel, ou Tesoura: '))
escolha2 = escolha.capitalize()

if escolha2 == 'Pedra' and jokenpo == 'Papel':
    print(f'O computador escolheu {jokenpo}, e você escolheu {escolha}. Você perdeu!')
elif escolha2 == 'Pedra' and jokenpo == 'Tesoura':
    print(f'O computador escolheu {jokenpo}, e você escolheu {escolha}. Você ganhou!')
elif escolha2 == 'Papel' and jokenpo == 'Tesoura':
    print(f'O computador escolheu {jokenpo} e você escolheu {escolha}. Você perdeu!')
elif escolha2 == 'Papel' and jokenpo == 'Pedra':
    print(f'O computador escolheu {jokenpo} e você escolheu {escolha}. Você ganhou!')
elif escolha2 == 'Tesoura' and jokenpo == 'Pedra':
    print(f'O computador escolheu {jokenpo} e você escolheu {escolha}. Você perdeu!')
elif escolha2 == 'Tesoura' and jokenpo == 'Papel':
    print(f'O computador escolheu {jokenpo} e você escolheu {escolha}. Você ganhou!')
else:
    print(f'O computador escolheu {jokenpo} e você escolheu {escolha}. Empate!')