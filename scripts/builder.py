"""
どんなパターンか：複雑な構造を持つインスタンスを、組み立て専用の抽象クラスを使って段階的に組み上げる
いつ使うか：
何が嬉しいか：
"""


class Builder:
    """
    文書の構成要素を作るクラスのインターフェイス。サブクラスたちは文書をアトリビュートとしてもち、
    内容を渡してメソッドを呼ぶと持ってる文書に定められた書式で加筆する。
    """

    def make_title(self, title: str) -> None:
        pass

    def make_string(self, string: str) -> None:
        pass

    def make_items(self, items: list[str]) -> None:
        pass

    def close(self) -> None:
        pass


class Director:
    """
    Builderのメソッドを呼び、文書を作る。Builderインターフェイスのみに依存し、
    その実装には依存しない。
    """

    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def construct(self) -> None:
        self.builder.make_title("Greeting")
        self.builder.make_string("General greetings")
        self.builder.make_items(
            [
                "How are you?",
                "Hello.",
                "Hi.",
            ]
        )
        self.builder.make_string("Time-dependent greetings")
        self.builder.make_items(
            [
                "Good morning.",
                "Good afternoon",
                "Good evening",
            ]
        )
        self.builder.close()


class TextBuilder(Builder):
    """Make a plain text document"""

    def __init__(self) -> None:
        self.content = ""

    def make_title(self, title: str) -> None:
        self.content += "==========================================\n"
        self.content += f"【{title}】\n\n"

    def make_string(self, string: str) -> None:
        self.content += f"■ {string}\n\n"

    def make_items(self, items: list[str]) -> None:
        for item in items:
            self.content += f"* {item}\n"

    def close(self) -> None:
        self.content += "==========================================\n"

    def get_content(self) -> str:
        return self.content


class HTMLBuilder:
    """Make an HTML document"""

    def __init__(self) -> None:
        self.content = ""

    def make_title(self, title: str) -> None:
        self.content += (
            "<!DOCTYPE html>\n" "<html>\n" "<head>...</head>\n" "<body>\n"
        )
        self.content += f"<h1>{title}</h1>\n\n"

    def make_string(self, string: str) -> None:
        self.content += f"<p>{string}</p>\n\n"

    def make_items(self, items: list[str]) -> None:
        self.content += "<ul>\n"
        for item in items:
            self.content += f"  <li>{item}</li>\n"
        self.content += "</ul>\n"

    def close(self) -> None:
        self.content += "</body>\n</html>"

    def get_content(self) -> str:
        return self.content


def main():
    text_builder = TextBuilder()
    director = Director(text_builder)
    director.construct()
    print(text_builder.get_content())
    html_builder = HTMLBuilder()
    director = Director(html_builder)
    director.construct()
    print(html_builder.get_content())


if __name__ == "__main__":
    main()
