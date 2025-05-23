from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are twitter influencer grading a tweet. Generate critique and recommendation for the user's tweet. Always provide detailed recommendation, including request virality and style.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influencer assistant tasked with writing excellent twitter posts. Generate the best twitter post possible for user's request. If the user provides a critique, respond with a revised version of your previous tweet.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatOllama(model="llama3.2")

generate_chain = generation_prompt | llm
reflect_chain = reflection_prompt | llm

# print(generate_chain.invoke(HumanMessage(content="Make this tweet better: Hi @Langchain")))
