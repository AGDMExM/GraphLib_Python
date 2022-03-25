from typing import List
import igraph

from GraphLib_Python.Model.EdgeModel import EdgeModel
from GraphLib_Python.Model.MatrixModel import MatrixModel
from GraphLib_Python.Model.TableOfRecordModel import TableOfRecordModel


class GraphLibCaAGM_Python:
    matrixModel: MatrixModel = None
    edgeModel: EdgeModel = None
    tableOfRecordModel: TableOfRecordModel = None

    def __init__(self, namesVertex, matrix):
        """
        :param namesVertex: namesVertex (list<string>)
        :param matrix: matrix (list<list<int>): contains int values, where 0 - no edge
        """

        self.matrixModel = MatrixModel(namesVertex, matrix)
        self.edgeModel = EdgeModel(self.matrixModel)
        self.tableOfRecordModel = TableOfRecordModel(self.matrixModel)

    def create_image(self, directed_=True, layout=""):
        """Save graph with name "graph" """
        graph = igraph.Graph(directed=directed_)

        graph.add_vertices(len(self.edgeModel.namesVertex))
        graph.vs["label"] = self.edgeModel.namesVertex

        edges = list()
        for edge in self.edgeModel.listOfEdges:
            edges.append((self.edgeModel.namesVertex.index(edge.from_),
                         self.edgeModel.namesVertex.index(edge.to)))

        graph.add_edges(edges)

        weights: List[int] = list()
        for edge in self.edgeModel.listOfEdges:
            weights.append(edge.weight)

        graph.es['weight'] = weights
        graph.es['label'] = weights

        graph.es['curved'] = False

        igraph.plot(graph, layout_=graph.layout(layout), bbox=(500, 500), vertex_label_color='black', vertex_label_size=15,
                    vertex_size=30, vertex_color='white', edge_width=[edge for edge in graph.es['weight']])
