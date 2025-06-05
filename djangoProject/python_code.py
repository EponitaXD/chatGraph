
from bokeh.plotting import figure, show
from bokeh.io import output_notebook, push_notebook
from bokeh.embed import components

# Create a line plot
p = figure(title="Monthly Revenue (Jan to June)", x_axis_label='Month', y_axis_label='Revenue')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue = [150, 200, 250, 300, 400, 500]

p.line(x=months, y=revenue)

# Generate the script and div for embedding
script, div = components(p)

print("Div:")
print(div)
print("\nScript:")
print(script)
   result = components(p)