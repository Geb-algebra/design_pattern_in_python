"""
どんなパターンか：
いつ使うか：
何が嬉しいか：
"""


class AbstractDisplay:
    """抽象クラス内で共通メソッドを定義しておく"""

    def open(self) -> None:
        pass

    def print(self) -> None:
        pass

    def close(self) -> None:
        pass

    def display(self) -> None:
        """抽象メソッドを使って勝利の雛形だけ作っておく"""
        self.open()
        for i in range(5):
            self.print()
        self.close()


class CharDisplay(AbstractDisplay):
    """具象化。display()は抽象クラスで作っているので実装されていない抽象メソッドだけ作る"""

    def __init__(self, char: str) -> None:
        self.char = char

    def open(self) -> None:
        print("<<", end="")

    def print(self) -> None:
        print(self.char, end="")

    def close(self) -> None:
        print(">>")


class StringDisplay(AbstractDisplay):
    def __init__(self, string: str) -> None:
        self.string = string
        self.width = len(self.string)

    def print_line(self) -> None:
        print("+" + "-" * self.width + "+")

    def open(self) -> None:
        self.print_line()

    def print(self) -> None:
        print(f"|{self.string}|")

    def close(self) -> None:
        self.print_line()


def main() -> None:
    """
    共通メソッドをAbstractで定義したことで、main()内ではAbstractDisplayのみに依存できる。
    具象に依存せず、抽象に依存するとはこういうことか。
    """
    d1: AbstractDisplay = CharDisplay("Hello")
    d2: AbstractDisplay = StringDisplay("Hello")

    d1.display()
    d2.display()


if __name__ == "__main__":
    main()
