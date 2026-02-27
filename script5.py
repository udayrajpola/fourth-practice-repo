def palindrome(s):
    val=""
    for letter in s:
        val=letter+val
    if val==s:
        return True
    else:
        return False




print(palindrome("ak`ka"))