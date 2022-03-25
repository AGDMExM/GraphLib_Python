import copy
from typing import List

from .RowTable import RowTable


class TableOfRecordModel:
    table: List[RowTable] = list()  # type list is RowTable

    def __init__(self, matrixModel):
        self._init(matrixModel)

    def _init(self, matrixModel):
        namesVertex = matrixModel.namesVertex

        for i in range(0, len(namesVertex)):
            self.table.append(RowTable())
            self.table[i].number = i
            self.table[i].name = namesVertex[i]

        for row in range(0, len(matrixModel.matrix)):
            line = matrixModel.matrix[row]  # list<int>
            currRow = self.table[row]

            for column in range(0, len(line)):
                value = line[column]

                if value == 0:
                    continue

                currRow.childCount += 1
                currRow.neighborsCount += 1
                currRow.numbersChildVertex = copy.deepcopy(currRow.numbersChildVertex)
                currRow.numbersChildVertex.append(column)
                currRow.numbersNeighborsVertex = copy.deepcopy(currRow.numbersNeighborsVertex)
                currRow.numbersNeighborsVertex.append(column)
                currRow.weightsOutputEdge = copy.deepcopy(currRow.weightsOutputEdge)
                currRow.weightsOutputEdge.append(value)

                self.table[column].parentCount += 1
                self.table[column].numbersParentVertex = copy.deepcopy(self.table[column].numbersParentVertex)
                self.table[column].numbersParentVertex.append(row)
                self.table[column].weightsInputEdge = copy.deepcopy(self.table[column].weightsInputEdge)
                self.table[column].weightsInputEdge.append(value)
                self.table[column].neighborsCount += 1
                self.table[column].numbersNeighborsVertex = copy.deepcopy(self.table[column].numbersNeighborsVertex)
                self.table[column].numbersNeighborsVertex.append(row)

    def _get_row_by_vertex_name(self, name):
        """Returns None if not found"""
        row: RowTable
        for row in self.table:
            if row.name == name:
                return row

        return None

    def get_neighbors_vertex_by_name(self, name):
        """Returns list<string> - names neighbors"""
        row = self._get_row_by_vertex_name(name)
        res = list()

        for number in row.numbersNeighborsVertex:
            res.append(self.table[number].name)

        return res

    def path_exist(self, path):
        """
        Returns True - if path exist, False - if not
        :param path: path (list<string>): names vertex
        """
        for i in range(0, len(path) - 1):
            currRow = self._get_row_by_vertex_name(path[i])
            flag = False

            for numChild in range(0, len(currRow.numbersChildVertex)):
                if path[i + 1] == self.table[currRow.numbersChildVertex[numChild]].name:
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

        for i in range(0, len(self.table)):
            currVertex: RowTable = self.table[i]
            sumIncEdge.append(0)

            for weight in currVertex.weightsInputEdge:
                sumIncEdge[i] += weight
            for weight in currVertex.weightsOutputEdge:
                sumIncEdge[i] += weight

        res = list()
        for i in range(0, len(sumIncEdge)):
            if sumIncEdge[i] > value:
                res.append(i)

        return res

    def get_count_edges(self):
        counter = 0

        for row in self.table:
            counter += len(row.numbersChildVertex)

        return counter

