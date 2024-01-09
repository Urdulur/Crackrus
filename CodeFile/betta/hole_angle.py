import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import pandas as pd


# Формулы решения скорости трещины
def nasgro(a):
    # if (1) <= 1:
    M1 = 1.13 - 0.09 * a/a
    M2 = -0.54 + 0.89 * (0.2 + a/a)**(-1)
    M3 = 0.5 - (0.65 + a/a)**(-1) + 14 * (1 - a/a)**24
    g1 = 1 + (0.1 + 0.35 * (a / t)**2)*(1-np.sin(phi))**2
    g3 = (1 + 0.04 * a/a) * (1 + 0.1 * (1 - np.cos(phi))**2)*(0.8 + 0.2 * (a / t)**(1/4))
    f_phi = ((a/a)**2 * ((1+np.cos(2*phi))/2) + ((1 - np.cos(2*phi))/2))**(1/4)
    E_k = (1 + 1.464 * (a/a)**1.65)**(1/2)
    # elif (1) > 1:
    #     M1 = np.sqrt(1) * (1 + 0.04 * a / b)
    #     M2 = 0.2 * (1)**(4)
    #     M3 = -0.11 * (a / b)**4
    #     g1 = 1 + (0.1 + 0.35 * (a / b) * (b / t)**2)*(1-np.sin(phi))**2
    #     g3 = (1.13 - 0.09 * a / b) * (1 + 0.1 * (1 - np.cos(phi))**2)*(0.8 + 0.2 * (b / t)**(1/4))
    #     f_phi = ((a / b)**2 * ((1-np.cos(2*phi))/2) + ((1 + np.cos(2*phi))/2))**(1/4)
    #     E_k = (1 + 1.464 * (a / b)**1.65)**(1/2)
    f_w = ((1/np.cos((np.pi*Rad)/(2*W))) * (1/np.cos(((np.pi*(2*Rad + n_crack * a))/(4*(W-a)+2*n_crack*a)) * (a/t)**(1/2))))**(1/2)
    L = (1 + (a / Rad) * np.cos(0.85 * phi))**(-1)
    g2 = (1 - 0.15*L + 3.46*L**2 - 4.47*L**3 + 3.52*L**4) * (1 + 0.13*L**2)**(-1)
    betta_bok_nas = ((M1 + M2*(a/t)**2 + M3*(a/t)**4) * g1 * g2 * g3 * f_phi * f_w) / E_k      
    Kth = (K0*(np.sqrt((a/(a+a_init)))))/((1-f)/((1-A0)*(1-R)))**(1+C_th*R)                                                               
    return ((1-((Smax * (betta_bok_nas) * np.sqrt(np.pi*a))/Kc))**q)/((C*(U*(Smax * (betta_bok_nas) * np.sqrt(np.pi*a)))**n)*(((1-(Kth/(Smax * (betta_bok_nas) * np.sqrt(np.pi*a))))**p)))  # Замените это на вашу функцию

def paris(a):
    # if (1) <= 1:
    M1 = 1.13 - 0.09 * a/a
    M2 = -0.54 + 0.89 * (0.2 + a/a)**(-1)
    M3 = 0.5 - (0.65 + a/a)**(-1) + 14 * (1 - a/a)**24
    g1 = 1 + (0.1 + 0.35 * (a / t)**2)*(1-np.sin(phi))**2
    g3 = (1 + 0.04 * a/a) * (1 + 0.1 * (1 - np.cos(phi))**2)*(0.8 + 0.2 * (a / t)**(1/4))
    f_phi = ((a/a)**2 * ((1+np.cos(2*phi))/2) + ((1 - np.cos(2*phi))/2))**(1/4)
    E_k = (1 + 1.464 * (a/a)**1.65)**(1/2)
    # elif (1) > 1:
    #     M1 = np.sqrt(1) * (1 + 0.04 * a / b)
    #     M2 = 0.2 * (1)**(4)
    #     M3 = -0.11 * (a / b)**4
    #     g1 = 1 + (0.1 + 0.35 * (a / b) * (b / t)**2)*(1-np.sin(phi))**2
    #     g3 = (1.13 - 0.09 * a / b) * (1 + 0.1 * (1 - np.cos(phi))**2)*(0.8 + 0.2 * (b / t)**(1/4))
    #     f_phi = ((a / b)**2 * ((1-np.cos(2*phi))/2) + ((1 + np.cos(2*phi))/2))**(1/4)
    #     E_k = (1 + 1.464 * (a / b)**1.65)**(1/2)
    f_w = ((1/np.cos((np.pi*Rad)/(2*W))) * (1/np.cos(((np.pi*(2*Rad + n_crack * a))/(4*(W-a)+2*n_crack*a)) * (a/t)**(1/2))))**(1/2)
    L = (1 + (a / Rad) * np.cos(0.85 * phi))**(-1)
    g2 = (1 - 0.15*L + 3.46*L**2 - 4.47*L**3 + 3.52*L**4) * (1 + 0.13*L**2)**(-1)
    betta_bok_par = (((M1 + M2*(a/t)**2 + M3*(a/t)**4) * g1 * g2 * g3 * f_phi * f_w) / E_k)
    return 1/(C_par*(((1-R)**m_par)*Smax_par*(betta_bok_par) * (np.sqrt(np.pi*a)))**n_par) # Замените это на вашу функцию

# Геометрия
R = 0 # Ассиметрия цикла
W = 0.492 #мм Ширина пластины 
t = 0.431 # толщина пластины
Rad = 0.156 # радиус
n_crack = 2
phi = 1.39626 

# Calculate the auxiliary variables
# def betta_holes(a):
#     alpha = (a + Rad) / b
#     alpha_star = (np.pi / 2) * alpha
#     delta = b / R  # 'b' is not defined in the provided formulas, assuming it's supposed to be 'delta'
#     gamma = R / b
#     beta = (alpha - gamma) / (1 - gamma)

#     # Calculate 'g', 'epsilon', 'phi', 'psi', 'P', 'beta_star', 'xi' using the given formulas
#     g = 0.13 * ((2 / np.pi * np.arctan(delta)) ** 2)
#     epsilon = alpha * (2 / np.pi * np.arctan(0.6 * (delta ** (1/3))))
#     phi = (np.pi * (np.sqrt((1 / alpha_star) * (np.tan(alpha_star) + g * np.sin(2 * alpha_star))) * 
#             (1 + epsilon ** 2 * (2 - epsilon ** 2) / (1 - epsilon))) - 
#             np.sqrt(1 + 2 * g))/(np.pi - 1)
#     beta_star = (gamma * delta) / (gamma * (2 * beta - 1) + 1)
#     xi = 1 + (2 / np.pi * np.arctan(1.5 * np.sqrt(delta)))
#     P = np.log((xi ** (-3/2))) / np.log(beta_star)
#     psi = (3 * (beta ** ((2/3)*P)) - 2 * np.sqrt(epsilon) * beta ** (P)) * epsilon
#     return phi * psi

# Исходные материала 
YTS = 66
UTS = 77

Smax = 18 #MPa

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
A0 = (0.825 - 0.34 * alpha + 0.05 * alpha**2)*(np.cos(((np.pi/2)*Smax)/sigma0))**(1/alpha)
A1 = (0.415-0.071*alpha)*Smax/sigma0
A3 = 2*A0 + A1 - 1
A2 = 1 - A0 - A1 - A3
f = max(R, A0 + A1*R + A2*R**2 + A3*R**3)
U = ((1 - f)/(1-R))
# C3 = ((Smax * b**4)**(p-n))/((K1c**q)*C*(U**n))
t0 = 2.5*(K1c/YTS)**2
# Kc = (1+Bk*np.e**(-Ak*t/t0)**2)*K1c
Kc = 40.1
print(Kc)

# Исходные данные для Paris
C_par = 6E-10
n_par = 3.613
m_par = 0.538
Smax_par = 18 # кгс/мм:2

# Исходные данные для Walker
# C_walker = 
# n_walker = 
# m_walker =
# K1c_walker = 

# Задайте пределы интегрирования
a_init = float(input("Введите нижний предел интегрирования: "))  # Нижний предел интегрирования
a_crit = float(input("Введите верхний предел интегрирования: "))  # Верхний предел интегрирования
step = float(input("Введите шаг интегрирования: "))
a0 = a_init
a_k = a_init + step
b = a_k
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
    # t = N_i_nas + N_nas[i-1]
    # l = N_i_par + N_par[i-1]
    N_nas.append(N_i_nas)
    N_par.append(N_i_par)
    a.append(a_k)
    a_k = a_k + step
    i = i + 1

# Используйте метод прямоугольников для численного интегрирования
for a_value, N_value in zip(a, N_nas):
    print(f"For Nasgro a = {a_value:.3f}, N = {N_value:.6f}")

for a_i, N_i in zip(a, N_par):
    print(f"For Paris a = {a_i:.3f}, N = {N_i:.6f}")

# Excel
# Create a DataFrame from the lists
df = pd.DataFrame({'Crack Length (inch)': a, 'Paris-Walker Cycles': N_par})

# Specify the filename
excel_filename = 'crack_growth_analysis.xlsx'

# Create a Pandas Excel writer using XlsxWriter as the engine
with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
    # Write the DataFrame data to XlsxWriter Excel object
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Access the XlsxWriter workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Create a chart object (scatter chart)
    chart = workbook.add_chart({'type': 'scatter', 'subtype': 'straight_with_markers'})

    # Configure the series for Nasgro cycles
    # chart.add_series({
        # 'name': 'Nasgro Cycles',
        # 'categories': ['Sheet1', 1, 0, len(a), 0],
        # 'values': ['Sheet1', 1, 1, len(N_nas), 1],
        # 'marker': {'type': 'circle', 'size': 7},
        # 'line': {'color': 'blue'}
    # })

    # Configure the series for Paris-Walker cycles
    chart.add_series({
        'name': 'Paris-Walker Cycles',
        'categories': ['Sheet1', 1, 1, len(a), 1],
        'values': ['Sheet1', 1, 0, len(N_par), 0],
        'marker': {'type': 'square', 'size': 7},
        'line': {'color': 'red'}
    })

    # Set the chart title and axis labels
    chart.set_title({'name': 'Crack Growth Analysis'})
    chart.set_x_axis({'name': 'Number of Cycles'})
    chart.set_y_axis({'name': 'Crack Length (inch)'})

    # Insert the chart into the worksheet
    worksheet.insert_chart('E2', chart)

print(f"Data and chart written successfully to {excel_filename}")

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

# # Paris figure
# plt.figure(figsize=(8,4))
# plt.plot(N_par[1:], a[1:], '-b', label = 'N(a)')
# plt.title('График функции Paris N(а)')
# plt.xlabel('Циклы N')
# plt.ylabel('Длина трещины а, мм')
# plt.legend(loc='upper right')
# plt.grid(True)
# plt.show()
# print(f"N = {N}")

# # Выведите результат
# for j in  1 to i:
#     print(f"a = {a[j]}, N = {N[j]}")
