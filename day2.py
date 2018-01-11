def parseInput():
    filepath = 'day2input.txt'
    grid = []
    with open(filepath) as fp:  
        line = fp.readline()
        while line:
            line = line.strip('\n').split('\t')
            line = [ int(x) for x in line ]
            line.sort()
            grid.append(line)
            line = fp.readline()
    return grid

def sumRowDiff(grid):
    rows = len(grid)
    result = 0
    for i in range(0, rows):
        nums = [ int(x) for x in grid[i] ]
        low = nums[0]
        high = nums[-1]
        diff = high - low
        result += diff
    return result

def sumRowQuotients(grid):
    rows = len(grid)
    result = 0
    for i in range(0, rows):
        nums = [ int(x) for x in grid[i] ]
        length = len(nums)
        matchFound = False
        j = 0
        while not matchFound and j < length:    
            k = j + 1        
            while not matchFound and k < length:
                if nums[k] % nums[j] == 0:
                    diff = nums[k] / nums[j]
                    result += diff
                    matchFound = True
                else:
                    k += 1
            j += 1
    return result
    
def main():
    grid = parseInput()
    # part 1
    part1 = sumRowDiff(grid)
    # part 2
    part2 = sumRowQuotients(grid)
    print part1, part2

if __name__== "__main__":
  main()
  
