from strands import Agent
# Step 1 - Import tool from strands
from strands import tool


# Step 1 - Add the decorator to transform your function into a tool
@tool
def roll_dice(faces: int = 6) -> int:
    # Step 2 - Write a docstring with the description, an Args section and the return value
    """Roll a single die and return the result.

    Simulates rolling one die with the given number of faces and returns a
    random integer between 1 and the number of faces (inclusive). Call this
    tool once per die; to roll multiple dice, call it repeatedly.

    Args:
        faces: The number of faces on the die (e.g. 6 for a d6, 20 for a d20).
            Must be at least 1. Defaults to 6.

    Returns:
        A random integer from 1 to faces, representing the die's outcome.
    """
    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)


print(roll_dice.tool_spec)  # what Strands tells the model about your tool

dice_master = Agent(
    # Step 3 - Add the tool to the agent
    tools=[roll_dice],
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in D&D adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about D&D mechanics, ability scores, and can help players with character creation.
    When rolling ability scores, remember the traditional method: roll 4d6, drop the lowest die."""
)

dice_master("Help me create a new D&D character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")
