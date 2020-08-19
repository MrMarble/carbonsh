def hex_to_rgb(hex: str) -> tuple:
    """
    Args:
        hex (str):
    """
    return tuple(int(hex.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
