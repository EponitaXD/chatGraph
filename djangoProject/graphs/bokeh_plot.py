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

    # invoke model
    model = OllamaLLM(model="codestral")
    output = model.invoke(query)

    # extract code
    start = "```python"
    end = "```"
    substring = output[output.find(start)+len(start):output.rfind(end)]
    substring = substring + "result = components(p)"
    print("New string: " + substring)  # Output: sample

    # create file for debuging purposes
    file_name = "python_code.py"
    try:
        with open(file_name, 'w') as file:
            file.write(substring)
        print(f"String successfully written to '{file_name}'")
    except IOError as e:
        print(f"Error writing to file: {e}")

    with open("python_code.py", "r") as file:
        code = file.read()

    # execute code
    loc = {}
    exec(code, globals(), loc)
    components = loc['result']
    print("components: ")
    print(components) 

    return components