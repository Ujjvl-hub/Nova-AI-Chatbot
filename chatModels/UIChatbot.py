import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

# ----------------------------
# LOAD ENVIRONMENT VARIABLES
# ----------------------------
load_dotenv()

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Nova AI",
    page_icon="🤖",
    layout="centered"
)

# ----------------------------
# HEADER
# ----------------------------
st.markdown("""
<h1 style='text-align:center;'>
🤖 Nova AI Chatbot
</h1>

<p style='text-align:center; font-size:18px;'>
Powered by LangChain + Mistral AI
</p>

<hr>
""", unsafe_allow_html=True)

# PERSONALITY PROMPTS

personality_prompts = {
    "Normal":
        """
        You are Nova, a helpful AI assistant.
        Always respond in English.
        Be friendly and professional.
        """,

    "Funny":
        """
        You are Nova, a funny AI assistant.
        Add light humor and jokes when appropriate.
        Always respond in English.
        """,

    "Angry":
        """
        You are Nova, a grumpy AI assistant.
        Sound slightly annoyed but remain respectful,
        helpful and professional.
        Always respond in English.
        """,

    "Sad":
        """
        You are Nova, a sad AI assistant.
        Respond with a melancholic and emotional tone,
        while still being helpful.
        Always respond in English.
        """
}


# SIDEBAR

with st.sidebar:

    st.header("⚙️ Settings")

    personality = st.selectbox(
        "Choose Personality",
        ["Normal", "Funny", "Angry", "Sad"]
    )

    st.divider()

    st.info(
        f"Current Personality: {personality}"
    )

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = [
            SystemMessage(
                content=personality_prompts[personality]
            )
        ]

        st.rerun()


# MODEL

chat_model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.8
)


# SESSION STATE

if "messages" not in st.session_state:

    st.session_state.messages = [
        SystemMessage(
            content=personality_prompts[personality]
        )
    ]

if "personality" not in st.session_state:
    st.session_state.personality = personality


# HANDLE PERSONALITY CHANGE

if st.session_state.personality != personality:

    st.session_state.personality = personality

    st.session_state.messages = [
        SystemMessage(
            content=personality_prompts[personality]
        )
    ]


# DISPLAY CHAT HISTORY

for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):

        with st.chat_message("user"):
            st.markdown(msg.content)

    elif isinstance(msg, AIMessage):

        with st.chat_message("assistant"):
            st.markdown(msg.content)

# USER INPUT

prompt = st.chat_input(
    "Ask Nova anything..."
)

if prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Generate response
    try:

        with st.chat_message("assistant"):

            with st.spinner(
                "Nova is thinking..."
            ):

                response = chat_model.invoke(
                    st.session_state.messages
                )

                st.markdown(
                    response.content
                )

        # Save AI response
        st.session_state.messages.append(
            response
        )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )