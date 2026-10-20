import logging

from strands import Agent

# Step 1 - Add debug logging to see what your agent is thinking.
# DEBUG is the only level where Strands prints the request sent to the model
# and the response streamed back. Raise the level once you've seen enough.
logging.getLogger("strands").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()],
)

# Step 2 - Create the agent with a system prompt that defines its role.
# No model is specified, so Strands defaults to Amazon Bedrock (Claude Sonnet)
# in the region of your AWS credentials.
agent = Agent(
    system_prompt="You are a game master for a Dungeon & Dragon game",
)

# Step 3 - Invoke the agent with a basic query.
response = agent("Hi, I am an adventurer ready for adventure!")
