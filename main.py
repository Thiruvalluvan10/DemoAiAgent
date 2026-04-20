from pydantic import BaseModel
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core import ChatPromptTemplate

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    api_key=api_key
)
response = llm.invoke("Explain black holes simply")
print(response.content)