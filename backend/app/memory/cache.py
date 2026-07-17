CACHE = {}


def normalize(text: str):
    return text.lower().strip()


def get_cache(question: str):

    return CACHE.get(normalize(question))


def save_cache(question: str, answer: str):

    CACHE[normalize(question)] = answer


def clear_cache():

    CACHE.clear()


def cache_size():

    return len(CACHE)