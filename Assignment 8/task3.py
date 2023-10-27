#task 3
def minimum_coins(N, X, coins):
    arr1 = [float('inf')] * (X+1)
    arr1[0] = 0

    for coin in coins:
        for value in range(coin, X+1):
            arr1[value] = min(arr1[value], arr1[value-coin] + 1)

    if arr1[X] < float('inf'):
        return arr1[X]
    else:
        return -1

with open('input3.txt', 'r') as input_file:
    N, X = map(int, input_file.readline().split())
    coins = list(map(int, input_file.readline().split()))

    result = minimum_coins(N, X, coins)

with open('output3.txt', 'w') as output_file:
    output_file.write(str(result))