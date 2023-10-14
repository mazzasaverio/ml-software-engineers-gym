"""
Problem Statement:

Certain applications require arbitrary precision arithmetic. One way to achieve this
is to use arrays to represent integers. Each array entry represents a digit, with the
most significant digit appearing first. A negative leading digit denotes a negative integer.

For example, the sequence [1, 9, 3, 7, 0, 7, 7, 2, 1] represents the number 193707721, and
the sequence [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7] represents the number -761838257287.

The task is to write a program that takes two arrays representing integers and returns
an integer representing their product.

Example:
    If the inputs are [1, 9, 3, 7, 0, 7, 7, 2, 1] and [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7],
    your function should return [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7],
    since 193707721 * -761838257287 = -147573952589676412927.

"""


# CREARE UNA STRUTTURA DELLA REPO CON PROBLEMI E DOMANDE
# RICERCA PACCHETTO O DECORATORE CHE MI DA INDICAZIONE SULLA COMPLESSITA DELLA FUNZIONE
def solution(A, B):
    result = []

    len_iter = min(len(A), len(B))
    report = 0

    for i in range(1, len_iter):
        prod_pos = A[-i] * B[-i]

        units = int(str(prod_pos)[-1])

        temp_result = units + report
        if temp_result > 9:
            report = int(str(temp_result)[:-1])
            units = temp_result[-1]
        else:
            report = 0

        result.extend(temp_result)

    final_result = [int(i) for i in str(report)]
    result = result.reverse()

    final_result.extend(result)
    return final_result
