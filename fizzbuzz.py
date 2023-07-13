"""
Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:
    Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
    Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
    Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.
"""

p = 0
list = []
for numero in range(1, 101):
    list.append(numero)
    if list[p] % 3 == 0:
        if list[p] % 3 == 0 and list[p] % 5 == 0:
            list[p] = "fizzbuzz"
        else:
            list[p] = "fizz"
    elif list[p] % 5 == 0:
        if list[p] % 5 == 0 and list[p] % 3 == 0:
            list[p] = "fizzbuzz"
        else:
            list[p] = "buzz"
    p += 1
