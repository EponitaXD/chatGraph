
from bokeh.plotting import figure, show
from bokeh.embed import components

def create_scatter_plot():
    # prepare some data
    x = [1, 2, 3, 4, 5]
    y1 = [6, 7, 2, 4, 5]
    y2 = [2, 3, 4, 5, 6]
    y3 = [4, 5, 5, 7, 2]

    # create a new plot with a title and axis labels
    p = figure(title="Multiple line example", x_axis_label="x", y_axis_label="y")

    # add multiple renderers
    p.line(x, y1, legend_label="Temp.", color="blue", line_width=2)
    p.line(x, y2, legend_label="Rate", color="red", line_width=2)
    p.line(x, y3, legend_label="Objects", color="green", line_width=2)

    # show the results
    return components(p)