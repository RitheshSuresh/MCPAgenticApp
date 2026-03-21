import os
import asyncio
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "github": {
                "transport": "http",
                "url": os.environ["GITHUB_MCP_URL"],
                "headers": {
                    "Authorization": f"Bearer {os.environ['GITHUB_PAT']}"
                },
            }
        }
    )

    tools = await client.get_tools()
    print("Loaded tools:", [tool.name for tool in tools])

    llm = ChatOpenAI(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],  # your Azure deployment name
        base_url=os.environ["AZURE_OPENAI_ENDPOINT"].rstrip("/") + "/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )

    agent = create_agent(model=llm, tools=tools)

    prompt = """
    Inspect the GitHub repository:

    Owner: RitheshSuresh
    Repository: MCPAgenticApp
    Branch: main

    Follow these steps:

    1. First, list files in the repository using available tools.
    2. Identify important Python files.
    3. Read those files using get_file_contents.
    4. Then:
    - Explain what the code does
    - Identify inefficiencies and bugs
    - Suggest improvements

    Do NOT assume file paths. Always discover them first.
    """

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": prompt}]}
    )
    print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())