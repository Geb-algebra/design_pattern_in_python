"""
どんなパターンか：
    ある問題を解く (状態や設定を入力して、答えを受け取りたい) とき、
    問題の入力と答えの出力のみを定めるAPIを作り、中の解法をそのAPIに沿って実装する。
いつ使うか：
    ある問題に対して、複数の解法を使い分けたい時
何が嬉しいか：
    問題を解き答えを利用するプログラムから求解プログラムを分離することができる。
    問題の答えを扱うプログラム上から、実装を変えずに好きな解法を選択できる。
"""

# 実装はテキストのコードが多かったのと、研究でのアルゴリズム実装で既にやってたのでパス。

class Strategy:
    def next_hand(self):
        pass

    def study(self):
        pass

    
class WinningStrategy(Strategy):
    def next_hand(self):


class Player:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy
        
    def next_hand(self):
        


def main():
    pass


if __name__ == "__main__":
    main()
