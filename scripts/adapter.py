"""
どんなパターンか：
いつ使うか：
何が嬉しいか：
"""


class Banner:
    def __init__(self, string: str) -> None:
        self.string = string

    def show_with_paren(self) -> None:
        print(f"({self.string})")

    def show_with_aster(self) -> None:
        print(f"*{self.string}*")


class Print:
    def print_weak(self) -> None:
        pass

    def print_strong(self) -> None:
        pass


class PrintBanner(Banner, Print):
    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()


class PrintBannerDelegation(Print):
    def __init__(self, string: str) -> None:
        self.banner = Banner(string)

    def print_weak(self) -> None:
        self.banner.show_with_paren()

    def print_strong(self) -> None:
        self.banner.show_with_aster()


def main():
    """
    mainの中では、pbの裏で動いているBannerの実装は関係ない。
    printインターフェイスを使っているだけ。
    元々あるライブラリの機能を使いたいが要求インターフェイスがライブラリと違う時に使える。
    後でライブラリだけを変えることも可能。
    """
    pb = PrintBanner("Hello")
    pb.print_weak()
    pb.print_strong()
    pbd = PrintBannerDelegation("Hello delegation")
    pbd.print_weak()
    pbd.print_strong()


if __name__ == "__main__":
    main()
