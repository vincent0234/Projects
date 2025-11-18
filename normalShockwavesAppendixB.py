import math as m
import numpy as np
import pandas as pd

def staticPressureRatio(M,gamma):
    P2_P1 = (1 + ((2*gamma)/(gamma+1))*(M**2 -1))
    return P2_P1

def staticDensityRatio(M,gamma):
    rho2_rho1 = ((gamma+1)*M**2)/(2+(gamma-1)*M**2)
    return rho2_rho1

def velocityRatio(M,gamma):
    U2_U1 = (((gamma+1)*M**2)/(2+(gamma-1)*M**2))**-1
    return U2_U1

def staticTemperatureRatio(M,gamma):
    T2_T1 = (1 + ((2*gamma)/(gamma+1))*(M**2 -1)) * (((gamma+1)*M**2)/(2+(gamma-1)*M**2))**-1
    return T2_T1

def Mach2(M,gamma):
    M2 = (1+((gamma-1)/2)*M**2) / ((gamma*M**2)-((gamma-1)/2))
    M2 = np.sqrt(M2)
    return M2

def entropyDelta(CP,R,T2_T1,P2_P1):
    delS = CP * np.log(T2_T1) - R * np.log(P2_P1)
    return delS

def stagnationPressureRatio(delS,R):
    Po2_Po1 = np.exp(-delS/R)
    return Po2_Po1

def supersonicPitotFreestreamPressureRatio(M,gamma):
    Po2_P1 = ((((gamma+1)**2)*M**2)/((4*gamma*M**2)-(2*(gamma-1))))**(gamma/(gamma-1)) * ((1-gamma+(2*gamma*M**2))/(gamma+1))
    return Po2_P1

def main():
    GAMMA = 1.4
    #Ratio of specific heats
    Mach = np.linspace(1,50,2450)
    CP = 1004.5
    #[J/KgK] Specific heat air at constant pressure
    R = 287
    #[J/KgK] Air gas constant

    P2_P1 = staticPressureRatio(Mach,GAMMA)
    T2_T1 = staticTemperatureRatio(Mach,GAMMA)
    Rho2_rho1 = staticDensityRatio(Mach,GAMMA)
    M2 = Mach2(Mach,GAMMA)
    delS = entropyDelta(CP,R,T2_T1,P2_P1)
    Po2_Po1 = stagnationPressureRatio(delS,R)
    Po2_P1 = supersonicPitotFreestreamPressureRatio(Mach,GAMMA)

    df = pd.DataFrame({
        "Mach": Mach,
        "P2/P1": P2_P1,
        "Rho2/Rho1": Rho2_rho1,
        "T2/T1": T2_T1,
        "Po2/Po1": Po2_Po1,
        "Po2/P1" : Po2_P1,
        "M2": M2,
        })

    print(df)


if __name__ == "__main__":
    main()
