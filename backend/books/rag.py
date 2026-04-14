from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client()
collection = client.get_or_create_collection(name="books")

def add_book(book_id, text):
    embedding = model.encode([text])[0]
    collection.add(
        documents=[text],
        ids=[str(book_id)],
        embeddings=[embedding]
    )

def query_book(question):
    try:
        q_emb = model.encode([question])[0]
        results = collection.query(query_embeddings=[q_emb], n_results=2)
        return results.get('documents', [[]])
    except:
        return [[]]