import re
import nltk
from nltk.corpus import stopwords
from typing import List, Set

nltk.download('stopwords', quiet=True)
STOPWORDS = set(stopwords.words('english'))


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def tokenize_and_remove_stopwords(text: str) -> List[str]:
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 1]
    return tokens


def generate_shingles(tokens: List[str], shingle_size: int = 3) -> Set[str]:
    if len(tokens) < shingle_size:
        return set()
    shingles = set()
    for i in range(len(tokens) - shingle_size + 1):
        shingle = " ".join(tokens[i:i + shingle_size])
        shingles.add(shingle)
    return shingles


def preprocess_document(text: str, shingle_size: int = 3) -> Set[str]:
    if not text or len(text.strip()) < 10:
        return set()

    cleaned = clean_text(text)
    tokens = tokenize_and_remove_stopwords(cleaned)
    if len(tokens) < shingle_size:
        return set()

    shingles = generate_shingles(tokens, shingle_size)
    return shingles