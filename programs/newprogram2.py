def check_pattern(pattern):
    if pattern[0] == ')' or pattern[-1] == '(':
        return False
    else:
        if pattern.count('(') == pattern.count(')'):
            return True
        else:
            return False


print(check_pattern('(())('))
print(check_pattern('(())()'))
print(check_pattern(')(()))'))

