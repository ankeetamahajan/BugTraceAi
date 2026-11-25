
import os
from pathlib import Path

from dotenv import load_dotenv


# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")


# Hugging Face configuration
HF_TOKEN = os.getenv("HF_TOKEN", "")
HF_MODEL_ID = os.getenv("HF_MODEL_ID", "")


# Embedding and reranking models
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

RERANKER_MODEL = os.getenv(
    "RERANKER_MODEL",
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


# Data directory
DATA_DIR = BASE_DIR / "data"


# Vector database configuration
CHROMA_DIR = BASE_DIR / os.getenv(
    "CHROMA_DIR",
    "chroma_db"
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "bugtrace_knowledge"
)


# Retrieval configuration
TOP_K = int(os.getenv("TOP_K", "5"))
CANDIDATE_K = int(os.getenv("CANDIDATE_K", "15"))


# Backend configuration
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8000"))


# Neo4j configuration
NEO4J_URI = os.getenv(
    "NEO4J_URI",
    "bolt://localhost:7687"
)

NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "")


def validate_config():
    """Validate application configuration."""

    if TOP_K <= 0:
        raise ValueError("TOP_K must be greater than zero.")

    if CANDIDATE_K < TOP_K:
        raise ValueError(
            "CANDIDATE_K must be greater than or equal to TOP_K."
        )

    if not 1 <= API_PORT <= 65535:
        raise ValueError("Invalid API port.")

    if not DATA_DIR.is_dir():
        raise ValueError("Data directory does not exist.")

    return True


if __name__ == "__main__":

    validate_config()

    print("=" * 50)
    print("BugTrace AI - Configuration Check")
    print("=" * 50)

    print("Project directory:", BASE_DIR)
    print("Data directory:", DATA_DIR)
    print("Embedding model:", EMBEDDING_MODEL)
    print("Reranker model:", RERANKER_MODEL)
    print("Vector database:", CHROMA_DIR)
    print("Collection:", COLLECTION_NAME)
    print("Top K:", TOP_K)
    print("Candidate K:", CANDIDATE_K)
    print("API host:", API_HOST)
    print("API port:", API_PORT)

    print(
        "Hugging Face token:",
        "Configured" if HF_TOKEN else "Not configured"
    )

    print(
        "LLM model:",
        HF_MODEL_ID or "Not selected yet"
    )

    print("=" * 50)
    print("Configuration validated successfully.")
