import random

def InterpolationSearch(list, val):
    low = 0
    high = (len(list) - 1)
    while low <= high and val >= list[low] and val <= list[high]:
        index = low + int(((float(high - low) / ( list[high] - list[low])) * ( val - list[low])))
        if list[index] == val: # value found
            return index # return index of value
        if list[index] < val: # list value smaller than target value
            low = index + 1; # ignore left side
        else: # list value larger than target value
            high = index - 1; # ignore right side

    # element not found once reached here
    return -1


def insertionsort(array):

    # loops through array
    for step in range(1, len(array)):
        key = array[step] # track value of array
        j = step - 1 # track index of array

        # compare the key with each element on the left until a smaller element is found
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # key placed in array after an object smaller than it
        array[j + 1] = key


def binary_search(list1, list2):
    low = 0 # lowest value
    high = len(list1) - 1 # right more value
    mid = 0

    while low <= high:

        mid = (high + low) // 2 # middle of list

        # If x is greater
        if list1[mid] < list2:
            low = mid + 1 # ignore left half

        # If x is smaller
        elif list1[mid] > list2:
            high = mid - 1 # ignore right half

        # x is found at mid
        else:
            return mid

    # element not found once reached here
    return -1


def mystatus():

    print('<My Status>')
    userinput = int(input('Enter player ID: '))

    print('\nplayer ID: ', userinput)
    print('player numbers: ', lotto[userinput])
    print('PWNs: ', pwn)
    print('SWNs: ', swn)

    count = 0

    for i in range(0, 6): # iterate in range of players lotto numbers
        count = 0 # reset count
        result = InterpolationSearch(pwn, lotto[userinput][i]) # interpolation search added to variable called result

        if result != -1: # if result returns a match
            count += 1 # increment count

    if count == 3: # if 4th class winner
        print('Player’s status: You are a 4th class winner, congratulations!\n')


    elif count == 4: # if 3rd class winner
        print('Player’s status: You are a 3rd class winner, congratulations!\n')


    elif count == 5: # if 2nd class winner
        print('Player’s status: You are a 2nd class winner, congratulations!\n')


    elif count == 6: # if winner
        print('Player’s status: You win the game, congratulations!\n')

    else: # search through SWN

        for i in range(0, 6): # iterate in range of players lotto numbers
            count = 0 # reset count
            result = InterpolationSearch(swn, lotto[userinput][i]) # interpolation search added to variable called result

            if result != -1: # if result returns a match
                count += 1 # increment count

        if count == 2: # if 4th class winner
            print('Player’s status: You are a 4th class winner, congratulations!\n')

        else: # else not a winner
            print('Player’s status: You are not a winner. Thanks for playing lotto. Good luck next time!\n')


def stat():

    leftovers = [] # list to hold players who arent winners from PWNs

    # declare classes and count as 0
    class1 = 0
    class2 = 0
    class3 = 0
    class4 = 0
    count = 0

    for i in range(len(lotto)): # loop in range of length of lotto
        count = 0 # reset count
        for j in range(0, 6): # loop in range of players numbers
            result = binary_search(pwn, lotto[i][j]) # use binary search under result variable

            if result != -1: # if result returns a match
                count += 1 # increment count

        if count == 3: # if count value is 3
            class4 += 1 # increment class4
            count = 0 # reset count

        elif count == 4: # if count value is 4
            class3 += 1 # increment class3
            count = 0 # reset count

        elif count == 5: # if count value is 5
            class2 += 1 # increment class2
            count = 0 # reset count

        elif count == 6: # if count value is 6
            class1 += 1 # increment class1
            count = 0 # reset count

        else: # if none of the above
            leftovers.append(lotto[i]) # append players to leftovers list

    for i in range(len(leftovers)): # loop in range of length of leftovers
        count = 0 # reset count
        for j in range(0, 6): # loop in range of players numbers
            result = binary_search(swn, leftovers[i][j]) # use binary search under result variable

            if result != -1: # if result returns a match
                count += 1 # increment count

        if count == 2: # count is 2
            class4 += 1 # increment class4
            count = 0 # reset count


    print('\nClass 1 : ', class1)
    print('Class 2 : ', class2)
    print('Class 3 : ', class3)
    print('Class 4 : ', class4, '\n')

def init():

    print('player ID | Players game numbers')
    for i in range(len(lotto)): # loop in range of length of lotto
        print('   ', i, '  |  ' ,lotto[i]) # prints players id and their corresponding numbers

    print('\n<Winning Numbers>')
    print(WinNo, '\n') # prints winning numbers


def menu():
    while True:
        try:
            print("1. Show Initialissed Data")
            print("2. Display Statistics of Winners")
            print("3. Check My Lotto Status")
            print("4. Exit ")

            userinput = int(input("Select: "))

            # user redirected to init()
            if userinput == 1:
                init()

            # user redirected to stat()
            elif userinput == 2:
                stat()

            # user redirected to mystatus()
            elif userinput == 3:
                mystatus()

            # user leaves program
            elif userinput == 4:
                quit()

        except ValueError:
            print('invalid value') # error message
    menu()

# initialize lists
pwn = []
swn = []
lotto = []

for x in range(0, 1000): # loop in range of 0 to 999
    gamenum = [] # stores individual players numbers

    randints = random.sample(range(1, 30), 6) # create list of distinct numbers under randints variable
    insertionsort(randints) # sort list

    for i in range(len(randints)): # loop in range of length of randints
        gamenum.append(randints[i]) # append each individual element

    lotto.append(gamenum) # append gamenum to lotto

WinNo = random.sample(range(1, 30), 8) # create a list of distinct numbers under WinNo variable

for i in range(len(WinNo)): # loop in range of length of WinNo
    if i <= 5: # if i smaller or equal to 5
        pwn.append(WinNo[i]) # append to pwn

    elif i >= 6: # if i larger or equal to 6
        swn.append(WinNo[i]) # append to swn

# sort both pwn and swn
insertionsort(pwn)
insertionsort(swn)

menu() # begin program
