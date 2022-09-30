import random

SUSHI_NETA = [
    {"name": "マグロ赤身", "price": 100},
    {"name": "えんがわ", "price": 100},
    {"name": "中トロ", "price": 200},
    {"name": "いくら", "price": 200},
    {"name": "大トロ", "price": 300},
    {"name": "うなぎ", "price": 300},
    {"name": "うに", "price": 400},
    {"name": "車エビ", "price": 400},
]
prices = {price["price"] for price in SUSHI_NETA}


class Itamae:
    def __init__(self, money):
        print(f"{money:,}円の中で何か握ります。")
        self.money = money

    def __iter__(self):
        return self

    def __next__(self):
        # 代金内で握れそうなら何か握る
        if self.money > min(prices):
            # とりあえず何か握る
            nigiri = random.choice(SUSHI_NETA)

            # 残高不足なら違うものを握る
            while self.money < nigiri["price"]:
                nigiri = random.choice(SUSHI_NETA)

            # 預かり金から代金を引く
            self.money -= nigiri["price"]

            # 握りを客に渡す
            return nigiri

        # 残金で握れるものがなくなったらおしまい。
        else:
            print("もう握れません。")
            raise StopIteration


# 板前さんにお金を渡すとお任せで握ってくれる。お金がなくなったら終了。
okane = 1560
itamae = Itamae(okane)
for sushi in itamae:
    print(f'{sushi["name"]}は{sushi["price"]}円。残金は{itamae.money}円')
