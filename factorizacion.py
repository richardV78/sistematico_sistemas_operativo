def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# ejemplo de uso 
numero_terminos = 10 
print("serie de fibonacci: ")
for i in range(numero_terminos):
    print (fibonacci(i))