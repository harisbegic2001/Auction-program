print("Welcome to silent auction program")
name_list = []
bid_list = []
copy = []
while True:
    name = input("What's your name: ")
    bid = int(input("What's your bid: $"))
    
    name_list.append(name)
    bid_list.append(bid)
    copy.append(bid)

    biders = input("Are there any more biders? (type \"yes\" or \"no\") ").lower()
    if biders == "yes":
        continue
    else:
        break

bid_list.sort()
winner = bid_list[-1]
lista = []
for i in range(len(copy)):
    if copy[i] == winner:
        lista.append(i)

winner_name = name_list[lista[0]]

print(f"The winner is {winner_name} with the bid of {winner}")
