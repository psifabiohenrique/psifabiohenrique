
def func(x, y, z):
    print(nums[0])
    print(nums[1])
    print(nums[2])
    media = sum(nums)/len(nums)
    print(f'A média entre os valores é {media}')

nums = [3, 6, 1]
nums.sort()
func(*nums)
