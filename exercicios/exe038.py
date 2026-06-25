print("-=" * 10)
print("Analisador de Triângulos")
print("-=" * 10)

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR um triângulo ", end="")
    
 
    if a == b == c:
        print("EQUILÁTERO")
    elif a != b and b != c and a != c:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo.")
