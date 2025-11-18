import math as m
import numpy as np
import pandas as pd

def pressureRatio(M,gamma):
    Po_P = (1 + ((gamma-1)/2)*pow(M,2) )**(gamma/(gamma-1))
    return Po_P

def densityRatio(M,gamma):
    rhoo_rho = (1 + ((gamma-1)/2)*pow(M,2) )**(1/(gamma-1))
    return rhoo_rho

def temperatureRatio(M,gamma):
    To_T = 1 + ((gamma-1)/2)*pow(M,2)
    return To_T

def areaMachNumber(M,gamma):
    A_Astar = (1/M) *((2/(gamma+1))*(1+((gamma-1)/2)*pow(M,2)))**((gamma+1)/(2*(gamma-1)))
    return A_Astar

def main():
    GAMMA = 1.4
    Mach = np.linspace(0.2,50,500)


    Po_P = pressureRatio(Mach,GAMMA)
    To_T = temperatureRatio(Mach,GAMMA)
    Rhoo_rho = densityRatio(Mach,GAMMA)
    A_Astar = areaMachNumber(Mach,GAMMA)

    df = pd.DataFrame({
        "Mach": Mach,
        "Po/P": Po_P,
        "Rho_o/Rho": Rhoo_rho,
        "To/T": To_T,
        "A_Astar": A_Astar
        })

    print(df)


if __name__ == "__main__":
    main()
