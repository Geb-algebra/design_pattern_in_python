"""
どんなパターンか：インスタンスの生成方法を特定のクラスの実装から分離する
いつ使うか：インスタンスの生成方法だけ使いまわしたい時 / インスタンス生成方法だけに依存する他のモジュールがある時？
何が嬉しいか：生成方法だけ決めた抽象クラスに依存し、具象クラスに依存しない実装ができる。
"""


class Product:
    def use(self):
        pass


class Factory:
    def create(self, owner: str):
        p: Product = self.create_product(owner)
        self.register_product(p)
        return p

    def create_product(self, owner: str):
        pass

    def register_product(self, product: Product):
        pass


class IDCard(Product):
    def __init__(self, owner: str) -> None:
        print(f"Issue {owner}'s card")
        self.owner = owner

    def use(self):
        print(f"Use {self.owner}'s card")

    def __str__(self) -> str:
        return f"[IDCard: {self.owner}]"


class IDCardFactory(Factory):
    def create_product(self, owner: str):
        return IDCard(owner)

    def register_product(self, product: Product):
        print(f"registered {product}")


def main():
    employees = ["Alice", "Bob", "Carol"]
    factory = IDCardFactory()
    for e in employees:
        # この実装はFactoryのみに依存し、IDCardFactoryの実装には依存しない。
        card = factory.create_product(e)
        card.use()  # ついでにこれも抽象に依存


if __name__ == "__main__":
    main()
