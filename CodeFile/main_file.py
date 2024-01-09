import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

geom_model = input("Type geom model - side crack, middle crack, hole crack, side-angle crack or hole-angle crack:")

# Определяем материалы
def betta(choice_geom):
    if choice_geom == 1:
        return np.sqrt(((2*b)/(np.pi*a)*np.tan((np.pi*a)/(2*b))))*((0.752+2.02*(a/b)+0.37*(1-np.sin((np.pi*a)/(2*b)))**2)/np.cos((np.pi*a)/(2*b)))
    elif choice_geom == 2:
        alpha = (a + Rad) / b
        alpha_star = (np.pi / 2) * alpha
        delta = Rad_el / Rad  
        gamma = Rad / b
        beta = (alpha - gamma) / (1 - gamma)
        g = 0.13 * ((2 / np.pi * np.arctan(delta)) ** 2)
        epsilon = alpha * (2 / np.pi * np.arctan(0.6 * (delta ** (1/3))))
        phi = (np.pi * (np.sqrt(( 1 / alpha_star) * (np.tan(alpha_star) + g * np.sin(2 * alpha_star))) * (1 + epsilon ** 2 * (2 - epsilon ** 2) / (1 - epsilon))) - np.sqrt(1 + 2 * g))/(np.pi - 1) 
        beta_star = (gamma * delta) / (gamma * (2 * beta - 1) + 1)
        xi = 1 + (2 / np.pi * np.arctan(1.5 * np.sqrt(delta)))
        P = np.log10((xi ** (-3/2))) / np.log10(beta_star)
        psi = (3 * (beta ** ((2/3)*P)) - 2 * np.sqrt(xi) * beta ** (P)) * xi
        return phi * psi
    elif choice_geom == 3:
        return
    elif choice_geom == 3:
        return
    elif choice_geom == 4:
        return
    elif choice_geom == 5:
        return

        
def equation(choice_eq):
    Kth = (K0*(np.sqrt((a/a+a_init))))/((1-f)/((1-A0)*(1-R)))**(1+C_th*R)                                                               
    nasgro = ((1-((Smax * (betta_bok_nas) * np.sqrt(np.pi*a))/Kc))**q)/((C*(U*(Smax * (betta_bok_nas) * np.sqrt(np.pi*a)))**n)*(((1-(Kth/(Smax * (betta_bok_nas) * np.sqrt(np.pi*a))))**p)))   
    paris = 1/(C_par*(((1-R)**m_par)*Smax_par*(betta_bok_par) * (np.sqrt(np.pi*a)))**n_par)
    if choice_eq == 1:
        return nasgro
    elif choice_eq == 2:
        return paris
    elif choice_eq == 3:
        return nasgro, paris 

def get_user_input():
    # Gather user inputs for loading and geometry parameters
    R = float(input("Enter the cycle asymmetry (R): "))
    Smax = float(input("Enter the maximum stress (Smax) in MPa: "))
    t = float(input("Enter the thickness (t) in mm: "))
    Rad = float(input("Enter the hole radius (Rad) in mm: "))
    Rad_el = float(input("Enter the major semi-axis (Rad_el) in mm: "))

    return R, Smax, t, Rad, Rad_el

def main():
    print("Choose a geometric model of the crack:")
    print("1. Side crack")
    print("2. Middle crack")
    print("3. Hole crack")
    print("4. Side-angle crack")
    print("5. Hole-angle crack")
    choice_geom = input("Enter your choice (1-4):")

    print("Choose a equation for crack growth:")
    print("1. Paris-Walker")
    print("2. NASGRO")
    print("3. NASGRO and Paris")
    choice_eq = input("Enter your choice (1-2):")

    # Gather user inputs for loading and geometry parameters
    R = float(input("Enter the cycle asymmetry (R): "))
    Smax = float(input("Enter the maximum stress (Smax) in MPa: "))
    t = float(input("Enter the thickness (t) in mm: "))
    Rad = float(input("Enter the hole radius (Rad) in mm: "))
    Rad_el = float(input("Enter the major semi-axis (Rad_el) in mm: "))
    R = 0 # Ассиметрия цикла
    b = 100 #мм Ширина пластины 
    t = 6 # толщина пластины
    Rad = 5 # радиус
    Rad_el = 5


    # Исходные материала 
    YTS = 434
    UTS = 517

    Smax = 98.0665 #MPa

    # Коэффициенты материала для NASGRO
    C = 0.113E-9 #Коэффициент
    n = 2.763
    p = 0.5
    q = 1
    K1e = 1042
    K1c = 764
    Ak = 1
    Bk = 1.5
    K0 = 97
    alpha = 1.5
    C_th = 1.5

    # Расчёт переменных для NASGRO 
    sigma0 = 0.5 * (YTS + UTS)
    A0 = (0.825 - 0.34 * alpha + 0.05 * alpha**2)*(np.cos(((np.pi/2)*Smax)/sigma0))**(1/alpha)
    A1 = (0.415-0.071*alpha)*Smax/sigma0
    A3 = 2*A0 + A1 - 1
    A2 = 1 - A0 - A1 - A3
    f = max(R, A0 + A1*R + A2*R**2 + A3*R**3)
    U = ((1 - f)/(1-R))
    # C3 = ((Smax * b**4)**(p-n))/((K1c**q)*C*(U**n))
    t0 = 2.5*(K1c/YTS)**2
    Kc = (1+Bk*np.e**(-Ak*t/t0)**2)*K1c
    print(Kc)

    # Исходные данные для Paris
    C_par = 1.07E-8
    n_par = 2.737
    m_par = 0.5
    Smax_par = 10 # кгс/мм:2


    # Задайте пределы интегрирования
    a_init = float(input("Введите нижний предел интегрирования: "))  # Нижний предел интегрирования
    a_crit = float(input("Введите верхний предел интегрирования: "))  # Верхний предел интегрирования
    step = float(input("Введите шаг интегрирования: "))
    a0 = a_init + step
    a_k = a_init + 2*step
    N_nas = []
    N_par = []
    a = []
    i = 1
    N_nas.append(0)
    N_par.append(0)
    a.append(0)


    while a0 <= a_crit:
        N_i_nas, error_nas = integrate.quad(nasgro, a0, a_k)
        N_i_par, error_par = integrate.quad(paris, a0, a_k)    
        t = N_i_nas + N_nas[i-1]
        l = N_i_par + N_par[i-1]
        N_nas.append(t)
        N_par.append(l)
        a0 = a0 + step
        a.append(a0)
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
