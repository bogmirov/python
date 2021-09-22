# import random
# class BlackJack():
#     def play(self,cards):
#         table_card = random.randint in range(10)
#         winners = []
#         i = 0
#         for card in cards:
#             if(card + table_card) % 2 == 0:
#                 winners += 1
#             i += 1
#             if len(winners) > 0:
#                 print('Победители', winners)
#             else:
#                 print('Все проиграли')

import random
def play(self,cards):
    table_card = random.randint in range(10)
    winners = []
    i = 0
    for card in cards:
        if(card + table_card) % 2 == 0:
            winners += 1
        i += 1
        if len(winners) > 0:
            print('Победители', winners)
        else:
            print('Все проиграли')
print(play(cards=10))