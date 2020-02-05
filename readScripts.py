import os

bender = open('characterTotals\\bender.txt', 'w', encoding='utf-8')
fry = open('characterTotals\\fry.txt', 'w', encoding='utf-8')
leela = open('characterTotals\\leela.txt', 'w', encoding='utf-8')
zoidberg = open('characterTotals\\zoidberg.txt', 'w', encoding='utf-8')

for file in os.listdir('episodes'):
    print(file)
    episode = open('episodes\\' + file, 'r', encoding='utf-8')
    for line in episode:
        if line.startswith("Bender:"):
            bender.write(line[7:])
        elif line.startswith("Fry:"):
            fry.write(line[4:])
        elif line.startswith("Leela:"):
            leela.write(line[6:])
        elif line.startswith("Zoidberg:"):
            zoidberg.write(line[9:])
    episode.close()
    
bender.close()
fry.close()
leela.close()
zoidberg.close()
