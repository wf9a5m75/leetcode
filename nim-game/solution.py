class Solution:
    def canWinNim(self, n: int) -> bool:
        #
        # 1 stone -> you can win
        #
        # 2 stones  -> you can also win
        #
        # 3 stones -> you can also win
        #
        # 4 stones -> you take 3 stones -> 1 stones remains -> Nim win!
        #                      2 stones -> 2 stones remain -> Nim takes 2 stones -> Nim win
        #                      1 stones -> 3 stones remain -> Nim takes 3 stones -> Nim win
        #
        # 5 stones -> you take 3 stones -> 2 stones remain -> Nim takes 2 stone -> Nim win
        #                      2 stones -> 3 stones remain -> Nim takes 3 stone -> Nim win
        #                      1 stones -> 4 stones remain -> Nim takes 3 stone -> 1 stone left -> you win
        #                                                  -> Nim takes 2 stone -> 2 stone left -> you win
        #                                                  -> Nim takes 1 stone -> 3 stone left -> you win
        # ....
        #
        # You will lose only when n % 4 == 0
        return (n % 4 != 0)
