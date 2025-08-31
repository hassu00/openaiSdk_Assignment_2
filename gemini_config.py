from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel

GEMINI_API_KEY = config('GEMINI_API_KEY')
GEMINI_BASE_URL = config('GEMINI_BASE_URL')
gemini_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=GEMINI_BASE_URL
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",openai_client=gemini_client
)
