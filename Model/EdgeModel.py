from .Edge import Edge
from .MatrixModel import MatrixModel


class EdgeModel:
    listOfEdges = list()  # list type is Edge
    namesVertex = list()  # list type is string

    def __init__(self, matrixModel):
        self._init(matrixModel)

    def _init(self, matrixModel):
        matrixModel: MatrixModel
        self.namesVertex = matrixModel.namesVertex.copy()

        for row in range(0, len(matrixModel.matrix)):
            line = matrixModel.matrix[row]  # list<int>
            for column in range(0, len(matrixModel.matrix)):
                value = line[column]
                if value == 0:
                    continue

                self.listOfEdges.append(Edge(self.namesVertex[row], self.namesVertex[column], value))

    def _get_num_vertex_by_name(self, name):
        """Returns -1 if not found"""
        for i in range(0, len(self.listOfEdges)):
            if self.listOfEdges[i].from_ == name:
                return i

        return -1

    def get_neighbors_vertex_by_name(self, name):
        """Returns list<string> - names neighbors"""
        res = list()

        for edge in self.listOfEdges:
            if name == edge.from_:
                res.append(edge.to)
            if name == edge.to:
                res.append(edge.from_)

        return res

    def path_exist(self, path):
        """
        Returns True - if path exist, False - if not
        :param path: path (list<string>): names vertex
        """
        for i in range(0, len(path) - 1):
            nameVertex = path[i]
            connVertex = list()  # list<string> - names neighbor

            for edge in self.listOfEdges:
                if edge.from_ == nameVertex:
                    connVertex.append(edge.to)

            flag = False
            for connName in connVertex:
                if connName == path[i + 1]:
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

        for i in range(0, len(self.namesVertex)):
            sumIncEdge.append(0)

        for numEdge in range(0, len(self.listOfEdges)):
            sumIncEdge[self.namesVertex.index(self.listOfEdges[numEdge].from_)] += self.listOfEdges[numEdge].weight
            sumIncEdge[self.namesVertex.index(self.listOfEdges[numEdge].to)] += self.listOfEdges[numEdge].weight

        res = list()
        for i in range(0, len(sumIncEdge)):
            if sumIncEdge[i] > value:
                res.append(i)

        return res

    def get_count_edges(self):
        return len(self.listOfEdges)
