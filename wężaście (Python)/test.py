import time

start = time.time()
suma = 0
for i in range(100000001):
    suma += i
end = time.time()
print(f"Wynik: {suma}")
print(f"Czas Pythona: {end - start:.4f} sekundy")