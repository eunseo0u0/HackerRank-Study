import os

def getMinimumCost(k, c):
    c.sort(reverse=True)
    answer = 0
    for i, f in enumerate(c):
        answer += (i // k + 1) * f
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
