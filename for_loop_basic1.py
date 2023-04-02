# 1. Basic
for n in range(151):
    print(n)

# 2. Multiples of Five
for n in range(5, 1001, 5):
    print(n)

# 3. Counting, the Dojo Way
for n in range(1, 101):
    if n % 10 == 0:
        print('Coding Dojo')
    elif n % 5 == 0:
        print('Coding')
    else:
        print(n)

# 4. Whoa. That Sucker's Huge
sum = 0
for n in range(1, 500000, 2):
    sum += n
print(sum)

# 5. Countdown by Fours
for n in range(2018, 0, -4):
    print(n)

# 6. Flexible Counter
lowNum = 3
highNum = 100
mult = 3
for n in range(lowNum, highNum, mult):
    print(n)
