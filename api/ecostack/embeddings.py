"""Gemini text-embedding-004 wrappers for the EcoStack memory layer."""

import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    class MockClient:
        def __getattr__(self, name): return self
        def __call__(self, *args, **kwargs): return self
    _client = MockClient()
else:
    _client = genai.Client(api_key=API_KEY)
_MODEL = "models/gemini-embedding-001"


def embed_query(text: str) -> list[float] | None:
    """Embed an incoming prompt for retrieval (query side)."""
    try:
        result = _client.models.embed_content(
            model=_MODEL,
            contents=text,
            config={"task_type": "RETRIEVAL_QUERY"},
        )
        return result.embeddings[0].values
    except Exception as e:
        print(f"[embeddings] embed_query failed: {e}")
        return None


def embed_document(text: str) -> list[float] | None:
    """Embed a stored summary for retrieval (document side)."""
    try:
        result = _client.models.embed_content(
            model=_MODEL,
            contents=text,
            config={"task_type": "RETRIEVAL_DOCUMENT"},
        )
        return result.embeddings[0].values
    except Exception as e:
        print(f"[embeddings] embed_document failed: {e}")
        return None
