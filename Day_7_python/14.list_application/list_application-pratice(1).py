def safe_index(my_list, value):
    # 함수를 완성하세요
    if value in my_list:
        return my_list.index(value)
    else:
        return None

print(safe_index([1,2,3,4,5], 5))
print(safe_index([1,2,3], 5))
