def appendAndDelete(s, t, k):
    if len(t) < len(s):
        for i in range(len(t)):
            if t[i] != s[i]:
                break
    else:
        for i in range(len(s)):
            if t[i] != s[i]:
                break
    diff = len(s[i:]) + len(t[i:])

    if len(s) + len(t) < k:
	'''Full string s can be replaced with string t.'''
        return "Yes"
    elif diff > k:
        return "No"
    elif diff%2 == k%2:
	'''Both diff and k must be even or odd
	so that append and delete is compensated.'''
        return "Yes"
    else:
        return "No"