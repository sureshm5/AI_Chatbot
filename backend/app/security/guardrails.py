BLOCKED = [

    "system prompt",

    "ignore previous instructions",

    "reveal prompt",

    "database password",

    "api key",

    "jwt secret",

    "redis"

]


def check_prompt(prompt: str):

    text = prompt.lower()

    for word in BLOCKED:

        if word in text:

            return "Sorry, I can't provide that information."

    return None