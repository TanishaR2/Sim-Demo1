import streamlit as st
import ollama

# streamlit UI
st.title = ("Ollama Chatbot")
st.write("Ask me anything!")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
  
  
  
# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
 
 

       
# User input
user_input = st.chat_input("Type your question...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content":user_input})
    
    # get responses from ollama(using dolphin phi model)
    response = ollama.chat(model="dolphin-phi", messages=[{"role": "user", "content":user_input}])
    
    bot_reply = response["message"]["content"]
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "user", "content": bot_reply})
    
    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)