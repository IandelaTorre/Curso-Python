from typing import Dict, List, Tuple


# Escribe una funcion que regrese el valor de fibonacci en la posicion nth
def fibonacci(n: int) -> int:
    if n < 0:
        print("entrada invalida")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)
    pass


# Escribe una funcion que verifique si una cadena es anagrama de otra
def is_anagram(str1: str, str2: str) -> bool:
    #escribe aqui tu codigo 
    pass

# Escribe una funcion que regrese los numeros impares entre 0-100
def first_100_odd_numbers() -> List[int]:
    numerosimpares = []
    for i in range(0,100):
        if i % 2 != 0:
            numerosimpares.append(i)
    return numerosimpares
    pass


# Escribe una funcion que convierta un numero decimal a binario
def decimal_to_binary(n: int) -> str:
    numerodecimal = n
    binario = bin(numerodecimal)
    return str(binario[2::])

    pass


# Escribe una funcion que recibe una lista de enteros y un valor n, que regrese
# el indice de los dos numeros que suman dicho valor n
def two_sum(numbers: List[int], target: int) -> List[int]:
    suma = {}
    for index, valor in enumerate(numbers):
        numero_restante = target - valor
        if numero_restante in suma:
            return [suma[numero_restante], index]  
        suma[valor] = index
    return -1


    pass


# Escribe una funcion que regrese el numero mayor y menor de un diccionario
# {"key1": 3, "key2": -1, "key1": 20, "key1": 4} min=-1 max=20
# (min, max)
def max_and_min_value_in_dict(values: Dict) -> Tuple[int, int]:
    max = 0
    min = 0
    for i in values:
        if values[i] > max:
            max = values[i]
        if values[i] < min:
            min = values[i]
    return min, max
    pass

# Escribe una funcion que ordene numeros
def sort_numbers(nums: List[int]) -> List[int]:
    longitud = len(nums)

    for i in range(longitud):
        for j in range(0, longitud-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
    pass
