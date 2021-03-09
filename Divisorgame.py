# Alice and Bob take turns playing a game, with Alice starting first.

# Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

# Choosing any x with 0 < x < N and N % x == 0.
# Replacing the number N on the chalkboard with N - x.
# Also, if a player cannot make a move, they lose the game.

# Return True if and only if Alice wins the game, assuming both players play optimally.









#Solution1
def divisorGame(N):
    if (N<=1):
        return False
    
    for i in range(0,N):
        if (N%x==0):
            if not divisorGame(N-x):
                return True
    return False


#Solution 2
def divisorGame(N):
    return  N%2==0