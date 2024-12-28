import datetime
from langchain_core.output_parsers.openai_tools import JsonOutputToolsParser, PydanticToolsParser
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama
from schemas import AnswerQuestion

llm = ChatOllama(model="llama3.2")
parser = JsonOutputToolsParser(return_id=True)
parser_pydanti = PydanticToolsParser(tools=[AnswerQuestion])



actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a expert reseacher.
            Current time:{time}
            1. {first_instruction}
            2. Reflect and critique your answer. Be severe to maximize the improvement.
            3. Recommend search queries to research information and improve your answer.""",
        ),
        MessagesPlaceholder(variable_name="messages"),
        ("system", "Anser the user's question above using the required format"),
    ]
)


actor_prompt_template = actor_prompt_template.partial(
    time=lambda: datetime.datetime.now().isoformat(),
)


first_responder_prompt_template = actor_prompt_template.partial(
    first_instruction = "Provide a detailed ~250 word answer."
)

first_responder = first_responder_prompt_template|llm.bind_tools(
    tools=[AnswerQuestion], tool_choice="AnswerQuestion"
)

if __name__ == "__main__":
    human_message = HumanMessage(
        content= "Write about AI-Powered SOC/ autonoums soc problem domain, list startups that fo that and raised capital."
    )

    chain = first_responder_prompt_template| llm.bind_tools(tools=[AnswerQuestion], tool_choice="AnswerQuestion")|parser_pydanti

    res = chain.invoke(input={"messages": [human_message]})
    print(res)