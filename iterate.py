import random

SUSHI_NETA_LIST = [
    {"name": "マグロ赤身", "price": 100},
    {"name": "えんがわ", "price": 100},
    {"name": "中トロ", "price": 200},
    {"name": "いくら", "price": 200},
    {"name": "大トロ", "price": 300},
    {"name": "うなぎ", "price": 300},
    {"name": "うに", "price": 400},
    {"name": "車エビ", "price": 400},
]


class Itamae:
    def show_ordered_list(self):
        """
        握ったネタのリストを返す
        """
        _ordered_list = [f'{order["name"]} {order["price"]}円' for order in self.ordered_list]
        total = sum([order["price"] for order in self.ordered_list])
        _ordered_list.append(f'合計 {total}円')
        return '\n'.join(['本日のお会計は以下の通りです。'] + _ordered_list)

    def __init__(self, money, neta_list):
        print(f"{money:,}円の中で何か握ります。")
        self.money = money
        self.neta_list = neta_list
        self.ordered_list = []

    def __iter__(self):
        return self

    def __next__(self):
        # 残金内で握れるネタのリストを作る
        # 以下の[1], [2]どちらでも行けるが、[1]のほうが読みやすいか。
        _neta_list = [n for n in self.neta_list if n["price"] <= self.money]  # [1]
        # _neta = list(filter(lambda n: n["price"] <= self.money, self.neta))  # [2]

        # 以下のような例外を先に扱う処理のほうが個人的には好み。(インデントされたブロックが減るから)
        if len(_neta_list) == 0:
            # 残金内で握れそうなネタがない場合はおしまい。
            print("もう握れません。\n")
            raise StopIteration

        # 残金内で握れそうなら何か握る
        nigiri = random.choice(_neta_list)  # 可能な範囲からネタをひとつ握る
        self.money -= nigiri["price"]  # 預かり金から代金を引く
        self.ordered_list.append(nigiri)  # 握ったネタをリストに追加する
        return f'{nigiri["name"]} を握って出しました'  # 握りを客に出す


# 板前さんにお金を渡すとお任せで握ってくれる。お金がなくなったら終了。
okane = 1560
itamae = Itamae(okane, SUSHI_NETA_LIST)
for sushi in itamae:
    print(sushi)

ordered_list = itamae.show_ordered_list()
print(ordered_list)
