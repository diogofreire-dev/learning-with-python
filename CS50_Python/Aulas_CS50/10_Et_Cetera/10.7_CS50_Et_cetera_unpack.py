def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "Knuts") # * unpacks the list into arguments

"""
print(total(coins[0], coins[1], coins[2]), "Knuts")
"""