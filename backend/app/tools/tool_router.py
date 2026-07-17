from app.tools.calculator import calculate
from app.tools.time_tool import current_time
from app.tools.weather import get_weather


def run_tool(prompt: str):

    text = prompt.lower()

    if text.startswith("calculate"):

        return calculate(text)

    if "time" in text:

        return current_time()

    if "weather" in text:

        return get_weather()

    return None