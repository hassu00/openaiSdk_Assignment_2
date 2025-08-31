from agents import Runner, RunContextWrapper,function_tool
# import asyncio
from Gemini_agent import teacher_agent



# def info(ctx: RunContextWrapper) -> str:
#     return f"my name is {ctx.context['name']} and my Role is {ctx.context['role']}, I will help you with your queries."

context = {
    "name":"Gemini agent",
    "age": 30,
    "location": "Pakistan",
}


prompt = input("Enter your question: ")

result = Runner.run_sync(
    teacher_agent,
    prompt,
    context=context,
)
print(result.final_output)

