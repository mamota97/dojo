"""
Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:
    Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
    Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
    Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.
"""

list = []
for item in range(0, 100):
    if item % 3 == 0:
        list.append("fizz")
        if item % 5 == 0:
            list.append("fizzbuzz")
    elif item % 5 == 0:
        list.append("buzz")
    else:
        list.append(item)

print(list)
