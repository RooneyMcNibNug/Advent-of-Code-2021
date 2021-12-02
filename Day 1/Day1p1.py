depths = open("input.txt", "r")

content = depths.read()
nums = content.split("\n")

depths.close()

count = 0

for i in range(len(nums)-1):
    prev = int(nums[i])
    nxt = int(nums[i+1])

    if nxt>prev:   
        count = count + 1
print(count)