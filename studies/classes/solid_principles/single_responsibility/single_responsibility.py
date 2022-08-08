#!/usr/bin/env python
import json

class Page:
    def __init__(self, title):
        self._title = title

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_page(self):
        return [self._title]

class JsonPageFormatter:
    def format_json(page: Page):
        return json.dumps(page.get_page())
