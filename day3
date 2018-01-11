# O(n) time complexity, O(1) space complexity
def solve(n):
    increment = 1 # distance before changing direction
    (x, y) = (0,0)
    progress = 1
    moveRight = True
    directions = ['r', 'u', 'l', 'd']
    lastMove = 'r'
    done = False
    while progress < n and not done:
        updateProgress = 0
        if progress + increment < n:
            if moveRight:
                x += increment
                updateProgress += increment
                lastMove = 'r'
                if progress + 2*increment < n:
                    y += increment
                    updateProgress += increment
                    lastMove = 'u'
            else:
                x -= increment
                updateProgress += increment               
                lastMove = 'l'
                if progress + 2*increment < n:
                    y -= increment
                    updateProgress += increment
                    lastMove = 'd'
        else:
            remaining = n - progress
            updateProgress += remaining
            spot = directions.index(lastMove)
            nextMove = directions[spot+1] if directions[spot] < 3 else directions[0]
            print lastMove, nextMove
            if nextMove is directions[0]:
                x += remaining
            elif nextMove is directions[1]:
                y += remaining
            elif nextMove is directions[2]:
                x -= remaining
            else:
                y -= remaining
            done = True            
        moveRight = not moveRight
        progress += updateProgress
        increment += 1

    print abs(x) + abs(y)
            

solve(325489)
             
