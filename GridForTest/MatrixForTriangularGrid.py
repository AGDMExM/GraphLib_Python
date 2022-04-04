import random
from typing import List


def get_matrix_for_triangular_grid(sizeTriangularMatrix, weightedGraph=False):
    """

    :param weightedGraph:
    :param sizeTriangularMatrix:
    :return: Return new matrix - adjacency matrix List[List[int]] for triangular grid
    """
    resultMatrix: List[List[int]] = list()

    for idVertex in range(0, sizeTriangularMatrix * sizeTriangularMatrix):
        lst = list()
        for j in range(0, sizeTriangularMatrix * sizeTriangularMatrix):
            lst.append(0)
        resultMatrix.append(lst)

    if weightedGraph:
        for idVertex in range(0, sizeTriangularMatrix * sizeTriangularMatrix - 1):
            r = int(idVertex / sizeTriangularMatrix)
            c = idVertex % sizeTriangularMatrix

            if c < sizeTriangularMatrix - 1:
                value = random.randrange(1, 10)
                resultMatrix[idVertex][idVertex + 1] = value
                resultMatrix[idVertex + 1][idVertex] = value

            if r < sizeTriangularMatrix - 1:
                value = random.randrange(1, 10)
                resultMatrix[idVertex][idVertex + sizeTriangularMatrix] = value
                resultMatrix[idVertex + sizeTriangularMatrix][idVertex] = value

                if (r % 2 == 0 and c % 2 == 0) or (r % 2 == 1 and c % 2 == 1):
                    if c > 0:
                        value = random.randrange(1, 10)
                        resultMatrix[idVertex][idVertex + sizeTriangularMatrix - 1] = value
                        resultMatrix[idVertex + sizeTriangularMatrix - 1][idVertex] = value
                    if c < sizeTriangularMatrix - 1:
                        value = random.randrange(1, 10)
                        resultMatrix[idVertex][idVertex + sizeTriangularMatrix + 1] = value
                        resultMatrix[idVertex + sizeTriangularMatrix + 1][idVertex] = value

    if not weightedGraph:
        for idVertex in range(0, sizeTriangularMatrix * sizeTriangularMatrix - 1):
            r = int(idVertex / sizeTriangularMatrix)
            c = idVertex % sizeTriangularMatrix

            if c < sizeTriangularMatrix - 1:
                resultMatrix[idVertex][idVertex + 1] = 1
                resultMatrix[idVertex + 1][idVertex] = 1

            if r < sizeTriangularMatrix - 1:
                resultMatrix[idVertex][idVertex + sizeTriangularMatrix] = 1
                resultMatrix[idVertex + sizeTriangularMatrix][idVertex] = 1

                if (r % 2 == 0 and c % 2 == 0) or (r % 2 == 1 and c % 2 == 1):
                    if c > 0:
                        resultMatrix[idVertex][idVertex + sizeTriangularMatrix - 1] = 1
                        resultMatrix[idVertex + sizeTriangularMatrix - 1][idVertex] = 1
                    if c < sizeTriangularMatrix - 1:
                        resultMatrix[idVertex][idVertex + sizeTriangularMatrix + 1] = 1
                        resultMatrix[idVertex + sizeTriangularMatrix + 1][idVertex] = 1

    return resultMatrix
