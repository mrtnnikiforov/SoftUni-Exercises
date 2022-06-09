def convert_iterable_to_absolute(nums_list):
    result = [abs(el) for el in nums_list]
    return result


nums = map(float, input().split())
print(convert_iterable_to_absolute(nums))
