def is_palindrome(string):
    right_ptr = len(string) - 1

    for left_ptr in range(len(string)):
        if right_ptr <= left_ptr:
            return True
        
        if string[left_ptr] != string[right_ptr]:
            return False
        
        right_ptr -= 1


res = is_palindrome("amannama")
print(res)