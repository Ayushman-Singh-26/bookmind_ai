# 📚 BookMind AI – Intelligent Book Insight Platform

A full-stack AI-powered document intelligence platform that collects, processes, and analyzes book data using Retrieval-Augmented Generation (RAG). The system enables users to explore books, generate insights, and ask intelligent questions.

---

## 🚀 Features

- 📖 Automated book data collection (Google Books API)
- 🧠 AI-powered insights (Summaries, recommendations)
- ❓ Question Answering using RAG pipeline
- 🔍 Semantic search using embeddings
- 🌐 REST APIs for core functionalities
- 💻 React frontend with Tailwind CSS

---

## 🏗️ Tech Stack

### Backend
- Python 3.13+
- Django REST Framework
- SQLite3 (metadata storage)
- ChromaDB (vector database)

### Frontend
- React.js
- Tailwind CSS
- Axios

### AI Integration
- Sentence Transformers (all-MiniLM-L6-v2)
- RAG pipeline for Q&A
- Support for OpenAI API / LM Studio

### Data Source
- Google Books API

---

## 🔗 API Endpoints

### GET APIs
| Endpoint | Description |
|----------|-------------|
| `GET /api/list/` | List all books |

### POST APIs
| Endpoint | Description |
|----------|-------------|
| `POST /api/ask/` | Ask questions about books |

#### Example Request:
```json
{
  "question": "What is artificial intelligence?"
}
Example Response:
json
{
  "answer": "Artificial Intelligence (AI) is the simulation of human intelligence in machines."
}
🤖 AI Features Implemented
✅ Question Answering (RAG Pipeline)

✅ Semantic Search with Embeddings

🔄 Book Summaries (via RAG)

🔄 Recommendations (via RAG)

🛠️ Setup Instructions
1. Clone Repository
bash
git clone https://github.com/Ayushman-Singh-26/bookmind_ai.git
cd bookmind_ai
2. Backend Setup
bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
3. Frontend Setup
bash
cd frontend
npm install
npm start
4. Load Books
Visit http://localhost:8000/api/fetch/ to fetch books from Google Books API

📸 Screenshots
https://./screenshots/dashboard.png
https://./screenshots/qa.png

💬 Sample Questions & Answers
Q: What is artificial intelligence?
A: Artificial Intelligence (AI) is the simulation of human intelligence in machines. Key topics include machine learning, neural networks, and natural language processing.

Q: Recommend similar books
A: Based on your interest in AI, I recommend 'Artificial Intelligence: A Modern Approach' and 'Artificial Intelligence Basics'.

Q: What is machine learning?
A: Machine Learning is a subset of AI that enables systems to learn from data.

📂 Project Structure
text
bookmind_ai/
├── backend/
│   ├── books/
│   ├── db.sqlite3
│   └── manage.py
├── frontend/
│   └── src/
├── screenshots/
├── README.md
└── requirements.txt
🧪 Testing
bash
# List books
curl http://localhost:8000/api/list/

# Ask a question
curl -X POST http://localhost:8000/api/ask/ \
  -H "Content-Type: application/json" \
  -d "{\"question\": \"What is AI?\"}"
👨‍💻 Author
Ayushman Singh
GitHub: https://github.com/Ayushman-Singh-26
⭐ Final Note
This project demonstrates a full-stack AI application using RAG, combining backend APIs, frontend UI, and intelligent data processing for book insights.

