def to_binary(n):
    if n <= 1:
        return str(n)
    return to_binary (n//2) + str(n%2)

print(to_binary(13))