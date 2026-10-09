def is_devisible_by_3(n):
    if n == 0:
        return True
    if n == 1 or n == 2:
        return False
    return sub_step(n-3)

def sub_step(n):
    return is_devisible_by_3(n)

print(is_devisible_by_3(15))