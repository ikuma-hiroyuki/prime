"""
2から指定された値を超えない最大の値までの素数を順番に出力する。
"""


class PrimeGenerator:
    def __init__(self, num_limit):
        """
        初期値を設定する

        :param num_limit: 最大値。この値を超えない範囲で素数を出力する。
                          この値に到達したらStopIterationを発生させる。

        self.num_limit  : 素数を探す範囲の上限値を設定する。
        self.prime_list : 既に見つけた素数のリストを格納する。
                          検査対象の自然数 n このリスト内のどの要素でも割り切れなかったら素数。
                          そのときは、その自然数 n を __next__() の戻り値として返す。
                          そして、このリストにその自然数 n を追加する。
        self.current    : 現在の探索位置を設定する。
        """
        self.num_limit = num_limit
        self.prime_list = []
        self.current = 2

    def __iter__(self):
        """
        このクラスのインスタンスをイテレータとして扱うためのメソッド。
        自分自身が __next__ を持っているので、自分自身を返す。
        """
        return self

    def is_prime(self, num):
        """
        指定された自然数が素数かどうかを判定する。

        :param num: 判定対象の自然数。2より大きいという前提。
        :return: 素数なら True、合成数なら False
        """
        for prime in self.prime_list:
            if num % prime == 0:
                return False
        return True

    def __next__(self):
        """
        このメソッドが呼ばれると、 self.current の次の自然数から、順番に素数を探していく。
        素数を見つけたら、 self.current を更新して、その素数を返す。
        ただし、 self.num_limit に到達したら、 StopIteration を発生させる。

        :return: 次の素数。
        """
        while not self.is_prime(self.current):
            if self.current > self.num_limit:  # 最大値を超えたら終了
                raise StopIteration
            self.current += 1

        self.prime_list.append(self.current)
        self.current += 1
        return self.prime_list[-1]


if __name__ == '__main__':
    num_limit = 100000
    prime_generator = PrimeGenerator(num_limit)
    for prime in prime_generator:
        print(prime)
