from typing import List


class MatrixModel:
    matrix: List[List[int]] = [[]]
    namesVertex: List[str] = list()

    def __init__(self, namesVertex, matrix):
        """
        :param namesVertex: namesVertex (list<string>)
        :param matrix: matrix (list<list<int>): contains int values, where 0 - no edge
        """
        self.matrix = matrix
        self.namesVertex = list(namesVertex)

    def _get_num_vertex_by_name(self, name):
        """Returns -1 if not found"""
        for name_ in self.namesVertex:
            if name_ == name:
                return self.namesVertex.index(name_)

        return -1

    def get_neighbors_vertex_by_name(self, name):
        """Returns list<string> - names neighbors"""
        res = list()
        idVertex = self._get_num_vertex_by_name(name)

        for i in range(0, len(self.matrix)):
            if self.matrix[idVertex][i] != 0:
                res.append(self.namesVertex[i])
            if self.matrix[i][idVertex] != 0:
                res.append(self.namesVertex[i])

        return res

    def path_exist(self, path):
        """
        Returns True - if path exist, False - if not
        :param path: path (list<string>): names vertex
        """
        for i in range(0, len(path) - 1):
            nameVertex = path[i]
            connVertex = list()  # list<string> - names neighbor

            for num in range(0, len(self.namesVertex)):
                if self.matrix[self.namesVertex.index(nameVertex)][num] != 0:
                    connVertex.append(self.namesVertex[num])

            flag = False
            for name in connVertex:
                if name == path[i + 1]:
                    flag = True

            if not flag:
                return False

        return True

    def get_num_vertex_who_have_sum_incident_edge_more_value(self, value):
        """
        :param value: value (int)
        :return: Returns list<int> - numbers of vertex
        """
        sumIncEdge = list()  # list<int> - for each edge contains weight incident edges

        for i in range(0, len(self.matrix)):
            sumIncEdge.append(0)

            for j in range(0, len(self.matrix)):
                if self.matrix[i][j] != 0:
                    sumIncEdge[i] += self.matrix[i][j]
                if self.matrix[j][i] != 0:
                    sumIncEdge[i] += self.matrix[j][i]

        res = list()
        for i in range(0, len(sumIncEdge)):
            if sumIncEdge[i] > value:
                res.append(i)

        return res

    def get_count_edges(self):
        counter = 0
        for row in range(0, len(self.matrix)):
            for column in range(0, len(self.matrix)):
                if self.matrix[row][column] != 0:
                    counter += 1

        return counter
