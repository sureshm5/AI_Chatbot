import faiss
import numpy as np

index = faiss.IndexFlatL2(384)

documents = []


def add_vectors(vectors, chunks):

    global documents

    vectors = np.array(vectors).astype("float32")

    index.add(vectors)

    documents.extend(chunks)


def has_documents():

    return len(documents) > 0


def search(vector, k=3):

    if len(documents) == 0:
        return []

    vector = np.array([vector]).astype("float32")

    D, I = index.search(vector, min(k, len(documents)))

    results = []

    for idx in I[0]:

        if idx != -1 and idx < len(documents):

            results.append(documents[idx])

    return results