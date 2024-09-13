
qtd_time = int(input('Informe a quantdade de times: '))
qtd_jogadores = int(input('Informe a quantdade de jogadores: '))

for t in range (1, qtd_time + 1):
    print(f'time{t}')
    

for j in range (1, qtd_jogadores + 1):
    if j%3 ==0:
        print(f'{j}-BET ', end="")
    else:
        print(f'{j} ', end="")

