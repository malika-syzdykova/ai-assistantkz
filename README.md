# 🇰🇿 AI Constitution Assistant (Kazakhstan)

This project is an AI-powered assistant built with **Streamlit**, **LangChain**, and **OpenAI GPT-4**, capable of answering questions about the **Constitution of the Republic of Kazakhstan**.

---

## 🚀 Features

- Upload and analyze any PDF version of the Constitution
- Ask natural language questions (e.g. "What does Article 2 say?")
- Uses GPT-4 for extended context (up to 128K tokens)
- Optimized to reduce API usage cost with chunking and retrieval limits

---

## 📂 Project Structure

```
ai-assistant/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env.example         # Template for environment variables
├── README.md            # This file
└── db/                  # Vector store (auto-created, gitignored)
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/ai-assistantkz.git
cd ai-assistantkz
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add OpenAI API key

Create a file named `.env` in the root of the project:

```
OPENAI_API_KEY=your-key-here
```

---

## ▶️ Run the assistant

```
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 💸 Cost Control (Important)

If you're using GPT-4 (`gpt-4-1106-preview`), it's expensive. To reduce costs:

- Limit chunk size: `chunk_size=300`
- Use top K documents: `search_kwargs={"k": 2}`
- Set `max_tokens=800` for shorter responses

You can change these settings in `app.py`.

---

## 📄 Example Questions

- What is stated in Article 1?
- What rights are guaranteed to citizens?
- How is the Parliament structured?
- What powers does the President have?

---

## 🧠 Made by

Developed by Malika Syzdykova | Astana IT University  
Group: SE-2322

