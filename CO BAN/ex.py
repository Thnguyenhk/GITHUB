import math

sizes = [5000, 10000, 100000, 1000000]
base_n = 1000
base_time = 1.0
print("n\tO(n**2)\t\tO(log2 n)")
print("-" * 35)

for n in sizes:
    time_n2 = base_time * (n**2) / (base_n**2)  # Đã sửa: (n**2)
    time_log = base_time * math.log2(n) / math.log2(base_n)
    print(f"{n}\t{time_n2:.2f} s\t\t{time_log:.2f} s")