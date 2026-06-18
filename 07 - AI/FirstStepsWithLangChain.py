
import dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
dotenv.load_dotenv()

#print(os.getenv("OPENAI_API_KEY"))

chat_model = ChatOpenAI(model="gpt-4o", temperature=0)
#response = chat_model.invoke("What is blood pressure?")

#print(response.content)

messages = [
    SystemMessage(
        content="""You are an assistant knowledgeable about heathcare. 
            Only answer healthcate-related questions."""
    )
]

question = HumanMessage(content="What is blood pressure?")

messages.append(question)

template_string = """" You're an expert on {topic}. 
    
    Here's an user review:
    {context}
    
    Please answer the following question concisely in one word:
    {question}
    """

prompt_template = PromptTemplate.from_template(template_string)

filled_prompt = prompt_template.format(
    topic="User Feedback",
    context="I love it here!",
    question="Any positive reviews?"
)

response = chat_model.invoke(filled_prompt)

print(response.content)



#response = chat_model.invoke(messages)

#print(response.content)