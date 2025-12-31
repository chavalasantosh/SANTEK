# Weaviate Integration for SanTOK

This folder contains the Weaviate vector database integration for SanTOK embeddings.

## Setup

1. Install dependencies:
```bash
pip install weaviate-client python-dotenv
```

2. Create a `.env` file in your project root:
```
WEAVIATE_URL=your_weaviate_cluster_url
WEAVIATE_API_KEY=your_weaviate_api_key
```

## Usage

```python
from weaviate.weaviate_vector_store import WeaviateVectorStore
import numpy as np

# Initialize store
vector_store = WeaviateVectorStore(
    collection_name="SanTOK_Token",
    embedding_dim=768
)

# Add tokens (assuming you have token_records and embeddings)
vector_store.add_tokens(token_records, embeddings)

# Search
query_embedding = np.random.rand(768)  # Your query embedding
results = vector_store.search(query_embedding, top_k=10)

# Get specific embedding
embedding = vector_store.get_token_embedding("token_0")

# Always close when done
vector_store.close()
```

## Or use context manager:

```python
with WeaviateVectorStore() as vector_store:
    vector_store.add_tokens(token_records, embeddings)
    results = vector_store.search(query_embedding)
    # Automatically closes connection
```

## Notes

- Collection name defaults to "SanTOK_Token"
- Embedding dimension defaults to 768
- Credentials can be passed directly or loaded from .env file
- Connection is automatically managed

