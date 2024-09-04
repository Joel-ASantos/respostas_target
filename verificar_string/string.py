var_a = 0
texto = input('digite um texto aqui: ')
for i in texto:
    for char in i:
        if char.isupper():
            char = char.islower()
            var_a+=1
        if char == 'a':
            var_a+=1
print('Ocorrencias de a: ',var_a)