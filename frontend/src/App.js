import { useState, useEffect } from 'react'
import axios from 'axios'

const API_BASE = process.env.REACT_APP_API_BASE_URL || 'http://127.0.0.1:8000'

function App() {
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState('')
  const [books, setBooks] = useState([])

  useEffect(() => {
    axios.get(`${API_BASE}/api/list/`).then(res => setBooks(res.data))
  }, [])

  const fetchBooks = async () => {
    await axios.get(`${API_BASE}/api/fetch/`)
    axios.get(`${API_BASE}/api/list/`).then(res => setBooks(res.data))
  }

  const ask = async () => {
    const res = await axios.post(`${API_BASE}/api/ask/`, { question })
    setAnswer(res.data.answer)
  }

  return (
    <div>
      <h1>AI Book Insight System</h1>
      <h3>Books</h3>
      <button onClick={fetchBooks}>Fetch Books</button>
      <ul>
        {books.map(b => <li key={b.id}>{b.title}</li>)}
      </ul>
      <input value={question} onChange={e => setQuestion(e.target.value)} />
      <button onClick={ask}>Ask</button>
      <p>{answer}</p>
    </div>
  )
}

export default App