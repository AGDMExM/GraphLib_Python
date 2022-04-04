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

    def create_image(self, directed_=True, layout="", highlightedEdges=None, highlightedColor="red"):
        """
        Save graph with name "graph"
        :param highlightedColor: Color for colored edges
        :param directed_:
        :param layout: select "grid" if you want to get a grid
        :param highlightedEdges: List[int] - list of idVertex for coloring
        :return:
        """
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

        if highlightedEdges is not None:
            highlightedEdges: List[int]

            for i in range(0, len(highlightedEdges) - 1):
                _from = highlightedEdges[0]
                _to = highlightedEdges[1]

                for edge in graph.es:
                    if edge.source == _from and edge.target == _to:
                        edge["color"] = highlightedColor

                highlightedEdges.pop(0)

        igraph.plot(graph, layout=graph.layout(layout), bbox=(500, 500), vertex_label_color='black',
                    vertex_label_size=15,
                    vertex_size=30, vertex_color='white', edge_width=[edge for edge in graph.es['weight']])
