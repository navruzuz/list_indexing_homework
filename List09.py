def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i=0
    while i<len(list1):
        if list1[1]==list1[3]==list1[0]==list1[2]==list1[4]:
            return 'true'
        else:
            return 'false'
        i+=1
    return 
print(main([0,10,0,0]))