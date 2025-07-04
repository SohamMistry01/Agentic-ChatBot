import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase= usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase= self.usecase
        graph = self.graph
        user_message = self.user_message
        print(user_message)
        if usecase =="Basic ChatBot":
                for event in graph.stream({'messages':("user",user_message)}):
                    print(event.values())
                    for value in event.values():
                        print(value['messages'])
                        with st.chat_message("user"):
                            st.write(user_message)
                        with st.chat_message("assistant"):
                            st.write(value["messages"].content)
        
        elif usecase=="ChatBot with Web":
             # Prepare state and invoke the graph
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)
            for message in res['messages']:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message)==ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif type(message)==AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)

        elif usecase == "Global News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing global news... ⏳"):
                result = graph.invoke({"messages": frequency})
                try:
                    # Read the markdown file
                    GLOBAL_NEWS_PATH = f"./News_Summary/{frequency.lower()}_global_summary.md"
                    with open(GLOBAL_NEWS_PATH, "r") as file:
                        markdown_content = file.read()

                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {GLOBAL_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

        elif usecase == "India News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing India news... ⏳"):
                result = graph.invoke({"messages": frequency})
                try:
                    # Read the markdown file
                    INDIA_NEWS_PATH = f"./News_Summary/{frequency.lower()}_india_summary.md"
                    with open(INDIA_NEWS_PATH, "r") as file:
                        markdown_content = file.read()

                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {INDIA_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

        elif usecase == "Sports News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing sports news... ⏳"):
                result = graph.invoke({"messages": frequency})
                try:
                    # Read the markdown file
                    SPORTS_NEWS_PATH = f"./News_Summary/{frequency.lower()}_sports_summary.md"
                    with open(SPORTS_NEWS_PATH, "r") as file:
                        markdown_content = file.read()

                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {SPORTS_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

        elif usecase == "Technology News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing technology news... ⏳"):
                result = graph.invoke({"messages": frequency})
                try:
                    # Read the markdown file
                    TECHNOLOGY_NEWS_PATH = f"./News_Summary/{frequency.lower()}_technology_summary.md"
                    with open(TECHNOLOGY_NEWS_PATH, "r") as file:
                        markdown_content = file.read()

                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {TECHNOLOGY_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")