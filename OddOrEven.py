from numpy import random

def main():
    game = True
    while game :
        print('Welcome to odd or even!')
        values = assignValues()
        checkForWinner(values)
        game = playAgain()
        if not game:
            print('Bye Bye')
#***************************************

def assignValues():
    oddOrEvenDic = {'human': '','humanNum':0, 'comp': '','compNum':0}
    # check input for odd/even
    while True:
        oddOrEvenDic['human'] = input('Human, choose odd or even ').lower()
        if oddOrEvenDic['human'] == 'odd':
            oddOrEvenDic['comp'] = 'even'
            break
        elif oddOrEvenDic['human'] == 'even':
            oddOrEvenDic['comp'] = 'odd'
            break
        else: print('you have to choose odd or even')

    print(f"Human your result will be {oddOrEvenDic['human']}, computers result will be {oddOrEvenDic['comp']}.")
    # check input for int
    while True:
        try:
            oddOrEvenDic['humanNum'] = int(input('choose number 1-100: '))
        except:
            print('invalid input , please try again')
        else:
            oddOrEvenDic['compNum'] = random.randint(1,101)
            print(f"Human your number is:  {oddOrEvenDic['humanNum']}, computers number is: {oddOrEvenDic['compNum']}.")
            break

    return oddOrEvenDic
#*************************************************

def checkForWinner(oddOrEvenDic):

    result = int(oddOrEvenDic['humanNum']) +int(oddOrEvenDic['compNum'])
    if result%2 == 0:
        print(f"The result is: {result}, even number")
        if oddOrEvenDic['human'] == 'even':
            print('Human you won!')
        else:
            print('Human you lost, computer won the game')
    else:
        print(f"The result is: {result}, odd number")
        if oddOrEvenDic['human'] == 'odd':
            print('Human you won!')
        else:
            print('Human you lost, computer won the game')
#**********************************************

def playAgain():
    game = input('play again? y/n ').lower()
    return game == 'y'
#********************************************


if __name__ == '__main__':
        main()
