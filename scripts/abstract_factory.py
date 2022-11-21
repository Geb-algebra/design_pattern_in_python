"""
どんなパターンか：複数の抽象的構成要素と、それを組み立てる抽象的Factoryを作り、それぞれを具象で実装する
いつ使うか：
    同じ種類 / 数の要素から同じように構成されるインスタンスが複数種あり、要素とその構成の仕方を
    抽象に分離したい時。
    そのようなインスタンスのクラスを後から増やすかもしれないとき
何が嬉しいか：
    要素と構成方法さえ同じなら、具体的実装が異なるインスタンスを作るクラスを簡単に増やせる。
"""


class Item:
    """LinkとTrayの共通スーパークラス"""

    def __init__(self, caption: str) -> None:
        self.caption = caption

    def make_html(self) -> str:
        """return an HTML-format string"""


class Link(Item):
    """HTMLリンクを生成する抽象クラス。HTML生成の実装をサブクラスで行う"""

    def __init__(self, caption: str, url: str) -> None:
        super().__init__(caption)
        self.url = url


class Tray(Item):
    """箇条書きのItemをまとめて持つ抽象クラス。HTML生成の実装をサブクラスで行う"""

    def __init__(self, caption: str) -> None:
        super().__init__(caption)
        self.tray: list[Item] = []

    def add(self, item: Item) -> None:
        self.tray.append(item)


class Page:
    """LinkとTrayから作られたページの抽象クラス。HTML生成の実装をサブクラスで行う"""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.content: list[Item] = []

    def add(self, item: Item) -> None:
        self.content.append(item)

    def output(self) -> None:
        print(self.make_html)

    def make_html(self) -> str:
        pass


class Factory:
    """Pageを組み立てる抽象クラス"""

    # 原著ではコマンドライン引数で具象クラス名を指定するために、文字列でクラス名を指定して
    # インスタンス生成していたが、今回はそこまでしないので普通にコンストラクタで作る。
    # Pythonでそれをやるのは少し面倒なのと、そこは別にAFパターンの本質ではないと思うから。

    def create_link(self, caption: str, url: str) -> Link:
        pass

    def create_tray(self, caption: str) -> Tray:
        pass

    def create_page(self, title: str, author: str) -> None:
        pass


class ListLink(Link):
    """LinkクラスのHTML生成を実装した具象クラス"""


class ListTray(Tray):
    """Tray以下略"""


class ListPage(Page):
    """Pageくらす以下略"""


def main():
    # いや長いって。電子書籍買えばよかった。
    pass


if __name__ == "__main__":
    main()
