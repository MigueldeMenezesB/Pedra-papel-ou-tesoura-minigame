# Jogo Pedra, Papel ou Tesoura

from random import choice # Desta maneira, ele importa do módulo random apenas a função choice

vitoriaJog = 0
vitoriaMaq = 0

def escolhaJogador():
  escolha = input('\nDigite pedra, papel ou tesoura: ')
  escolha.lower()
  if escolha == 'pedra':
    return escolha
  elif escolha == 'papel':
    return escolha
  elif escolha == 'tesoura':
    return escolha
  else:
    return 'Opção Inválida! Tente novamente.'
    escolhaJogador() #Desta maneira, ele repete a execução da função, caso não entre em nenhuma condição!


def escolhaMaquina():
  escolhaMaquina = choice(['pedra', 'papel', 'tesoura'])
  return escolhaMaquina


while True:

  escolha = escolhaJogador() # Desta forma, ele armazena na variável 'escolha' o valor gerado pela função escolhaJogador()
  escolhaMaq = escolhaMaquina()

  if (escolha == 'pedra') and (escolhaMaq == 'tesoura') \
    or (escolha == 'papel') and (escolhaMaq == 'pedra') \
      or (escolha == 'tesoura') and (escolhaMaq == 'papel'):
      print(f'Jogador escolheu {escolha} e a máquina escolheu {escolhaMaq}. Você venceu!')
      vitoriaJog += 1
  
  if escolha == escolhaMaq:
    print(f'Jogador escolheu {escolha} e a máquina escolheu {escolhaMaq}. Empatou!')
  else:
    print(f'Jogador escolheu {escolha} e a máquina escolheu {escolhaMaq}. Você perdeu!')
    vitoriaMaq += 1

          
  print(f'\nSua pontuação: {vitoriaJog}')
  print(f'Pontuação Máquina: {vitoriaMaq}')

  exec = input('\ncontinuar?[S/N]: ')
  if exec in ['Ss']:
    pass
  elif exec in ['Nn']:
    break
  else:
    break
