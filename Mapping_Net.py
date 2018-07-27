import csv

lista_mac = []
lista_ip = []
conteudo = []

with open('MAC.csv','r', newline='\n', encoding='utf-8') as csvmac:  # OPEN FILE WITH MAC ADDRESS
    reader = csv.reader(csvmac, delimiter=',')
    for x in reader:
        lista_mac.append(x)

with open('IP.csv','r',newline='\n',encoding='utf-16') as csvip:    # OPEN FILE WITH IP ADDRESS
    readerr = csv.reader(csvip, delimiter=',')                   # OBS: UTF-16 ENCONDIG NECESSARY WHEN PYTHON DON´T
                                                                    # RECOGNIZE THE FILE AS A LIST TYPE. USE ENCONDIG ON
    for i in readerr:                                            # A LIST RECOGNIZED FILE WILL GENERATE AN ERROR
        lista_ip.append(i)                                          # TO CHECK THIS USE "type(variable)"

print("PASSED HERE")

# OPEN FILE TO INSERT THE RESULT OF MATCH

printer = open('RESULT.csv',"w")


# MATCH MAC ADDRESS ON IP.CSV FILE AND MAC.CSV AND INSERT STRUCTURED DATA ON A NEW LIST
print("PASSED HERE TOO")


for x in range(0,lista_ip.__len__()):    # RUN A LOOP WITH THE LENGTH OF lista_ip

    for z in range(0,lista_mac.__len__()):  # RUN A LOOP WITH THE LENGTH OF lista_MAC

        if lista_ip[x][1] == lista_mac[z][1]:   # COMPARE THE COLUMN 1 ( SECOND ELEMENT ) AT EACH LIST,
                                                # THAT SHOULD HAVE THE MAC ADDRESS

            conteudo.append([lista_ip[x][0], lista_mac[x][1],lista_mac[x][0]])   # ADD MATCH VALUES ON A NEW LIST

print()
for item in conteudo:
    printer.write("%s\n" % item)


# FOR CLOSE THE OPENS FILES
csvmac.close()
csvip.close()
printer.close()

# END PROGRAM