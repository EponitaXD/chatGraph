import math
import re
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, Ellipse, StaticLayoutProvider
from bokeh.palettes import Spectral8
from bokeh.embed import components

from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_community.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def create_scatter_plot():
    print("Inside!!!!")
    # Define the query to generate a Bokeh line chart and return embeddable HTML
    query = """
        Write Python code to:
        1. Create a line plot using Bokeh that shows monthly revenue for January to June: [150, 200, 250, 300, 400, 500]
        2. Use `bokeh.embed.components()` to generate the script and div for embedding.
        3. Print the div and script as plain text output.
        """


    model = OllamaLLM(model="codestral")

    output = model.invoke(query)


    output = """
    1. To create a line plot in Bokeh, you first need to import the required modules. Then you define your data (monthly revenue) and use it to create the figure. Here's how you can do this:
    
    ```python
    from bokeh.plotting import figure, show
    from bokeh.embed import components

    # Prepare some data
    x = list(range(1, 7)) # Months from Jan (1) to June (6)
    y = [150, 200, 250, 300, 400, 500] # Revenue for each month

    # Create a figure object
    p = figure(title="Monthly Revenue", x_axis_label='Month', y_axis_label='Revenue')

    # Add a line to the plot
    p.line(x, y)

    # Generate the script and div for embedding
    script, div = components(p)

    # Print the div and script as plain text output
    print('div:', div)
    print('script:', script)
    ```

    2. The `bokeh.embed.components()` function is used to generate the JavaScript (script) and HTML (div) for embedding a Bokeh plot into a webpage or dashboard. In this case, it generates a line plot of monthly revenue using the data provided.

    3. Finally, we print out the div and script as plain text output so you can see what they look like.
    """

    # extract code
    start = "```python"
    end = "```"
    substring = output[output.find(start)+len(start):output.rfind(end)]
    print("New string: " + substring)  # Output: sample

    file_name = "python_code.py"

    try:
        with open(file_name, 'w') as file:
            file.write(output)
        print(f"String successfully written to '{file_name}'")
    except IOError as e:
        print(f"Error writing to file: {e}")

    with open("python_code.py", "r") as file:
        code = file.read()

    loc = {}
    exec(code, globals(), loc)
    return_workaround = loc['return']
    print(return_workaround)  