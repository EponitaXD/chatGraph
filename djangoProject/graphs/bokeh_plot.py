import math
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, Ellipse, StaticLayoutProvider
from bokeh.palettes import Spectral8
from bokeh.embed import components

from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_community.llms import OpenAI

def create_scatter_plot():
    print("Inside!!!!")
    # Load LLM (you can use GPT-3.5 or GPT-4)
    llm = OpenAI(temperature=0, api_key="")

    # Use the Python REPL tool to execute code
    tools = [PythonREPLTool()]

    # Create the agent
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    # Define the query to generate a Bokeh line chart and return embeddable HTML
    query = """
    Write Python code to:
    1. Create a line plot using Bokeh that shows monthly revenue for January to June: [150, 200, 250, 300, 400, 500]
    2. Use `bokeh.embed.components()` to generate the script and div for embedding.
    3. Print the div and script as plain text output.
    """

    # Run the agent
    output = llm.invoke(query)
    print("Out: ")
    print(output)
