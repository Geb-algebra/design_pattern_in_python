"""
どんなパターンか：コンストラクタを1回しか呼出せないようにする。
いつ使うか：あるクラスのインスタンスを1つしか生成しないように縛りたいとき
何が嬉しいか：プログラム側で厳密に縛れるため実装ミスがない。
"""

from __future__ import annotations


# pythonではコンストラクタをプライベートにできないため
# https://www.denzow.me/entry/2018/01/28/171416
# を参考に少しトリッキーな実装をする


class Singleton:
    _unique_instance: Singleton | None = None

    def __new__(cls):
        # 外部からコンストラクタが呼ばれたときはエラー
        raise NotImplementedError(
            "Instantiation via constructor is not allowed"
        )

    @classmethod
    def __internal_new__(cls):
        # 内部からこいつを明示的に呼ぶことで、__new__で定義したエラーを回避してインスタンス生成
        super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if cls._unique_instance is not None:
            cls._unique_instance = cls.__internal_new__()
        return cls._unique_instance


def main():
    a = Singleton.get_instance()  # インスタンス生成
    b = Singleton.get_instance()  # 複数回インスタンス生成メソッドを読んでも、同じメモリ上のインスタンスが返される。
    if a is b:
        print("a and b is identical.")
    x = Singleton()  # エラー


if __name__ == "__main__":
    main()
