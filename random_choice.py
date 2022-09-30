import random


class RandomChoices:
    """
    for 文は、 [0, 1, 2, 3, 4, 5, 6, ] からランダムにひとつを取り出す。
    一度取り出された値は、二度と取り出されない。
    すべての値が取り出されたら、 StopIteration を発生させる。
    """

    def __init__(self):
        self.item_list = [0, 1, 2, 3, 4, 5, 6, ]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.item_list) == 0:
            raise StopIteration

        # self.item_list の何番目を拾ってくるかを決定する
        index = random.randint(0, len(self.item_list) - 1)

        # self.item_list の index 番目の要素を取り出す。
        # popなので、取り出された値はリストから削除される
        return self.item_list.pop(index)


if __name__ == "__main__":
    for item in RandomChoices():
        print(item)
