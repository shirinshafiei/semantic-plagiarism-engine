import os
import glob
from typing import List, Tuple, Dict


def load_documents_from_folder(folder_path: str, file_pattern: str = "*.txt") -> List[Tuple[str, str]]:
    documents = []
    pattern = os.path.join(folder_path, "**", file_pattern)
    file_paths = glob.glob(pattern, recursive=True)

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            documents.append((file_path, content))
        except Exception as e:
            pass
    return documents


def load_documents_from_paths(file_paths: List[str]) -> List[Tuple[str, str]]:
    documents = []
    for file_path in file_paths:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            documents.append((file_path, content))
        except Exception as e:
            raise Exception(f"Could not read file '{file_path}': {e}")
    return documents


def get_document_names_and_contents(folder_path: str) -> Dict[str, str]:
    docs = load_documents_from_folder(folder_path)
    result = {}
    for path, content in docs:
        name = os.path.basename(path)
        result[name] = content
    return result