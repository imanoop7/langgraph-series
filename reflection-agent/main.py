from typing import List, Sequence
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chain import generate_chain, reflect_chain



def generate_node(state:Sequence[BaseMessage]):
    return generate_chain.invoke({"messages" : state})


def refect_node(message:Sequence[BaseMessage]):
    res= reflect_chain.invoke({"messages" : message})
    return [HumanMessage(content=res.content)]  


builder = MessageGraph()

builder.add_node("generate", generate_node)
builder.add_node("reflect", refect_node)    

builder.set_entry_point("generate")

def should_continue(state:List[BaseMessage]):
    if len(state) < 5:
        return END
    return "reflect"


builder.add_conditional_edges("generate", should_continue)
builder.add_edge("reflect", "generate")

graph = builder.compile()


if __name__ == "__main__":
    inputs =HumanMessage(content=""" Make this tweet better:
                         @Langchain 
                         - newly tool calling feature is seriously underrated.
                         - after a long wait it's finally here. making the implementation of agents across different models with function calling.
                         - have written a medium article on it. check it out.
    """)
    response = graph.invoke(inputs)
    print(response) 