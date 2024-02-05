import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# Поправочный коэффициент
def betta(a):
    if choice_geom == 1:
        return np.sqrt(((2*b)/(np.pi*a)*np.tan((np.pi*a)/(2*b))))*((0.752+2.02*(a/b)+0.37*(1-np.sin((np.pi*a)/(2*b)))**3)/np.cos((np.pi*a)/(2*b)))
    elif choice_geom == 2:
        alpha = ((a) + Rad) / b
        alpha_star = (np.pi / 2) * alpha
        delta = Rad / Rad
        gamma = Rad / b
        beta = (alpha - gamma) / (1 - gamma)
        g = 0.13 * ((2 / np.pi * np.arctan(delta)) ** 2)
        epsilon = alpha * (2 / np.pi * np.arctan(0.6 * (delta ** (1/3))))
        phi = (np.pi * (np.sqrt(( 1 / alpha_star) * (np.tan(alpha_star) + g * 2 * np.sin(alpha_star) * np.cos(alpha_star))) * (1 + epsilon ** 2 * (2 - epsilon ** 2) / (1 - epsilon))) - np.sqrt(1 + 2 * g))/(np.pi - 1)
        beta_star = (gamma * delta) / (gamma * (2 * delta - 1) + 1)
        xi = 1 + (2 / np.pi * np.arctan(1.5 * np.sqrt(delta)))
        P = np.log10((xi ** (-3/2))) / np.log10(beta_star)
        psi = (3 * (beta ** ((2/3)*P)) - 2 * np.sqrt(xi) * beta ** (P)) * xi
        return psi * phi
    elif choice_geom == 3:
        M1 = 1.13 - 0.09 * a/a
        M2 = -0.54 + 0.89 * (0.2 + a/a)**(-1)
        M3 = 0.5 - (0.65 + a/a)**(-1) + 14 * (1 - a/a)**24
        g1 = 1 + (0.1 + 0.35 * (a / t)**2)*(1-np.sin(phi))**2
        g3 = (1 + 0.04 * a/a) * (1 + 0.1 * (1 - np.cos(phi))**2)*(0.8 + 0.2 * (a / t)**(1/4))
        f_phi = ((a/a)**2 * ((1+np.cos(2*phi))/2) + ((1 - np.cos(2*phi))/2))**(1/4)
        E_k = (1 + 1.464 * (a/a)**1.65)**(1/2)
        f_w = ((1/np.cos((np.pi*Rad)/(2*W))) * (1/np.cos(((np.pi*(2*Rad + n_crack * a))/(4*(W-a)+2*n_crack*a)) * (a/t)**(1/2))))**(1/2)
        L = (1 + (a / Rad) * np.cos(0.85 * phi))**(-1)
        g2 = (1 - 0.15*L + 3.46*L**2 - 4.47*L**3 + 3.52*L**4) * (1 + 0.13*L**2)**(-1)
        return ((M1 + M2*(a/t)**2 + M3*(a/t)**4) * g1 * g2 * g3 * f_phi * f_w) / E_k 

# Уравнение        
def equation(a):
    if choice_eq == 1:
        Kth = (K0*(np.sqrt((a/(a+a_init)))))/((1-f)/((1-A0)*(1-R)))**(1+C_th*R)                                                                
        nasgro = ((1-((Smax * (betta(a)) * np.sqrt(np.pi*a))/Kc))**q)/((C*(U*(Smax * (betta(a)) * np.sqrt(np.pi*a)))**n)*(((1-(Kth/(Smax * (betta(a)) * np.sqrt(np.pi*a))))**p))) 
        return nasgro
    elif choice_eq == 2:
        paris = 1/(C_par*(((1-R)**m_par)*Smax_par*(betta(a)) * (np.sqrt(np.pi*a)))**n_par)
        return paris
    elif choice_eq == 3:
        Kth = (K0*(np.sqrt((a/(a+a_init)))))/((1-f)/((1-A0)*(1-R)))**(1+C_th*R)                                                                
        nasgro = ((1-((Smax * (betta(a)) * np.sqrt(np.pi*a))/Kc))**q)/((C*(U*(Smax * (betta(a)) * np.sqrt(np.pi*a)))**n)*(((1-(Kth/(Smax * (betta(a)) * np.sqrt(np.pi*a))))**p))) 
        paris = 1/(C_par*(((1-R)**m_par)*Smax_par*(betta(a)) * (np.sqrt(np.pi*a)))**n_par)
        return nasgro, paris 

def get_user_input():
    # Gather user inputs for loading and geometry parameters
    R = float(input("введите ассиметрию цикла R:"))
    Smax = float(input("введите максимальное напряжение Smax:"))
    t = float(input("введите толщину пластины t:"))
    Rad = float(input("введите радиус пластины Rad:"))
    Rad_el = float(input("введите большую полуось пластины Rad_el:"))
    b = float(input("введите ширину пластины b:"))

    return R, Smax, t, Rad, Rad_el, b

def material():

    YTS = 1655  # кгс/мм:2
    UTS = 1793 # кгс/мм:2

    # Nasgro Material parameters
    C = 0.876E-11
    n = 2.6
    p = 0.25
    q = 0.25
    K1e = 3127
    K1c = 2970
    Ak = 0.75
    Bk = 0.75
    K0 = 264
    alpha = 2.5
    C_th = 0.4
    return YTS, UTS, C, n, p, q, K1e, K1c, Ak, Bk, K0, alpha, C_th

def nasgro_var():
    
    # Расчёт переменных для NASGRO 
    sigma0 = 0.5 * (YTS + UTS)
    A0 = (0.825 - 0.34 * alpha + 0.05 * alpha**2)*(np.cos(((np.pi/2)*Smax)/sigma0))**(1/alpha)
    A1 = (0.415-0.071*alpha)*Smax/sigma0
    A3 = 2*A0 + A1 - 1
    A2 = 1 - A0 - A1 - A3
    f = max(R, A0 + A1*R + A2*R**2 + A3*R**3)
    U = ((1 - f)/(1-R))
    C3 = ((Smax * b**4)**(p-n))/((K1c**q)*C*(U**n))
    t0 = 2.5*(K1c/YTS)**2
    Kc = (1+Bk*np.e**(-Ak*t/t0)**2)*K1c
    return sigma0, A0, A1, A3, A2, f, U, C3, t0, Kc


def paris():
    C_par = 6E-10
    n_par = 3.613
    m_par = 0.538
    Smax_par = 18 # кгс/мм:2
    return C_par, n_par, m_par, Smax_par


R, Smax, t, Rad, Rad_el, b = get_user_input()
choice_geom = int(input("выберите модель геометрии: 1 - SIDE, 2 - HOLE_SIDE, 3 - HOLE_ANGLE: "))
choice_eq = int(input("выберите тип уравнения: 1 - NASGRO, 2 - PARIS, 3 - PARIS and NASGRO: "))
YTS, UTS, C, n, p, q, K1e, K1c, Ak, Bk, K0, alpha, C_th = material()
sigma0, A0, A1, A3, A2, f, U, C3, t0, Kc = nasgro_var()
C_par, n_par, m_par, Smax_par = paris()

def main():

    # Задайте пределы интегрирования
    a_init = float(input("Введите нижний предел интегрирования: "))  # Нижний предел интегрирования
    a_crit = float(input("Введите верхний предел интегрирования: "))  # Верхний предел интегрирования
    step = float(input("Введите шаг интегрирования: "))
    N_nas = []
    N_par = []
    a = np.arange(a_init, a_crit, step)   
    N_nas.append(0)
    N_par.append(0)


    for a_value in a[1:]:
        if choice_eq == 1:
            N_i_nas, error_nas = integrate.quad(equation, a_init, a_value)
            N_nas.append(N_i_nas)
        elif choice_eq == 2:
            N_i_par, error_par = integrate.quad(equation, a_init, a_value)
            N_par.append(N_i_par)
        elif choice_eq == 3:
            N_i_nas, error_nas = integrate.quad(equation, a_init, a_value)
            N_i_par, error_par = integrate.quad(equation, a_init, a_value)
            N_nas.append(N_i_nas)
            N_par.append(N_i_par)

    #  Используйте метод прямоугольников для численного интегрирования
    if choice_eq == 1:
        for a_value, N_value in zip(a, N_nas):
            print(f"For Nasgro a = {a_value:.3f}, N = {N_value:.6f}")
    elif choice_eq == 2:
        for a_value, N_value in zip(a, N_par):
            print(f"For Paris a = {a_value:.3f}, N = {N_value:.6f}")

    # Nasgro figure
    plt.figure(figsize=(8,4))
    if choice_eq == 1:
        plt.plot(N_nas[0:], a[0:], '-b', label = 'Nasgro', color='blue')
        plt.legend(loc='upper right')
    elif choice_eq == 2:
        plt.plot(N_par[0:], a[0:], '-b', label = 'Paris', color='red')
        plt.legend(loc='upper left')
    elif choice_eq == 3:
        plt.plot(N_nas[0:], a[0:], '-b', label = 'Nasgro', color='blue')
        plt.legend(loc='upper right')
        plt.plot(N_par[0:], a[0:], '-b', label = 'Paris', color='red')
        plt.legend(loc='upper left')
    plt.title('График функции N(а)')
    plt.xlabel('Циклы N')
    plt.ylabel('Длина трещины а, мм')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()