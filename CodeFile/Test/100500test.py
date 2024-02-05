import numpy as np

# Define the parameters
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


C_par = 3E-10
n_par = 2.26
m_par = 0.5
Smax_par = 365 
# return C_par, n_par, m_par, Smax_par

a = 1.92   # Initial crack length
b = 9.5 
t = 4 

YTS = 1793  # кгс/мм:2
UTS = 1655

Smax = 50.83
sigma0 = 0.5 * (YTS + UTS)

R = -0.33
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
# Kc = 131
Kc = (1+Bk*np.exp(-(Ak*t/t0)**2))*K1c
def betta(a):
    if choice_geom == 1:
        # return 0.75*1.122
        return np.sqrt(((2*b)/(np.pi*a)*np.tan((np.pi*a)/(2*b))))*((0.752+2.02*(a/b)+0.37*(1-np.sin((np.pi*a)/(2*b)))**3)/np.cos((np.pi*a)/(2*b))) * 1.122

    elif choice_geom == 4:
        phi = 1.38
        M1 = 1.08 - 0.03 * a/a
        M2 = -0.44 + 1.06 / (0.3 + a/a)
        M3 = -0.5 - 0.25*(a/a) + 14.8 * (1 - a/a)**15
        g1 = 1 + (0.08 + 0.4 * (a / t)**2)*(1-np.sin(phi))**3
        g2 = 1 + (0.08 + 0.15 * (a / t)**2)*(1-np.cos(phi))**3
        f_phi = ((a/a)**2 * np.cos(phi)**2 + np.sin(phi)**2)**(1/4)
        E_k = (1 + 1.464 * (a/a)**1.65)**(1/2)
        return (((M1 + M2*(a/t)**2 + M3*(a/t)**4) * g1 * g2 * f_phi) / E_k)
# betta = lambda a: np.sqrt(((2*b)/(np.pi*a)*np.tan((np.pi*a)/(2*b))))*((0.752+2.02*(a/b)+0.37*(1-np.sin((np.pi*a)/(2*b)))**3)/np.cos((np.pi*a)/(2*b))) # Geometric correction coefficient function
choice_geom = 1
# Define the nasgro equation
def nasgro(a):
    
    Kth = (K0*(np.sqrt((a/(a+0.0385)))))/(((1-f)/((1-A0)*(1-R)))**(1-C_th*R))
    print('betta =', betta(a), 'a =', a, 'Kth =', Kth, 'deltaK =', (1-R) * Smax * betta(a) * np.sqrt(np.pi*a), 'Kc =', Kc)
    return (C*(U*((1-R) * Smax * betta(a) * np.sqrt(np.pi*a)))**n)*((1-(Kth/((1-R) * Smax * betta(a) * np.sqrt(np.pi*a))))**p)/(((1-((Smax * betta(a) * np.sqrt(np.pi*a))/Kc))**q))

def paris(a):
    return (C_par*(((1-R)**m_par)*Smax_par*(betta(a)) * (np.sqrt(np.pi*a)))**n_par)

# Define the crack growth calculation
def crack_growth(a, final_crack_length):
    num_cycles = 0
    while a < final_crack_length:
        da = nasgro(a)
        a += da
        num_cycles += 1
    return num_cycles

# Calculate the number of cycles until the crack reaches a certain length
final_crack_length = 8
num_cycles = crack_growth(a, final_crack_length)
print("Number of cycles until crack length", final_crack_length, "is reached:", num_cycles)