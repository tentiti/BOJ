hour , min = input().split()
hour = int(hour)
min = int(min)
if min>=45:
  print(hour%24, min-45)
else:
  print((hour-1)%24, min+15)