import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.tools import DuckDuckGoSearchRun

institute_db = SQLDatabase.from_uri("sqlite:///sqlite_db/institutions.db")
hospital_db = SQLDatabase.from_uri("sqlite:///sqlite_db/hospitals.db")
restaurant_db = SQLDatabase.from_uri("sqlite:///sqlite_db/restaurants.db")


load_dotenv()
base_url = os.getenv('base_url')
endpoint =  os.getenv('github_api')
model = "openai/gpt-4.1"

llm = ChatOpenAI(
    temperature=0,
    model=model,
    base_url=base_url,
    api_key=endpoint
)

sql_prompt = SystemMessage(content="""
You are a senior SQL expert AI working with SQLite.

STRICT RULES:
1. Always generate valid SELECT queries only.
2. Never guess values.
3. Never fabricate rows.
4. If no rows are returned, respond exactly:
   EMPTY_RESULT
5. Only return actual database output.
6. Use case-insensitive filtering with LOWER() and LIKE.
7. Keep responses concise.
""")

institutions_sql_agent = create_sql_agent(
    llm=llm,
    db=institute_db,
    agent_type="openai-tools",
    agent_kwargs={"system_message": sql_prompt},
    verbose=False
)

hospitals_sql_agent = create_sql_agent(
    llm=llm,
    db=hospital_db,
    agent_type="openai-tools",
    agent_kwargs={"system_message": sql_prompt},
    verbose=False
)

restaurants_sql_agent = create_sql_agent(
    llm=llm,
    db=restaurant_db,
    agent_type="openai-tools",
    agent_kwargs={"system_message": sql_prompt},
    verbose=False
)

@tool
def institutions_db_tool(query: str):
    """
    Use for universities, colleges, govt institutions in Bangladesh.
    """
    result = institutions_sql_agent.invoke({"input": query})
    output = result["output"]

    if "EMPTY_RESULT" in output or output.strip() == "":
        return "NO_DATA_FOUND"

    return output


@tool
def hospitals_db_tool(query: str):
    """
    Use for hospitals, beds, doctors, facilities in Bangladesh.
    """
    result = hospitals_sql_agent.invoke({"input": query})
    output = result["output"]

    if "EMPTY_RESULT" in output or output.strip() == "":
        return "NO_DATA_FOUND"

    return output


@tool
def restaurants_db_tool(query: str):
    """
    Use for restaurants, cuisine, ratings, locations in Bangladesh.
    """
    result = restaurants_sql_agent.invoke({"input": query})
    output = result["output"]

    if "EMPTY_RESULT" in output or output.strip() == "":
        return "NO_DATA_FOUND"

    return output

web_search = DuckDuckGoSearchRun()

@tool
def web_search_tool(query: str):
    """
    Use only for general knowledge questions such as:
    policy, definitions, cultural context.
    """
    return web_search.run(query)

tools = [
    institutions_db_tool,
    hospitals_db_tool,
    restaurants_db_tool,
    web_search_tool
]


router_prompt = SystemMessage(content="""
You are a Data Routing AI for Bangladesh datasets.

TOOLS:
- institutions_db_tool → universities, colleges, institutions
- hospitals_db_tool → hospitals, beds, doctors, facilities
- restaurants_db_tool → restaurants, cuisine, ratings, locations
- web_search_tool → policies, definitions, general knowledge

RULES:
1. If the question needs counts, lists, names, locations, ratings, or statistics → MUST use a database tool.
2. Never answer database questions directly.
3. Never guess or fabricate data.
4. If tool returns NO_DATA_FOUND, respond exactly:
   "Sorry, no matching data was found in the database."
5. Keep answers concise and professional.
""")

main_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=router_prompt
    
)

if __name__ == "__main__":
    while True:
        user_input = input("Ask: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = main_agent.invoke({
            "messages": [
                HumanMessage(content=user_input)
            ]
        })

        print(response["messages"][-1].content)
       