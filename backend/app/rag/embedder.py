from sentence_transformers import SentenceTransformer

model = None


def get_model():

    global model

    if model is None:

        model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return model


def embed(chunks):

    return get_model().encode(chunks)