dial=['A', 'D', 'G', 'J', 'M', 'P','T','W','[']
# for letter in dial:
    # letter = ord(letter)

sum = 0
for _ in input():
    sum += 3
    counter = 0
    while ord(_) > ord(dial[counter+1])-1:
        counter += 1
        sum += 1
    # print(counter)

print(sum)