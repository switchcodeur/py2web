from dataclasses import dataclass

from .style import Style


@dataclass
class Paragraph:
    content: str
    style: Style = Style()

    def __str__(self) -> str:
        content = self.content.replace("\n", "<br>")

        return f"<p style={str(self.style)}>{content}</p>"


@dataclass
class Text:
    content: str
    inline: bool = True

    def __str__(self) -> str:
        inline = "" if self.inline else "<br>"
        content = self.content.replace("\n", "<br>")

        return f"{inline}{content}"
    