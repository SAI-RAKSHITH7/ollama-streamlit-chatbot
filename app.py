import streamlit as st
import ollama

# Configure page settings
st.set_page_config(
    page_title="AI Chatbot with Ollama",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Local AI Chatbot")
st.caption("Powered by Ollama & Streamlit")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Check Ollama connection and list models
    try:
        models_info = ollama.list()
        # In newer ollama-python versions, models is a list of Model objects
        model_names = [m.model for m in models_info.models] if hasattr(models_info, "models") else [m["name"] for m in models_info.get("models", [])]
        if not model_names:
            model_names = ["llama3.2:1b"]
        st.success("Ollama is Connected ✅")
    except Exception as e:
        model_names = ["llama3.2:1b"]
        st.warning(f"Ollama check: {e}")

    selected_model = st.selectbox("Select Model", model_names, index=0)
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown(
        "This is a lightweight AI chatbot running entirely locally on your system using **Ollama** and **Streamlit**."
    )
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your local AI assistant running offline with Ollama. Ask me anything!"}
    ]

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User prompt input
if prompt := st.chat_input("Type your question or prompt here..."):
    # Append user prompt
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        try:
            # Stream response from Ollama
            stream = ollama.chat(
                model=selected_model,
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True,
            )
            for chunk in stream:
                content = chunk.message.content if hasattr(chunk, "message") else chunk["message"]["content"]
                full_response += content
                response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)
        except Exception as err:
            full_response = f"⚠️ Error communicating with Ollama: {err}"
            response_placeholder.error(full_response)
            
    # Append assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
