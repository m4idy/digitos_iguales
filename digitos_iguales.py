
print(".................................................................")
print("..........................Digtos iguales.........................")
print(".................................................................")

# imput
N = int(input("Ingrese un número: "))

# prosesing
X = N%100
T = X%10
D = X//10

#ouptut
if T==D :
    rta = "Los dos ultimos digitos son iguales"

else :
    rta = "Los dos ultimos digitos son diferentes"

print(str(rta))