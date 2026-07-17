import math


def calculate(prompt):

    text = prompt.lower().replace("calculate", "").strip()

    try:

        if "root of" in text:

            number = float(text.replace("root of", "").strip())

            return str(math.sqrt(number))

        if "square of" in text:

            number = float(text.replace("square of", "").strip())

            return str(number ** 2)

        return str(eval(text))

    except Exception:

        return "Invalid calculation."