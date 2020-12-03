day1=open("day1.txt","r")
numbersRaw=day1.read().split()
day1.close()
numbers=[]
for num in range(199):
    numbers.append(int(numbersRaw[num]))
for first in range(198):
    result = 0
    for second in range(1, 199):
        for third in range (2, 198):
            if numbers[first] + numbers[second] + numbers[third] == 2020:
                result = numbers[first] * numbers[second] * numbers[third]
                print(result)
