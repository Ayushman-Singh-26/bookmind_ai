from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .rag import add_book, query_book
import requests


@api_view(['GET'])
def fetch_books(request):
    try:
        url = "https://www.googleapis.com/books/v1/volumes?q=artificial intelligence"
        data = requests.get(url).json()

        for item in data.get('items', []):
            info = item.get('volumeInfo', {})
            desc = info.get('description', '')

            if not desc:
                continue

            book, created = Book.objects.get_or_create(
                title=info.get('title', ''),
                defaults={
                    "authors": ",".join(info.get('authors', [])),
                    "description": desc
                }
            )

            if created:
                add_book(book.id, desc)

        return Response({"status": "books added without duplicates"})

    except Exception as e:
        return Response({"error": str(e)})


@api_view(['GET'])
def list_books(request):
    try:
        books = Book.objects.all().values()
        return Response(list(books))
    except Exception as e:
        return Response({"error": str(e)})


@api_view(['POST'])
def ask(request):
    try:
        question = request.data.get('question')

        if not question:
            return Response({"error": "No question provided"})

        docs = query_book(question)

        if not docs or not docs[0]:
            return Response({
                "answer": f"I couldn't find exact info in books for '{question}', but it's an important AI topic."
            })

        context = " ".join(docs[0])

        return Response({
            "answer": context
        })

    except Exception as e:
        return Response({"error": str(e)})