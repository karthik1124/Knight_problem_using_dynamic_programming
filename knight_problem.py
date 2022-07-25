memo={}
def knightProbability(n,k,row,column):
    if row<0 or row>=n: return 0 # check if we moved off the board
    if column< 0 or column>=n: return 0 # check if we moved off the board
    if k==0: return 1.0 # If all specific sequence of moves are survived then probability will be 1
    if (row,column,k) in memo: return memo[(row,column,k)] # If already calculated then return the value
    p=0 # intitializng the probability 
    # There are 8 different moves the knight can move but half of those moves are mirror moves
    # (x+1,y+2), (x+2,y+1), (x+2,y-1), (x+1,y-2), (x-1,y-2), (x-2,y-1), (x-2,y+1), (x-1,y+2)
    for i,j in [(-2, -1), (-2, 1), (-1, -2), (-1, 2)]:
        p+=knightProbability(n,k-1,row+i,column+j)*1/8
        p+=knightProbability(n,k-1,row-i,column-j)*1/8
    memo[(row,column,k)]=p
    return p
def getsteps(x,y,tx,ty,dp):
    # (x,y)- coordinate of the knight.(tx,ty)- coordinate of the target position.
    if x==tx and y==ty: return dp[0][0] # If knight is on the target position then return 0
    elif dp[abs(x-tx)][abs(y-ty)]!=0: return dp[abs(x-tx)][abs(y-ty)] # If already calculated then return the value
    else:
        # There will be two distinct positions for the knight to reach target. Let the positions be (x1,y1) & (x2,y2)
        x1=y1=x2=y2=0
        # (x1,y1) & (x2,y2) positions different according to the situation as follow.
        if x<=tx and y<=ty:
            x1,y1=x+2,y+1
            x2,y2=x+1,y+2
        elif x<=tx and y>ty:
            x1,y1=x+2,y-1
            x2,y2=x+1,y-2
        elif x>tx and y<=ty:
            x1,y1=x-2,y+1
            x2,y2=x-1,y+2
        else:
            x1,y1=x-2,y-1
            x2,y2=x-1,y-2
        # Number of steps will be 1 + minimum of steps required from (x1, y1) and (x2, y2).
        dp[abs(x-tx)][abs(y-ty)]=min(getsteps(x1,y1,tx,ty,dp),getsteps(x2,y2,tx,ty,dp))+1
        # Exchanging the coordinates x with y of both knight and target will result in same number of steps.
        dp[abs(y-ty)][abs(x-tx)]=dp[abs(x-tx)][abs(y-ty)]
    return dp[abs(x-tx)][abs(y-ty)]
def minimumsteps(n,x,y,tx,ty):
    # (x,y)- coordinate of the knight.(tx,ty)- coordinate of the target position.
    # Cases where either the knight or the target is at the corner and the difference of knight & target 
    # coordinates is (1,1)
    l=[(1,1,2,2),(2,2,1,1),(1,n,2,n-1),(2,n-1,1,n),(n,1,n-1,2),(n-1,2,n,1),(n,n,n-1,n-1),(n-1,n-1,n,n)]
    if (x,y,tx,ty) in l: ans=4
    else:
        dp=[[0 for i in range(n)] for j in range(n)] 
        # dp[a][b], here a, b is the difference of x & tx and y & ty respectively
        dp[1][0]=dp[0][1]=3 # If knight & target are at adjacent squares along same row or column
        dp[1][1]=dp[2][0]=dp[0][2]=2 # If knight & target are at adjacent squares but lie diagonally to each other
        dp[2][1]=dp[1][2]=1 # If target lies two cells in a cardinal direction and then one cell in an 
                            # orthogonal direction (forming the shape of L) to the knight
        ans=getsteps(x,y,tx,ty,dp)
    return ans
n=int(input("Enter chess board size(nxn): "))
x,y=map(int,input("Enter knight coordinate: ").split())
tx,ty=map(int,input("Enter target coordinate: ").split())
ans=minimumsteps(n,x,y,tx,ty)
print(minimumsteps(n,x,y,tx,ty))
print(knightProbability(n,ans,x,y))
