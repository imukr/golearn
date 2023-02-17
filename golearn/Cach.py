class Coins:
    '''
    :param: self._coins: tuple -> (1, 2, 5, 10, 25, 50)
    :param: self.total_sum -> 185
    :return: {50: 3, 25: 1, 10: 1, 5: 0, 2: 0, 1: 0}
    '''
    def __init__(self, total_sum):
        self._coins = (1, 2, 5, 10, 25, 50)
        self.total_sum = total_sum
    def change(self):
        result = {}
        item = len(self._coins)-1
        while item >= 0:
            value = self.total_sum//self._coins[item]
            result[self._coins[item]]=value
            self.total_sum = self.total_sum-self._coins[item]*value
            item -=1
        return result

test = Coins(185)
print(test.change())