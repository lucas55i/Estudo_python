import requests


print("###################")
print("## Consulta CEP ##")
print("###################")
print()


cep_input = input('Digite o CEP para a consulta: ')

if len(cep_input) != 8:
    print('Quantidade de digitos Invalida!')
    exit()


requests = requests.get('https://viacep.com.br/ws/{}/json/' .format(cep_input))


address_data =requests.json()

if 'erro' not in address_data:
    print('==> CEP ENCONTRADO <==')

    print('CEP: {}'.format(address_data))
else:
    print('CEP invalido')