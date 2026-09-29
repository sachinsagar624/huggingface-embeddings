
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = [
    "Hello this is Sachin Sagar",
    "Hello your name is funny fellow",
    "etc"
]

vector = embedding.embed_documents(text)
print("Vector length:", len(vector))

print(vector)

