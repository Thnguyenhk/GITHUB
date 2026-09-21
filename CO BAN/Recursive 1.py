days = 6
recovery_factors= [0.5, 0.5, 1, 1, 1.5, 1.5]
#iterative implementation
def walking_distance_iterative(days,recovery_factors):
    if days <= 0 or len(recovery_factors) < days:
        return []
    actual_distances = []
    base_distances = []
    for i in range(days):
        if i == 0:
            base = 1
        elif i == 1:
            base = 2
        else:
            base = base_distances[i-1] + base_distances[i-2]
        base_distances.append(base)
        actual_distances.append(base * recovery_factors[i])
    return actual_distances
print(walking_distance_iterative(days, recovery_factors))

#recursive implementation
def get_base_distance(day):
    if day == 1:
        return 1
    if day == 2:
        return 2
    return get_base_distance(day - 1) + get_base_distance(day - 2)

def walking_distance_recursive(days, recovery_factors):
    if days <= 0 or len(recovery_factors) < days:
        return []
    
    actual_distances = []
    for i in range(1, days + 1):
        base = get_base_distance(i)
        actual_distances.append(base * recovery_factors[i-1])
        
    return actual_distances
print(walking_distance_recursive(days, recovery_factors))

#Test efficiency of both version
%timeit walking_distance_iterative(days, recovery_factors)
%timeit walking_distance_recursive(days, recovery_factors)