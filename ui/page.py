from jinja2 import Template
from typing import Tuple
from os.path import dirname, join

import __main__
from .style import Style


class Page:
    def __init__(
        self, 
        *objs: Tuple[object], 
        title: str = "Document", 
        charset: str = "utf-8", 
        lang: str = "en", 
        style: Style = Style()
    ) -> None:
        (
            self.objs, 
            self.title, 
            self.charset, 
            self.lang, 
            self.style
        ) = (
            objs, 
            title, 
            charset, 
            lang, 
            style
        )

    def __str__(self) -> str:
        with open(join(dirname(__main__.__file__), "templates/page.jinja"), "r") as f:
            template = Template(f.read())
        
        return template.render({
            "lang": self.lang,
            "title": self.title,
            "charset": self.charset,
            "objs": "".join([str(obj) for obj in self.objs]),
            "style": self.style
        })
    