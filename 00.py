import bisect

nums = [1, 0, 1, 0, 0, 0, 1, 1, 1, 0]

first_zero = bisect.bisect_left(nums, 0)
last_zero = bisect.bisect_right(nums, 0, lo=first_zero)

if first_zero == len(nums) or nums[first_zero] != 0:
    first_zero = -1
    last_zero = -1

print("First Zero Index:", first_zero)
print("Last Zero Index:", last_zero)