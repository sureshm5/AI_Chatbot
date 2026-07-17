def detect_intent(message: str):

    text = message.lower()

    if text.startswith("calculate"):
        return "calculator"

    if "time" in text:
        return "time"

    if "weather" in text:
        return "weather"

    if text.startswith("summarize"):
        return "summary"

    if text.startswith("translate"):
        return "translation"

    return "chat"