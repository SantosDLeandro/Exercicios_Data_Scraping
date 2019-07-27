import requests

url = 'http://educacao.dadosabertosbr.com/api/escolas/buscaavancada?'
situação = 'situacaoFuncionamento=1&estado=pe&cidade=2606408'
data = requests.get(url + situação).json()
print ('Primeiras 100 escolas:')
for escola in data[1]:
  print (f'{escola["nome"]}')
print ('Escolas em funcionamento na Cidade de Gravtá')
print (data[0])
