# A simple program for calculating price for books during a special offer

books = int(input())  # input number of books
prices = []  # empty list for the books' prices

for book in range(books): 
    price = int(input())  # for as many books, input their price
    prices.append(price)  # the books' prices append to the prices list

total = 0  # initialize a variable called total
prices.sort()  # sorting of the prices list
group = []  # empty list for groups of books

while prices:
    price = prices.pop() 
    group.append(price)  # remove a book from the prices list, add it to the group
    if len(group) == 3:  
        total += sum(group) - min(group)
        group = []  # if the group has three books (prices), update the total price and make a new group

if 0 < len(group):
    total += sum(group)
    group = []  

print(total)  # print the total price to the console 