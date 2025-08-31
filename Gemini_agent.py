from agents import Agent,RunContextWrapper
from gemini_config import model

def dynamic_instruction(ctx: RunContextWrapper, agent):
 
    instruction = (
        f"Based on the context, your name is {ctx.context['name']}, "
        f"you are a {ctx.context['age']} year old agent who lives in {ctx.context['location']}, "
        f"your a teacher, who will answer according to there queries "
        f"you will answer the question based on the data provided related to any random subject."
    )

    return instruction

teacher_agent = Agent(
    name="GeminiAgent",
    instructions=dynamic_instruction,
    model=model)