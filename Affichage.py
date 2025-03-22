import itertools
import random

import matplotlib
import numpy
import plotly
import plotly.graph_objects as go
from Graphe import Graphe
from Edge import Edge
from Vertice import Vertice


class Affichage:
    fig = None

    def trace(self, graphe: Graphe):
        for vertice in graphe.get_vertices():
            print(vertice.get_nom() + " : " + str(vertice.get_neighbours()))
        edge_x = []
        edge_y = []
        for edge in graphe.get_edges():
            x0, y0 = edge.get_origine().getPosition()
            x1, y1 = edge.get_end().getPosition()
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)
        edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=0.5, color='#888'), hoverinfo='none', mode='lines')
        node_text = []
        node_color = []
        for node in graphe.get_vertices():
            node_text.append(node.get_nom())
            node_color.append(node.get_color())
        vertice_x = []
        vertice_y = []
        for node in graphe.get_vertices():
            x, y = node.getPosition()
            vertice_x.append(x)
            vertice_y.append(y)

        vertice_trace = go.Scatter(x=vertice_x, y=vertice_y, mode='markers+text', hoverinfo='text', text=node_text,
                                   textposition='top center', textfont=dict(size=14, color="blue"),
                                   marker=dict(showscale=True, colorscale='Greens', reversescale=True, color=node_color,
                                               size=25,
                                               line_width=3, symbol="circle"), name='vertices')

        self.fig = go.Figure(data=[edge_trace, vertice_trace],
                             layout=go.Layout(title='<br>Network graph made with Python', titlefont_size=16,
                                              showlegend=False,
                                              margin=dict(b=20, l=5, r=5, t=40),
                                              annotations=[
                                                  dict(showarrow=False, xref="paper", yref="paper", x=0.005, y=-0.002)],
                                              xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                              yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                             )
        self.fig = go.FigureWidget(self.fig)
        self.fig.show()

    def update_fig_color(self, colors):
        self.fig.for_each_trace(
            lambda trace: trace.update(marker_color=colors) if trace.name == "vertices" else ()  #creer fonction lambda qui prend trace en parametre
        )
        self.fig.show()

