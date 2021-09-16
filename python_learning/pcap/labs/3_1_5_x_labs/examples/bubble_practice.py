#!/usr/bin/env python

if __name__ == '__main__':

    nums = [8, 10, 6, 2, 4]
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                swapped = True
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    print(nums)
