# IMPLEMENTASI INTEGRASI NUMERIK UNTUK MENGHITUNG ESTIMASI NILAI PI ~ (METODE 1: INTEGTRASI REIMANN)
#=======================================================

# HAFIDZ PUTRA RACHMAN ~ (21120120140096)
# METODE NUMERIK (A)
#=======================================================

import numpy as np
import time

print("[HAFIDZ PUTRA RACHMAN ~ (21120120140096)]")
print("[METODE 1: INTEGTRASI REIMANN]")
print("===========================================")

#=======================================================

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Fungsi yang  diintegrasi
def f(x):
    return 4 / (1 + x**2)

# Fungsi = menghitung integral menggunakan metode 1: Riemann
def riemann_integral(f, a, b, N):
    dx = (b - a) / N
    x = np.linspace(a, b, N, endpoint=False)
    total_sum = np.sum(f(x)) * dx
    return total_sum

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Loop melalui variasi N, hitung integral, galat RMS, dan waktu eksekusi
for N in N_values:
    start_time = time.time()
    integral_value = riemann_integral(f, 0, 1, N)
    end_time = time.time()
    
    # Hitung galat RMS
    rms_error = np.sqrt((integral_value - pi_ref)**2)
    
    # Hitung waktu eksekusi
    execution_time = end_time - start_time
    
    print(f"N = {N}")
    print(f"Estimasi Nilai π: {integral_value}")
    print(f"RMS Error: {rms_error}")
    print(f"Waktu Eksekusi(detik): {execution_time:.6f} seconds\n")
print("===========================================")