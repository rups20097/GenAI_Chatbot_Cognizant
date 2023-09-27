from dotenv import load_dotenv
import openai
import os
from langchain.llms import OpenAI
from langchain.chat_models import AzureChatOpenAI
load_dotenv()

DEPLOYMENT_NAME="openaidemomb001"
os.environ["OPENAI_API_KEY"]= os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_BASE"] = "https://openai-demo-mb-001.openai.azure.com/"
os.environ["OPENAI_API_VERSION"] = "2023-05-15"

chat = AzureChatOpenAI(deployment_name="openaidemomb001", temperature=0.7,tiktoken_model_name="gpt-3.5-turbo")
print(chat.predict("what is the capital of India?"))