#!/usr/bin/python3

with open('find.txt','r') as find:
     for linha in find:
        goku = linha.split(' ')
        print(len(goku))

for i in range(len(goku)):
    print(goku[i][0].upper(), end="")

#RESULT
#WELLSPACEDONESPACETHESPACEFLAGSPACEISSPACECTFSPACEOPENBRACKETSPACEZEROSEVENBSEVENZEROBFNINEFIVEEATWOBFIVEFIVEFFIVEFIVENINEONEBETWOCFIVENINEFIVEBBFIVETHREESEVENSPACECLOSEBRACKET
#
#WELL SPACE DONE SPACE THE SPACE FLAG SPACE IS SPACE CTF SPACE OPEN BRACKET SPACE ZERO SEVEN B SEVEN ZERO B F NINE FIVE E A TWO B FIVE FIVE F FIVE FIVE NINE ONE B E TWO C FIVE NINE FIVE B B FIVE THREE SEVE N SPACE CLOSE BRACKET
#CTF{07b70bf95ea2b55f5591be2c595bb537}
