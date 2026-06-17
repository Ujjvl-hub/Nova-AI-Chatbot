# Nova AI Chatbot 🤖

Nova is an AI-powered chatbot built using **LangChain**, **Mistral AI**, and **Streamlit**. It provides an interactive conversational experience with multiple AI personalities and conversation memory, allowing users to engage with the chatbot in different styles while maintaining context throughout the conversation.

---

## 🚀 Features

### 🎭 Multiple AI Personalities

Choose how Nova responds:

* **Normal** – Professional and informative responses
* **Funny** – Humorous and entertaining responses
* **Angry** – Aggressive and sarcastic responses
* **Sad** – Emotional and melancholic responses

### 🧠 Conversation Memory

* Maintains context during the chat session
* Remembers previous messages for more natural conversations

### 💬 Interactive Chat Interface

* Modern and user-friendly Streamlit interface
* Real-time AI-generated responses

### 🗑️ Clear Chat Functionality

* Reset conversations instantly
* Start a fresh chat session anytime

### 🔒 Secure API Key Management

* Uses environment variables to protect sensitive API keys

---

## 🛠️ Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Core Programming Language       |
| Streamlit     | Frontend User Interface         |
| LangChain     | LLM Orchestration & Memory      |
| Mistral AI    | Language Model                  |
| Python Dotenv | Environment Variable Management |

---

## 📂 Project Structure

```text
Nova-AI-Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── assets/
    └── screenshots/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ujjvl-hub/Nova-AI-Chatbot.git
cd Nova-AI-Chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
MISTRAL_API_KEY=your_api_key_here
```

### 5. Run the Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Main Chat Interface

*Add screenshot here*

### Personality Selection

*Add screenshot here*

### Memory Demonstration

*Add screenshot here*

---

## 🎯 Example Use Cases

### Normal Mode

```text
User: What is Artificial Intelligence?

Nova: Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that typically require human intelligence.
```

### Funny Mode

```text
User: What is Artificial Intelligence?

Nova: Imagine teaching a computer to think... then watching it outperform you in chess!
```

---

## 🔮 Future Improvements

* 🎤 Voice Input
* 🔊 Text-to-Speech
* 📄 PDF Chat (RAG)
* 💾 Chat Export
* 🤖 Multi-Model Support
* 🌐 Web Search Integration

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

* Large Language Models (LLMs)
* Prompt Engineering
* LangChain Framework
* AI Application Development
* Streamlit UI Development
* Conversation Memory Management
* API Integration

---

## 👨‍💻 Author

**Ujjwal**

GitHub: https://github.com/Ujjvl-hub

If you found this project interesting, consider giving it a ⭐ on GitHub.
