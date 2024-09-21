### While Loops:
# flag = True

# while flag == True:
#     print("Check")
#     break #Breaking the infinte loop


# i = 1

# while i <= 10:
#     print(i)
#     i += 2
#     i **= 2 # why this is not infinitly looping? -> beacause printing 3rd time will be i = 11^2
# print("Done")

# i = 1

# while i <= 5:
#     print('*' * i)
#     i += 1

### For Loops:

#Lets say we want to print 1 to 20
# for i in range(1,21): #Why we took the range upto 21?
#     print(i)

items = ['burger', 'egg', 'pizza', 'Cheese', 'cake']

#Lets say we want to print the lenth of the list:
# for i in range(len(items)):
#     print(i)  # i == index number.

#Lets say we want to print all the items in the list
# for i in items: # i == iterate variable.
#     print(i)

#Lets say we want to count all the items
# count = 0
# for i in items:
#     count += 1
# print(count)

#Lets say we want to print all the items in the list in reverse order
# for i in reversed(items):
#     print(i)

#Lets say we want to print an item that starts with character 'c'
# for i in items:
#     if i[0].lower() == 'b':  # Check if the first character is 'c' (case-insensitive), why?
#         print(i)


# account_number = False
# credit_scores = 100

# if account_number == True:
#     if credit_scores >= 60:
#         print("You qualify for the loan.")
#     else:
#         print("Sorry, you do not meet the credit score requirement.")