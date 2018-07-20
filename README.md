# mapping-network
this script connect information gathered on arp table and a switch mac-address table, and create a ".csv" file to organize the data.


# INSTRUCTIONS
At first, is necessary to create 3 .csv file on a directory that will take the script.py

# COPY THE NAME BELLOW 
IP.csv
MAC.csv
RESULT.csv

# Fill the files
IP.csv need to receive the arp table
MAC.csv need to receive the switch mac-address table
RESULT.csv will be filled by the script

# Working
the script only support two column and the order have to be interface Number,Mac-address like example:

MAC.csv
g1/0/1,xxxx-xxxx-xxxx

IP.csv
a.b.c.d,xxx-xxx-xxxx
