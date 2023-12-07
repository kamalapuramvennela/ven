
def shortest_palindrome(s):
    if not s:
        return ""

    rev_s = s[::-1]
    l = s + '#' + rev_s
    p = [0] * len(l)

    for i in range(1, len(l)):
        j = p[i - 1]
        while j > 0 and l[i] != l[j]:
            j = p[j - 1]
        p[i] = j + (l[i] == l[j])

    return rev_s[:len(s) - p[-1]] + s


s1 = "aacecaaa"
print("Output:", shortest_palindrome(s1))


s2 = "abcd"
print("Output:", shortest_palindrome(s2))
