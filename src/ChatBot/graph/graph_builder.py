from langgraph.graph import StateGraph, START, END
from src.ChatBot.state.state import State
from src.ChatBot.nodes.basic_chatbot_node import BasicChatBotNode
from src.ChatBot.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.ChatBot.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition
from src.ChatBot.nodes.global_news_node import GlobalNewsNode
from src.ChatBot.nodes.india_news_node import IndiaNewsNode
from src.ChatBot.nodes.sports_news_node import SportsNewsNode
from src.ChatBot.nodes.technology_news_node import TechnologyNewsNode

class GraphBuilder:

    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """

        self.basic_chatbot_node=BasicChatBotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """
        ## Define the tool and tool node
        tools=get_tools()
        tool_node=create_tool_node(tools)

        ## Define the LLM
        llm=self.llm

        ## Define the chatbot node

        obj_chatbot_with_node=ChatbotWithToolNode(llm)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)
        ## Add nodes
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)
        # Define conditional and direct edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")

    def global_news_builder_graph(self):

        global_news_node=GlobalNewsNode(self.llm)

        ## added the nodes

        self.graph_builder.add_node("fetch_news",global_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",global_news_node.summarize_news)
        self.graph_builder.add_node("save_result",global_news_node.save_result)

        #added the edges

        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result", END)

    def india_news_builder_graph(self):

        india_news_node=IndiaNewsNode(self.llm)

        ## added the nodes

        self.graph_builder.add_node("fetch_news",india_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",india_news_node.summarize_news)
        self.graph_builder.add_node("save_result",india_news_node.save_result)

        #added the edges

        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result", END)

    def sports_news_builder_graph(self):

        sports_news_node=SportsNewsNode(self.llm)

        ## added the nodes

        self.graph_builder.add_node("fetch_news",sports_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",sports_news_node.summarize_news)
        self.graph_builder.add_node("save_result",sports_news_node.save_result)

        #added the edges

        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result", END)

    def technology_news_builder_graph(self):

        technology_news_node=TechnologyNewsNode(self.llm)

        ## added the nodes

        self.graph_builder.add_node("fetch_news",technology_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",technology_news_node.summarize_news)
        self.graph_builder.add_node("save_result",technology_news_node.save_result)

        #added the edges

        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result", END)
    
    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic ChatBot":
            self.basic_chatbot_build_graph()
        if usecase == "ChatBot with Web":
            self.chatbot_with_tools_build_graph()
        if usecase == "Global News":
            self.global_news_builder_graph()
        if usecase == "India News":
            self.india_news_builder_graph()
        if usecase == "Sports News":
            self.sports_news_builder_graph()
        if usecase == "Technology News":
            self.technology_news_builder_graph()

        return self.graph_builder.compile()