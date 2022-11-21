"""
どんなパターンか：
    ある抽象クラスを、具象クラス作成のための抽象クラス (実装クラス) と、機能拡張ように継承するための抽象クラス (機能クラス) に
    分離し、両者をつなぐ...
いつ使うか：抽象クラスを作って具象クラスで実装 + 抽象クラスの機能拡張のための抽象クラス継承 を同時にやりたいとき
何が嬉しいか：
"""


class DisplayImpl:
    """実装に使う抽象クラス。実装のAPIを決めておき、機能の抽象クラスでこれを使って機能を作る。"""

    def raw_open(self) -> None:
        pass

    def raw_print(self) -> None:
        pass

    def raw_close(self) -> None:
        pass


class StringDisplayImpl(DisplayImpl):
    """DisplayImplの実装。"""

    def __init__(self, string: str):
        self.string = string

    @property
    def width(self):
        return len(self.string)

    def print_line(self) -> None:
        print("+" + "-" * self.width + "+")

    def raw_open(self) -> None:
        self.print_line()

    def raw_print(self):
        print(f"|{self.string}|")

    def raw_close(self) -> None:
        self.print_line()


class Display:
    """
    機能拡張に使う抽象クラス。DisplayImplのサブクラスを保持し、抽象クラスDisplayImplで
    定めたAPIを使って機能を作る。
    DisplayImplを継承せず、移譲で
    """

    def __init__(self, impl: DisplayImpl):
        self._impl = impl

    def open(self) -> None:
        self._impl.raw_open()

    def print(self) -> None:
        self._impl.raw_print()

    def close(self) -> None:
        self._impl.raw_close()

    def display(self) -> None:
        self.open()
        self.print()
        self.close()


class DisplayExtend(DisplayImpl):
    """
    移譲ではなく継承で機能のくらすを作ったらどうなるか考えてみた。
    これでも実装はできるが、raw_openなどを具体的に実装するStringDisplayImplを作るときは
    このくらすを継承する必要がある。
    そのため、このクラスを継承して機能拡張した抽象クラスを作ったとき、その拡張機能を使うためには
    新しくその拡張クラスを継承したStringDisplayImplを作り直さなければならない。
    言い換えると、継承は1対多の関係しか作れないが、移譲なら多対多の関係を作れる。
    """

    def open(self):
        self.raw_open()

    def print(self):
        self.raw_print()

    def close(self):
        self.raw_close()

    def display(self) -> None:
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):
    """
    Displayの機能を拡張した抽象クラス。DisplayImplのAPIを使うかぎり、DisplayImplの
    サブクラスによる実装は気にせず機能拡張が可能。
    DisplayImplのサブクラスも、Displayのサブクラス全てを使うことが可能。
    """

    def multi_display(self, times: int) -> None:
        self.open()
        for _ in range(times):
            self.print()
        self.close()


def main():
    d1 = Display(StringDisplayImpl("Hello, World"))
    d2 = CountDisplay(StringDisplayImpl("Hello, World"))

    d1.display()
    d2.display()
    d2.multi_display(5)


if __name__ == "__main__":
    main()
