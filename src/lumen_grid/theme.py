"""CSS variable bridge used by the Lumen Grid adapter."""


def to_css_vars(tokens: dict, prefix: str = "lumen") -> str:
    if not prefix:
        raise ValueError("prefix is required")
    return "\n".join(
        f"--{prefix}-{key.replace('_', '-')}: {value};"
        for key, value in sorted(tokens.items())
    )
