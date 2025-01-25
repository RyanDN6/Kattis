n = int(input())
trees = input().split()
i = 0
while i < n:
    trees[i] = int(trees[i])
    i = i + 1
trees.sort(reverse=True)
i = 0
while i < n:
    trees[i] += i + 2
    i = i + 1
trees.sort(reverse=True)
print(trees[0])