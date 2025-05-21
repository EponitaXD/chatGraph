import math
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, Ellipse, StaticLayoutProvider
from bokeh.palettes import Spectral8
from bokeh.embed import components

def create_scatter_plot():
    # list the nodes and initialize a plot
    N = 8
    node_indices = list(range(N))

    plot = figure(title="Graph layout demonstration", x_range=(-1.1,1.1),
                y_range=(-1.1,1.1), tools="", toolbar_location=None)

    graph = GraphRenderer()

    # replace the node glyph with an ellipse
    # set its height, width, and fill_color
    graph.node_renderer.glyph = Ellipse(height=0.1, width=0.2,
                                        fill_color="fill_color")

    # assign a palette to ``fill_color`` and add it to the data source
    graph.node_renderer.data_source.data = dict(
        index=node_indices,
        fill_color=Spectral8)

    # add the rest of the assigned values to the data source
    graph.edge_renderer.data_source.data = dict(
        start=[0]*N,
        end=node_indices)

    # generate ellipses based on the ``node_indices`` list
    circ = [i*2*math.pi/8 for i in node_indices]

    # create lists of x- and y-coordinates
    x = [math.cos(i) for i in circ]
    y = [math.sin(i) for i in circ]

    # convert the ``x`` and ``y`` lists into a dictionary of 2D-coordinates
    # and assign each entry to a node on the ``node_indices`` list
    graph_layout = dict(zip(node_indices, zip(x, y)))

    # use the provider model to supply coourdinates to the graph
    graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

    # render the graph
    plot.renderers.append(graph)

    return components(plot)
