a = [1, 3, 5, 7]
b = [2, 4, 8, 16, 32, 64]
c = [0, 1, 4, 9, 16, 25, 36]
d = [4, 16, 36, 64]
e = [1, 1, 2, 3, 5, 8]
f = [2, 10, 12, 16, 17, 18, 19]

prox_a = a[-1] + 2  
prox_b = b[-1] * 2  
prox_c = (len(c)) ** 2 
prox_d = (len(d) * 2) ** 2
prox_e = e[-1] + e[-2]
prox_f = f[-1] + 1

print(f"a) {a + [prox_a]}")
print(f"b) {b + [prox_b]}")
print(f"c) {c + [prox_c]}")
print(f"d) {d + [prox_d]}")
print(f"e) {e + [prox_e]}")
print(f"f) {f + [prox_f]}")