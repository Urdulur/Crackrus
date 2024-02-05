import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton


class CrackGrowthAnalysisApp(QWidget):
    def __init__(self):
        super().__init__()

        # Default values
        self.R = -0.30
        self.Smax = 50.83
        self.t = 4
        self.Rad = 1
        self.Rad_el = 1
        self.b = 9.5
        self.choice_geom = 1
        self.choice_eq = 1

        self.init_ui()

    def init_ui(self):
        # Create widgets
        label_a_init = QLabel('Initial Crack Length (mm):')
        self.input_a_init = QLineEdit('1.92')

        label_a_crit = QLabel('Critical Crack Length (mm):')
        self.input_a_crit = QLineEdit('8.0')

        label_step = QLabel('Step Size:')
        self.input_step = QLineEdit('0.01')

        btn_plot = QPushButton('Plot Graph')
        btn_plot.clicked.connect(self.plot_graph)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(label_a_init)
        layout.addWidget(self.input_a_init)
        layout.addWidget(label_a_crit)
        layout.addWidget(self.input_a_crit)
        layout.addWidget(label_step)
        layout.addWidget(self.input_step)
        layout.addWidget(btn_plot)

        self.setLayout(layout)
        self.setWindowTitle('Crack Growth Analysis')

    def get_user_input(self):
        self.a_init = float(self.input_a_init.text())
        self.a_crit = float(self.input_a_crit.text())
        self.step = float(self.input_step.text())

    def plot_graph(self):
        self.get_user_input()

        a = np.arange(self.a_init, self.a_crit, self.step)
        N_nas = []
        N_par = []
        a_values = [self.a_init]  # Initial value for a

        for a_value in a[1:]:
            if self.choice_eq == 1:
                N_i_nas, _ = integrate.quad(self.equation, self.a_init, a_value)
                N_nas.append(N_i_nas)
            elif self.choice_eq == 2:
                N_i_par, _ = integrate.quad(self.equation, self.a_init, a_value)
                N_par.append(N_i_par)
            elif self.choice_eq == 3:
                N_i_nas, _ = integrate.quad(self.equation, self.a_init, a_value)
                N_i_par, _ = integrate.quad(self.equation, self.a_init, a_value)
                N_nas.append(N_i_nas)
                N_par.append(N_i_par)
            a_values.append(a_value)

        # Plotting
        plt.figure(figsize=(8, 4))
        if self.choice_eq == 1:
            plt.plot(N_nas, a_values, '-b', label='Nasgro', color='blue')
            plt.legend(loc='upper right')
        elif self.choice_eq == 2:
            plt.plot(N_par, a_values, '-b', label='Paris', color='red')
            plt.legend(loc='upper left')
        elif self.choice_eq == 3:
            plt.plot(N_nas, a_values, '-b', label='Nasgro', color='blue')
            plt.legend(loc='upper right')
            plt.plot(N_par, a_values, '-b', label='Paris', color='red')
            plt.legend(loc='upper left')
        plt.title('Crack Growth Analysis')
        plt.xlabel('Number of Cycles')
        plt.ylabel('Crack Length (mm)')
        plt.grid(True)
        plt.show()

    def betta(self, a):
        if choice_geom == 1:
            return np.sqrt(((2*b)/(np.pi*a)*np.tan((np.pi*a)/(2*b))))*((0.752+2.02*(a/b)+0.37*(1-np.sin((np.pi*a)/(2*b)))**3)/np.cos((np.pi*a)/(2*b))) * 1.122
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
            phi = 0.58
            M1 = 1.08 - 0.03 * a/a
            M2 = -0.44 + 1.06 / (0.3 + a/a)
            M3 = -0.5 - 0.25*(a/a) + 14.8 * (1 - a/a)**15
            g1 = 1 + (0.08 + 0.4 * (a / t)**2)*(1-np.sin(phi))**3
            g2 = 1 + (0.08 + 0.15 * (a / t)**2)*(1-np.cos(phi))**3
            f_phi = ((a/a)**2 * np.cos(phi)**2 + np.sin(phi)**2)**(1/4)
            E_k = (1 + 1.464 * (a/a)**1.65)**(1/2)
            return (((M1 + M2*(a/t)**2 + M3*(a/t)**4) * g1 * g2 * f_phi) / E_k) 

    def equation(self, a):
        if self.choice_eq == 1:
            Kth = (K0*(np.sqrt((a/(a+0.0385)))))/(((1-f)/((1-A0)*(1-R)))**(1+C_th*R))
            nasgro = (1-((Smax * betta(a) * np.sqrt(np.pi*a))/(Kc)))**q/((C*(U*((1-R)*Smax * (betta(a)) * np.sqrt(np.pi*a)))**n)*((1-(Kth/((1-R) * Smax * betta(a) * np.sqrt(np.pi*a))))**p))
            return nasgro
        elif self.choice_eq == 2:
            paris = 1/(C_par*((1-R)**(m_par) * Smax_par * (betta(a)) * (np.sqrt(np.pi*a)))**n_par)
            return paris
        elif self.choice_eq == 3:
            Kth = (K0*(np.sqrt((a/(a+1.91)))))/((1-fl)/((1-A0)*(1-R)))**(1+C_th*R)                                                                
            nasgro = ((1-((Smax * (betta(a)) * np.sqrt(np.pi*a))/Kc))**q)/((C*(U*(Smax * (betta(a)) * np.sqrt(np.pi*a)))**n)*(((1-(Kth/(Smax * (betta(a)) * np.sqrt(np.pi*a))))**p))) 
            paris = 1/(C_par*(((1-R)**m_par)*Smax_par*(betta(a)) * (np.sqrt(np.pi*a)))**n_par)
            return nasgro, paris 
   
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
        K1c = 2606
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
        Kc = (1+Bk*np.exp(-(Ak*t/t0)**2))*K1c
        print(Kc)
        return C, n, p, q, K1e, K1c, Ak, Bk, K0, alpha, C_th, sigma0, A0, A1, A3, A2, f, U, t0, Kc 
    
    def paris():
        C_par = 3E-10
        n_par = 2.26
        m_par = 0.5
        Smax_par = 365 # кгс/мм:2
        return C_par, n_par, m_par, Smax_par



def main():
    app = QApplication(sys.argv)
    window = CrackGrowthAnalysisApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
