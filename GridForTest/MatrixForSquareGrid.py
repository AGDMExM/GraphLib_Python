import random
from typing import List


def get_matrix_for_square_grid(sizeSquareMatrix, weightedGraph=False):
    """

    :param weightedGraph:
    :param sizeSquareMatrix:
    :return: Return new matrix - adjacency matrix List[List[int]] for square grid
    """
    resultMatrix: List[List[int]] = list()

    for idVertex in range(0, sizeSquareMatrix * sizeSquareMatrix):
        lst = list()
        for j in range(0, sizeSquareMatrix * sizeSquareMatrix):
            lst.append(0)
        resultMatrix.append(lst)

    if weightedGraph:
        for idVertex in range(0, sizeSquareMatrix*sizeSquareMatrix - sizeSquareMatrix):
            r = idVertex / sizeSquareMatrix
            c = idVertex % sizeSquareMatrix
            if c < sizeSquareMatrix:
                value = random.randrange(0, 1000000)
                resultMatrix[idVertex][idVertex + 1] = value
                resultMatrix[idVertex + 1][idVertex] = value

            if r < sizeSquareMatrix:
                value = random.randrange(0, 1000000)
                resultMatrix[idVertex][idVertex + sizeSquareMatrix] = value
                resultMatrix[idVertex + sizeSquareMatrix][idVertex] = value

    if not weightedGraph:
        for idVertex in range(0, sizeSquareMatrix*sizeSquareMatrix - sizeSquareMatrix):
            r = idVertex / sizeSquareMatrix
            c = idVertex % sizeSquareMatrix
            if c < sizeSquareMatrix:
                resultMatrix[idVertex][idVertex + 1] = 1
                resultMatrix[idVertex + 1][idVertex] = 1

            if r < sizeSquareMatrix:
                resultMatrix[idVertex][idVertex + sizeSquareMatrix] = 1
                resultMatrix[idVertex + sizeSquareMatrix][idVertex] = 1

    return resultMatrix
