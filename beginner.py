#1000
print('Hello World!')

#1001
a = int(input())
b = int(input())
print('X =', a+b)

#1002
r = float(input())
print('A=%.4f' %(3.14159*pow(r, 2)))

#1003
a, b = int(input()), int(input())
print("SOMA = %d" %(a+b))

#1004
a, b = int(input()), int(input())
print("PROD = %d" %(a*b))

#1005
a, b = float(input()), float(input())
print("MEDIA = %.5f" %(((a*3.5)+(b*7.5))/11))

#1006
a, b, c = float(input()), float(input()), float(input())
print("MEDIA = %.1f" %(((a*2)+(b*3)+(c*5))/10))

#1007
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print("DIFERENCA = %d" %((a*b)-(c*d)))

#1008
a, b, c = int(input()), int(input()), float(input())
print("NUMBER = %d" %a)
print("SALARY = U$ %.2f" %(b*c))

#1009
a, b, c = str(input()), float(input()), float(input())
print("TOTAL = R$ %.2f" %(0.15*c+b))

#1010
code, unit, price = input().split()
code2, unit2, price2 = input().split()
print("VALOR A PAGAR: R$ %.2f" %((float(unit)*float(price)+float(unit2)*float(price2))))

#1011
pi = 3.14159
r = float(input())
print("VOLUME = %.3f" %((4/3)*pi*pow(r, 3)))

#1012
a, b, c = input().split()
pi = 3.14159
a, b, c = float(a), float(b), float(c)
print("TRIANGULO: %.3f\n" %(a*c/2) + "CIRCULO: %.3f\n" %(pi*c**2) + "TRAPEZIO: %.3f\n" %((a+b)*c/2) + "QUADRADO: %.3f\n" %(b*b) + "RETANGULO: %.3f" %(a*b))

#1013
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
maiorab = (a+b+(abs(a-b)))/2
maiorac = (a+c+(abs(a-c)))/2
maiorbc = (b+c+(abs(b-c)))/2
if maiorab > maiorac :
    print("%d eh o maior"  %maiorab)
elif maiorac > maiorbc :
    print("%d eh o maior" %maiorac)
else:
    print("%d eh o maior" %maiorbc)