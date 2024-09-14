from dotenv import load_dotenv #used to read env variables and load them into the enviroment
import os 
import pandas as pd
from llama_index.query_engine import PandasQueryEngine #will allow us to ask specific questions about the data
from prompts import new_prompt, instruction_str, context
from notetaker_engine import note_engine
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI
from pdf import afghan_engine

load_dotenv() #when called, the API_KEY from .env will be loaded into enviroment

population_path = os.path.join("dataset", "Population.csv")
population_df = pd.read_csv(population_path)

population_query_engine = PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})
#using this we can directly query
#this is a tool that the agent would use to create a more human readable response

tools = [
    note_engine,
    QueryEngineTool(query_engine=population_query_engine, 
                    metadata=ToolMetadata(
                        name="population_data",
                        description="gives information about the population",
        ),
    ),
    QueryEngineTool(query_engine=afghan_engine, 
                    metadata=ToolMetadata(
                        name="afghan_data",
                        description="gives information about the afghanistan history",
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo-0125")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context="context")

while (prompt :=input("Ask any questions(prompts), (enter q to quit)")) != "q":
       result = agent.query(prompt)
       print(result)





