"""
どんなパターンか：
いつ使うか：クラスを使って0からインスタンスを作るのが難しく、他のインスタンスをコピーする方が早い時
何が嬉しいか：
    似たようで少し違うインスタンスが無数に欲しい時に、いちいちクラスを別々に定義しなくて良い
    クラス名を文字列などで指定できるため、抽象のコードにクラス名を書かずに済む
"""


import copy


class Product:
    def use(self):
        pass

    def create_copy(self):
        """return a copy of the instance itself."""
        pass


class Manager:
    """Stores instances as prototypes and makes copies of them"""

    def __init__(self) -> None:
        self.showcase: dict[str, Product] = {}

    def register(self, name: str, prototype: Product) -> None:
        self.showcase[name] = prototype

    def create(self, name: str) -> Product:
        # インスタンスのコピーによって新規インスタンスを生成することで、
        # Managerクラスは作るべき具象クラスに依存しない。
        proto = self.showcase[name]
        return proto.create_copy()


class MessageBox(Product):
    """Display the given string surrounded by registered characters

    Attributes:
        deco_string (string): The character which is used to surround
    """

    def __init__(self, deco_string: str) -> None:
        self.deco_string = deco_string

    def use(self, content: str):
        """Display the given string surrounded by registered characters

        Args:
            content (str): The string printed
        """
        d = self.deco_string
        width = len(content) + 2
        print(d * width)
        print(f"{d}{content}{d}")
        print(d * width)

    def create_copy(self):
        return copy.deepcopy(self)


class UnderlinePen(Product):
    def use(self, content: str):
        length = len(content)
        print(content)
        print("-" * length)

    def create_copy(self):
        return copy.deepcopy(self)


def main():
    manager = Manager()
    # 囲み文字だけが違う2種類のboxを作る時に、prototypeパターンなら
    # 別々のクラスにする必要がない。コードを減らせる。
    manager.register("slash_box", MessageBox("/"))
    manager.register("aster_box", MessageBox("*"))
    manager.register("ul_pen", UnderlinePen())
    s_box = manager.create("slash_box")
    s_box.use("Hello")
    a_box = manager.create("aster_box")
    a_box.use("Hello")
    ulpen = manager.create("ul_pen")
    ulpen.use("Hello")


if __name__ == "__main__":
    main()
