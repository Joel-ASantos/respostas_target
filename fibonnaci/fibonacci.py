#Expressão de Fibonacci: Fn = fn-1 + fn-2
def fibonacci(n):
    if n < 0:
        return False
    
    fibo = [0,1]
    while fibo[-1] < n:
        fibo.append(fibo[-1]+fibo[-2])
    
    if n in fibo:
       print(f'{n} pertence a fibonacci')
    else:
        print(f'{n} não pertence a fibonacci')
    return fibo
n = int(input('digite um numero pra gerar a sequencia de fibonacci: '))
sequencia = fibonacci(n)
print('sequencia de fibonacci: ',sequencia)