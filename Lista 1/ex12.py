s = []
f = []
n = []

letra = input()
objetos = input()


if letra == 's':
    s = objetos.split()
    print(s)
elif letra == 'f':
    f = list(map(int, objetos.split()))
    print(f)
elif letra == 'n':
    n = list(map(float, objetos.split()))
    print(n)

