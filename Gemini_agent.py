from agents import Agent,RunContextWrapper,function_tool
from gemini_config import model


@function_tool
def multiplier(a: int, b: int) -> int:
    return a * b

@function_tool
def adder(a: int, b: int) -> int:
    return a + b

@function_tool
def divider(a: int, b: int) -> float:
    if b == 0:
        return 0
    return a / b 

@function_tool
def subtractor(a: int, b: int) -> int:
    return a - b

def dynamic_instruction(ctx: RunContextWrapper, agent):
 
    instruction = (
        f"Based on the context, your name is {ctx.context['name']}, "
        f"you are a {ctx.context['age']} year old agent who lives in {ctx.context['location']}, "
        f"your a teacher, who will answer according to there queries "
        f"you will answer the question based on the data provided related to any random subject, like geography, history, english and any other subject."
        f"you will also answer general knowledge questions."
    )

    return instruction

teacher_agent = Agent(
    name="GeminiAgent",
    instructions=dynamic_instruction,
    model=model,
    tools=[multiplier, adder, divider, subtractor]
    )