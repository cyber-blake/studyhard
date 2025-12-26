abscissas = list(map(float, input().split()))
ordinates = list(map(float, input().split()))
applicates = list(map(float, input().split()))
result = zip(abscissas, ordinates, applicates)

for x in result:
    