import csv
from typing import TextIO

printer = open('RESULT.csv',"r")
conteudo = []
lista_ip = []
lista_mac = []
with open('IP.csv', newline='\n') as csvfile1:
    # o nome 'spamreader' abaixo é só exemplo, poderia ser qq. coisa
    spamreader = csv.reader(csvfile1, delimiter=',') # separe por vírgula

    # o módulo csv detectará novas linhas automaticamente
    for linha in spamreader:
        lista_ip.append(linha)
with open('MAC.csv', newline='\n') as csvfile2:
    # o nome 'spamreader' abaixo é só exemplo, poderia ser qq. coisa
    spamreader = csv.reader(csvfile2, delimiter=',') # separe por vírgula

    # o módulo csv detectará novas linhas automaticamente
    for linha in spamreader:
        lista_mac.append(linha)

for x in range(0,lista_ip.__len__()):
    for y in range(0,lista_ip.__len__()):
        if lista_ip[x][1] == lista_mac[y][1]:

            conteudo.append([lista_ip[x][0], ";", lista_mac[x][1], ";", lista_mac[x][0]])


printer = open('RESULT.csv',"w")

for item in conteudo:
  printer.write("%s\n" % item)


csvfile1.close()
csvfile2.close()
printer.close()
# insira seu conteúdo
# obs: o método append() é proveniente de uma lista
#conteudo.append('Nova linha')
#print(conteudo)
# Abre novamente o arquivo (escrita)
# e escreva o conteúdo criado anteriormente nele.
#arquivo = open('Oi.txt', 'w')
#arquivo.writelines(conteudo)
#arquivo.close()