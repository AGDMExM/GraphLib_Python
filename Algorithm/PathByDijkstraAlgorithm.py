import queue

from GraphLib_Python.Model.MatrixModel import MatrixModel


def get_path_by_dijkstra_algorithm(matrixModel, A, B):
    """

    :param matrixModel:
    :param A: From Edge
    :param B: To Edge
    :return: Return list(0 - dst, 1 - path) distance between start and end edges and list of names in path
    """
    matrixModel: MatrixModel

    distanceToEdges = list()
    for i in range(0, len(matrixModel.matrix)):
        distanceToEdges.append(999999)
    pathsForEdges = list()
    for i in range(0, len(matrixModel.matrix)):
        pathsForEdges.append(list())

    distanceToEdges[matrixModel.namesVertex.index(A)] = 0  # Distance to start edge == 0

    q = queue.Queue()
    q.put(matrixModel.namesVertex.index(A))
    while not q.empty():
        i = q.get()
        for idNeighbor in range(0, len(matrixModel.matrix)):
            if matrixModel.matrix[i][idNeighbor] == 0:
                continue

            if distanceToEdges[i] + matrixModel.matrix[i][idNeighbor] < distanceToEdges[idNeighbor]:
                distanceToEdges[idNeighbor] = distanceToEdges[i] + matrixModel.matrix[i][idNeighbor]
                pathsForEdges[idNeighbor].clear()
                for name in pathsForEdges[i]:
                    pathsForEdges[idNeighbor].append(name)
                pathsForEdges[idNeighbor].append(matrixModel.namesVertex[idNeighbor])

                q.put(idNeighbor)

    return [distanceToEdges[matrixModel.namesVertex.index(B)], pathsForEdges[matrixModel.namesVertex.index(B)]]
