# programa que retorna frase de acordo com ano de nascimento
def ano(year):
    from datetime import date
    atual = date.today().year
    x2 = atual - year
    print(f'Idade: {x2} anos.')
    if x2 < 16:
        print('NÃO VOTA!')
    elif 16 <= x2 < 18 or x2 > 65:
        print('VOTO OPCIONAL')
    else:
        print('VOTO OBRIGATÓRIO!')
    print('FIM!')


# programa principal
ano(int(input('Digite seu ano de nascimento:')))