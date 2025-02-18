import math

n1, n2 = map(float, input().split())
n3, n4 = map(float, input().split())

d = math.sqrt(math.pow(n3 - n1, 2) + math.pow(n2 - n4, 2))
print(f"{d:.4f}")
