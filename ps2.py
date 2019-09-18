
#.......Problem2.........
print("Welcome to the Game!")
board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]
player = '1' #with this we'll know which player's turn it is

def tic_tac_toe ():
    print ('|' ,board[0],'|',board[1] ,'|', board[2],'|')
    print ('--------------------')
    print ('|' ,board[3],'|',board[4] ,'|', board[5],'|')
    print ('--------------------')
    print ('|' ,board[6],'|',board[7] ,'|', board[8],'|')

def move(x1,x2):
    board[x2] = x1
    tic_tac_toe()

def odd (x, x2):
    while  (x%2==0):
        x = int(input ('enter an odd number'))
    #Nothing here because if we get out of the while is because it's a valid number (we're not checking numbers out of range or anything)
    move (x ,x2)      

def even (x ,x2) :
    while  (x%2!=0):
        x = int(input ('enter an even number'))
    #Same here
    move (x ,x2)        

def winner ():
    if (board[0]+board [1]+board[2]==15 or
        board[0]+board [3]+board[6]==15 or
        board[1]+board [4]+board[7]==15 or
        board[3]+board [4]+board[5]==15 or
        board[2]+board [5]+board[8]==15 or
        board[6]+board [7]+board[8]==15):
        print ('you are the winner')
        return True #To know if we need to stop the game
    else: return False

def turn(s):
    print ('its '+ s +' turn')
    x = int (input ('enter the number: '))
    x1 = int (input ('enter the places number: '))
    if player == '1':
        even(x, x1)
    else: odd(x, x1)          

print('Tic Tac Toe')
print ('player A should enter even numbers only'+' and player B should enter odd numbers only')
print ('the player with the ood numbers start')
tic_tac_toe ()
while (True):
    turn(player)
    if winner(): break
    else:
        if player == '1': player = '2'
        else: player = '1'    


