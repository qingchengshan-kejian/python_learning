import collections

# 创建具名元组
# typename是Card
# 有两个字段，一个字段是rank, 一个字段是suit
Card = collections.namedtuple('Card', ['rank', 'suit'])

# 这一副牌是不具备洗牌功能的
# self._cards是顺序是固定的
# 11章，使用__setitem__实现洗牌
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # 一个数组，数组的元素是一个一个的Card
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# beer_card = Card('7', 'diamonds')
# print(beer_card)

deck = FrenchDeck()
# print(len(deck))
# print(deck[0])

# from random import choice
# choice作用于一个序列的函数，随机返回序列中的一个元素
# print(choice(deck))

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
# print(len(suit_values))
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# 类的属性可以直接使用
# print(FrenchDeck.ranks)

for card in sorted(deck, key=spades_high):
    # 直接变成一个可迭代对象了
    # deck并不是一个可迭代对象，只是因为有__getitem__方法，可以用[]索引
    # key是一个函数，作用在每一个deck中的元素（__getitem__方法获取的元素）的
    print(card)


# 自定义的类通过使用魔术方法，使得具有python通用对象的方法。


