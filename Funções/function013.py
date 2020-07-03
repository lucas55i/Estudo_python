def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade >= 18:
        return (f'Com {idade} anos: Voto é Obrigatório')
    elif idade >= 65:
        return (f'Com {idade} anos: Voto não é obrigatório')
    elif idade >= 16:
        return (f'Com {idade} anos: Voto Opcional')
    elif idade > 16:
        return (f'Com {idade} anos: Voce não pode votar')




ano = int(input('Em qual ano tu nasceu: '))
print(voto(ano))

# anos que nasceu  menos anos atual igual a sua idade
