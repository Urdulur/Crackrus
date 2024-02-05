import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import integrate


# Поправочный коэффициент
def betta(a):
    if choice_geom == 1:
        return np.sqrt(((2*b)/(np.pi*a)*np.tan((np.pi*a)/(2*b))))*((0.752+2.02*(a/b)+0.37*(1-np.sin((np.pi*a)/(2*b)))**3)/np.cos((np.pi*a)/(2*b))) *1.122
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
    elif choice_geom == 4:
        phi = 1.32
        M1 = 1.08 - 0.03 * a/a
        M2 = -0.44 + 1.06 / (0.3 + a/a)
        M3 = -0.5 - 0.25*(a/a) + 14.8 * (1 - a/a)**15
        g1 = 1 + (0.08 + 0.4 * (a / t)**2)*(1-np.sin(phi))**3
        g2 = 1 + (0.08 + 0.15 * (a / t)**2)*(1-np.cos(phi))**3
        f_phi = ((a/a)**2 * np.cos(phi)**2 + np.sin(phi)**2)**(1/4)
        E_k = (1 + 1.464 * (a/a)**1.65)**(1/2)
        return (((M1 + M2*(a/t)**2 + M3*(a/t)**4) * g1 * g2 * f_phi) / E_k) * 1.122
# Уравнение        
def equation(a):
    if choice_eq == 1:
        Kth = (K0*(np.sqrt((a/(a+0.0385)))))/(((1-f)/((1-A0)*(1-R)))**(1+C_th*R))
        nasgro = (1-((Smax * betta(a) * np.sqrt(np.pi*a))/(Kc)))**q/((C*(U*((1-R)*Smax * (betta(a)) * np.sqrt(np.pi*a)))**n)*((1-(Kth/((1-R) * Smax * betta(a) * np.sqrt(np.pi*a))))**p))
        return nasgro
    elif choice_eq == 2:
        paris = 1/(C_par*((1-R)**(m_par) * Smax_par * (betta(a)) * (np.sqrt(np.pi*a)))**n_par)
        return paris
    elif choice_eq == 3:
        Kth = (K0*(np.sqrt((a/(a+1.91)))))/((1-fl)/((1-A0)*(1-R)))**(1+C_th*R)                                                                
        nasgro = ((1-((Smax * (betta(a)) * np.sqrt(np.pi*a))/Kc))**q)/((C*(U*(Smax * (betta(a)) * np.sqrt(np.pi*a)))**n)*(((1-(Kth/(Smax * (betta(a)) * np.sqrt(np.pi*a))))**p))) 
        paris = 1/(C_par*(((1-R)**m_par)*Smax_par*(betta(a)) * (np.sqrt(np.pi*a)))**n_par)
        return nasgro, paris 

def get_user_input():
    R = -0.30
    Smax = 50.83
    t = 4
    Rad = 1
    Rad_el = 1
    b = 9.5 
    return R, Smax, t, Rad, Rad_el, b

def material():

    YTS = 1793  # кгс/мм:2
    UTS = 1655 # кгс/мм:2

    return YTS, UTS,

def nasgro_var():
    
    # Nasgro Material parameters
    C = 0.876E-11
    n = 2.6
    p = 0.25
    q = 0.25
    K1e = 3127
    K1c = 2970
    Ak = 0.75
    Bk = 0.75
    K0 = 104
    alpha = 2.5
    C_th = 0.4

    # Расчёт переменных для NASGRO 
    sigma0 = 0.5 * (YTS + UTS)
    A0 = (0.825 - 0.34 * alpha + 0.05 * alpha**2)*(np.cos(np.pi/2*(Smax/sigma0)))**(1/alpha)
    A1 = (0.415-0.071*alpha)*Smax/sigma0
    A3 = 2*A0 + A1 - 1
    A2 = 1 - A0 - A1 - A3
    if R >= 0:
        f = max(R, A0 + A1*R + A2*R**2 + A3*R**3)
    else:
        f = A0 + A1*R
    U = ((1 - f)/(1-R))
    t0 = 2.5*(K1c/YTS)**2
    print('t0=', t0)
    # Kc = K1c
    Kc = (1+Bk*np.exp(-(Ak*t/t0)**2))*K1c
    print(Kc)
    return C, n, p, q, K1e, K1c, Ak, Bk, K0, alpha, C_th, sigma0, A0, A1, A3, A2, f, U, t0, Kc 


def paris():
    C_par = 3E-10
    n_par = 2.26
    m_par = 0.5
    Smax_par = 461# кгс/мм:2
    return C_par, n_par, m_par, Smax_par


R, Smax, t, Rad, Rad_el, b = get_user_input()
choice_geom = 1
choice_eq = 1
YTS, UTS = material()
C, n, p, q, K1e, K1c, Ak, Bk, K0, alpha, C_th, sigma0, A0, A1, A3, A2, f, U, t0, Kc= nasgro_var()
C_par, n_par, m_par, Smax_par = paris()

def main():

    # Задайте пределы интегрирования
    a_init = 1.92    # Нижний предел интегрирования
    a_crit = 8 # Верхний предел интегрирования
    step = 0.01
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
        plt.plot(N_nas, a, '-b', label = 'Nasgro', color='blue')
        plt.legend(loc='upper right')
    elif choice_eq == 2:
        plt.plot(N_par, a, '-b', label = 'Paris', color='red')
        plt.legend(loc='upper left')
    elif choice_eq == 3:
        plt.plot(N_nas, a, '-b', label = 'Nasgro', color='blue')
        plt.legend(loc='upper right')
        plt.plot(N_par, a, '-b', label = 'Paris', color='red')
        plt.legend(loc='upper left')
    plt.title('График функции N(а)')
    plt.xlabel('Циклы N')
    plt.ylabel('Длина трещины а, мм')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()