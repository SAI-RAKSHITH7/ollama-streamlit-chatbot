# Local AI Chatbot with Ollama & Streamlit 🤖

A beginner-friendly AI chatbot running entirely locally using [Ollama](https://ollama.com) as the local model engine and [Streamlit](https://streamlit.io) for the interactive web user interface.

## Features
- **100% Local & Offline**: Powered by local Ollama model (`llama3.2:1b`), with zero external API fees or data sharing.
- **Interactive UI**: Real-time streaming chat messages, conversation history, and quick clear-chat feature.
- **Model Switcher**: Dynamic dropdown in sidebar showing connected models.
- **High Performance**: Accelerated with local GPU inference.

## Prerequisites
- **Python**: 3.10+
- **Ollama**: Installed and running on your system.

## Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/SAI-RAKSHITH7/ollama-streamlit-chatbot.git
cd ollama-streamlit-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Ensure Ollama is running and has the model
```bash
ollama pull llama3.2:1b
```

### 4. Run the Streamlit application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.
