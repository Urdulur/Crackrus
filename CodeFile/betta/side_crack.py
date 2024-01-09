import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def nasgro(a):
    betta_bok_nas = np.sqrt(((2*b)/(np.pi*a)*np.tan((np.pi*a)/(2*b))))*((0.752+2.02*(a/b)+0.37*(1-np.sin((np.pi*a)/(2*b)))**3)/np.cos((np.pi*a)/(2*b)))
    Kth = (K0*(np.sqrt((a/(a+a_init)))))/((1-f)/((1-A0)*(1-R)))**(1+C_th*R)                                                               
    return ((1-((Smax * (betta_bok_nas) * np.sqrt(np.pi*a))/Kc))**q)/((C*(U*(Smax * (betta_bok_nas) * np.sqrt(np.pi*a)))**n)*(((1-(Kth/(Smax * (betta_bok_nas) * np.sqrt(np.pi*a))))**p)))  # Замените это на вашу функцию

def paris(a):  
    betta_bok_par = np.sqrt(((2*b)/(np.pi*a)*np.tan((np.pi*a)/(2*b))))*((0.752+2.02*(a/b)+0.37*(1-np.sin((np.pi*a)/(2*b)))**3)/np.cos((np.pi*a)/(2*b)))
    return 1/(C_par*(((1-R)**m_par)*Smax_par*(betta_bok_par) * (np.sqrt(np.pi*a)))**n_par)


# Gather user inputs for loading and geometry parameters
t = 0.431
# Rad = 0.156
# Rad_el = 0.156
R = 0 # Ассиметрия цикла
b = 14.52 #мм Ширина пластины 


# Исходные материала 
YTS = 66
UTS = 76

Smax = 18 #ksi

# Коэффициенты материала для NASGRO
C = 0.250E-7 #Коэффициент
n = 2.5
p = 1
q = 1
K1e = 43
K1c = 32
Ak = 1
Bk = 0.75
K0 = 2.4
alpha = 1.9
C_th = 2.2

# Расчёт переменных для NASGRO 
sigma0 = 0.5 * (YTS + UTS)
A0 = (0.825 - 0.34 * alpha + 0.05 * alpha**2)*(np.cos(((np.pi/2)*Smax/sigma0))**(1/alpha))
A1 = (0.415-0.071*alpha)*Smax/sigma0
A3 = 2*A0 + A1 - 1
A2 = 1 - A0 - A1 - A3
f = max(R, A0 + A1*R + A2*R**2 + A3*R**3)
U = ((1 - f)/(1-R))
# C3 = ((Smax * b**4)**(p-n))/((K1c**q)*C*(U**n))
t0 = 2.5*(K1c/YTS)**2
Kc = (1+Bk*np.e**(-Ak*t/t0)**2)*K1c
# Kc = 40.1
print(Kc)

# Исходные данные для Paris
C_par = 6E-10
n_par = 3.613
m_par = 0.538
Smax_par = 18 # кгс/мм:2


# Задайте пределы интегрирования
a_init = float(input("Введите нижний предел интегрирования: "))  # Нижний предел интегрирования
a_crit = float(input("Введите верхний предел интегрирования: "))  # Верхний предел интегрирования
step = float(input("Введите шаг интегрирования: "))
a0 = a_init
a_k = a_init + step
N_nas = []
N_par = []
a = []
i = 1
N_nas.append(0)
N_par.append(0)
a.append(a0)


while a_k <= a_crit:
    N_i_nas, error_nas = integrate.quad(nasgro, a0, a_k)
    N_i_par, error_par = integrate.quad(paris, a0, a_k)    
    # # t = N_i_nas
    # l = N_i_par 
    N_nas.append(N_i_nas)
    N_par.append(N_i_par)
    a.append(a_k)
    a_k = a_k + step
    i = i + 1

#  Используйте метод прямоугольников для численного интегрирования
for a_value, N_value in zip(a, N_nas):
    print(f"For Nasgro a = {a_value:.3f}, N = {N_value:.6f}")

for a_i, N_i in zip(a, N_par):
    print(f"For Paris a = {a_i:.3f}, N = {N_i:.6f}")

# Nasgro figure
plt.figure(figsize=(8,4))
plt.plot(N_nas[1:], a[1:], '-b', label = 'Nasgro', color='blue')
plt.legend(loc='upper right')
plt.plot(N_par[1:], a[1:], '-b', label = 'Paris', color='red')
plt.legend(loc='upper left')
plt.title('График функции N(а)')
plt.xlabel('Циклы N')
plt.ylabel('Длина трещины а, мм')
plt.grid(True)
plt.show()
