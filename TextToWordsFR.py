file = open("dicofr.txt", 'r')
file = file.read()
file = file.replace(' ', '')
file = file.split(',')
liste = []
special = ['Ãª']
var = 1224

print(file)


def clean(file):
    for i in range(var):
        if file[i].isalpha() == False:
            del file[i]

    print(file)
    print(len(file))

    for i in range(var):
        for j in range(len(special)):
            if special[j] in file[i]:
                del file[i]

    print(file)
    print(len(file))


for i in range(3):
    clean(file)

for word in file:
    if word[0] == 's' and word[1] == 'e':
        print(word)
