# Find largest of 3 numbers without max()

def find_max(numbers):
    
    for i in range(len(numbers)-1):
        largest = numbers[i]
        if numbers[i] > numbers[i+1]:
            largest = numbers[i]
        else:
            largest = numbers[i+1]
    print("largest: ", largest)
    
find_max([1,2,3])
find_max([40,50,20])

print(max([1,2,3]))