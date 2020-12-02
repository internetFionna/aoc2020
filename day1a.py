day1=open("input.txt","r")
numbersRaw=day1.read().split()
day1.close
numbers=[]
for num in range(199):
    numbers.append(int(numbersRaw[num]))
for num in range(198):
    first = num
    result = 0
    for second in range(1, 199):
        if numbers[first] + numbers[second] == 2020:
            result = numbers[first] * numbers [second]
            print(result)
