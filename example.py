from flask import Flask

from ui import Page, Paragraph, Style, Text

app = Flask(__name__)


@app.route("/")
def index():
    return str(Page(
        Paragraph(
            content="Hello world!",
            style=Style(
                ("font-size", "26px"),
                ("margin", "0")
            )
        ),
        Text(
            content="This is an hello world page"
        ),
        style=Style(
            ("font", "13px 'Fira Sans', sans-serif"),
        ),
        title="Hello world!"
    ))


app.run(port=8080)
