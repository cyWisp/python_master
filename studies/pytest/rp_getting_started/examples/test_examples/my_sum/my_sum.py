

def my_sum(nums: any) -> int:
    total = 0

    try:
        for num in nums:
            total += num

        return total

    except TypeError as e:
        print(f'Object is not an iterable:\n{e}')

