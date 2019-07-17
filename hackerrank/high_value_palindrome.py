
# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    if k <= 0:
        return s if s == s[::-1] else '-1'
    s = list(s)
    changes = [False] * n
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            if s[i] > s[n-i-1]:
                s[n-i-1] = s[i]
                changes[n-1-i] = True
            else:
                s[i] = s[n-i-1]
                changes[i] = True
            k -= 1
        if k < 0:
            return '-1'
    print(s,k,changes)
    #Try to get to max
    for i in range(n//2):
        if s[i] == s[n-i-1] == '9':
            continue
        else:
            if changes[i] == changes[n-i-1] == False:
                if k > 1:
                    s[i] = s[n-i-1] = '9'
                    k -= 2
            elif changes[i] != changes[n-i-1]:
                if k > 0:
                    s[i] = s[n-i-1] = '9'
                    k -= 1
        if k == 0:
            break
                

                

    if k > 0 and n % 2 != 0:
        s[(n//2)] = '9'

    return ''.join(s)