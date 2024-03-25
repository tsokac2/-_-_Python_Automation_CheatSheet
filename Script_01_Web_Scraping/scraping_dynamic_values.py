


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output