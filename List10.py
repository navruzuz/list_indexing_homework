def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    i=0
    while i<len(list_num):
        if list_num[0]>list_num[-1]:
            max=list_num[0]
        else:
            max=list_num[-1]
        i+=1
    return max
print(main([1,2,5,6]))