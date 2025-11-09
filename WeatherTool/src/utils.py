def make_pretty_output(text):
    """
    给文本加上一个漂亮的边框
    """
    lines = text.strip().split('\n')
    width = max(len(line) for line in lines) + 4

    border = "=" * width
    pretty_text = f"\n{border}\n"
    for line in lines:
        pretty_text += f"| {line:<{width - 4}} |\n"
    pretty_text += f"{border}\n"

    return pretty_text