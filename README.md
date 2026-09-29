# Hugging Face Text Embeddings

This project demonstrates how to generate text embeddings using the **Hugging Face `all-MiniLM-L6-v2` model** with LangChain.

## Model

* **Model:** `sentence-transformers/all-MiniLM-L6-v2`
* **Provider:** Hugging Face / Sentence Transformers
* **Framework:** LangChain
* **Purpose:** Convert text into numerical vector representations

## Project Structure

```text id="kz8j2x"
huggingface-embeddings/
│
├── embedding.py
├── requirements.txt
└── README.md
```

## Installation

Install the required dependencies:

```bash id="p0kz5c"
pip install -r requirements.txt
```

## How It Works

The project uses LangChain's `HuggingFaceEmbeddings` to convert multiple text documents into numerical vectors.

Example:

```python id="u7q1nf"
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector = embedding.embed_documents(text)
```

The `embed_documents()` method generates an embedding vector for each text in the list.

## Example Input

```text id="r1s6km"
Hello this is Sachin Sagar
Hello your name is funny fellow
etc
```

## How to Run

Run the Python file:

```bash id="e0j4dp"
python embedding.py
```

The program prints:

1. The number of generated vectors
2. The generated embedding vectors

## Technologies Used

* Python
* LangChain
* Hugging Face
* Sentence Transformers
* `all-MiniLM-L6-v2`

## Learning Objective

This project demonstrates how to:

1. Use Hugging Face embedding models with LangChain.
2. Convert multiple text documents into numerical vectors.
3. Use `embed_documents()`.
4. Understand the concept of text embeddings.
5. Prepare embeddings for applications such as semantic search and RAG.

## Author

**Sachin Sagar**
