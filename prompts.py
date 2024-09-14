#this file = turns natural language queries (in english) into python pandas code that can be run on pandas dataframe to get answers from dataset
from llama_index  import PromptTemplate


#telling engine what it should be doing with Pandas data
instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression."""

#when making a prompt to the AI(gpt), it recieves context in 3 ways
#context in the dataframe to understand structure of data, instructions that guide AI, and the normal language query used to generate a relevant python exp
new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

context = """Purpose: The primary role of this agent is to assist users by providing accurate 
            information about world population statistics and details about a country. """

