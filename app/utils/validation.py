def normalize_title(title: str) -> str:
    """Apply the project's simple title normalization rule."""
    return " ".join(title.strip().split())
