def change(money):
    """

    :param money: int
    :return: tuple
    """
    Coins = (100,50,10,5,2,1)
    Result = []
    for coin in Coins:
        x = money/coin
        money = money%coin
        Result.append(x)
    return Result

if __name__ == '__main__':
    assert(change(157)==[1,1,0,1,1,0])
    assert (change(222) == [2, 0, 2, 0, 1, 0])
    assert (change(58) == [0, 1, 0, 1, 1, 1])
    assert (change(-157) == 'wrong number')

    assert (change(157.5) == change(158))
    assert (change(qwe) == 'wrong number')