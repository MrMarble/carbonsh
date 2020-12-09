import urllib.parse


def hex_to_rgb(hex: str) -> tuple:
    """
    Args:
        hex (str):
    """
    return tuple(int(hex.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))


def encode_url(text: str) -> str:
    first_encoding = urllib.parse.quote(text, safe='*()')
    return urllib.parse.quote(first_encoding, safe='*')  # Carbonsh encodes text twice


def trim_url(text: str) -> str:
    if len(text) < 2000:
        return text

    if '%25' not in text:
        return text[:2000]

    if text[:2003][:-3] == '%25':
        return text[:2000]

    last_percent = text[:2000].rindex('%25')
    return text[:last_percent]
