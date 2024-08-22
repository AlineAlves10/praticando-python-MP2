def my_isdigit(s):
    for i in s:
        if i < '0' or i > '9':
            return False
    
    return True

digitos = input()

resultado = my_isdigit(digitos)
print(resultado)