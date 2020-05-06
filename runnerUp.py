# Code goes through array of integers with scores to find the runner up value (second highest)
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    first = arr[0]
    for x in arr:
        if x > first:
            first = x
    
    runnerUp = arr[0]
    for y in arr:
        if runnerUp >= first:
            runnerUp = y
        elif y > runnerUp and y < first:
            runnerUp = y
        
    print runnerUp
