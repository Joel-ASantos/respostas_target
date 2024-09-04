var_a = 0
texto = input('digite um texto aqui: ')
for i in texto:
    for char in i:
        if char == 'a' or char == 'A':
            var_a+=1
print('Ocorrencias de a: ',var_a)