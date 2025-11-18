import math as m
import numpy as np

# Constants
GO = 9.806645
#[m/s^2] acceleration of gravity at SL

RE = 6356766
#[m] Radius of Earth at SL

TO = 288.150
#[K] Standard Atmosphere temperature at SL

PO = 101325
#[Pa] Standard Atmosphere pressure at SL

R = 287.0528
#[J/kgK] Standard Atmosphere for Gas Constant

def standardAtmosphere(H):
    Z = (RE*H)/(RE+H)

    if Z <= 11000:
        Ti = -6.5/1000
        T = TO + Ti*(Z-0)
        P = PO *((T/TO))**(-(GO/(R*Ti)))
        Rho = P/(R*T)
        atmosphericConditions = np.array([P, Rho, T])
        return atmosphericConditions
    
    elif Z > 11000 and Z <= 20000:
        Zi = 11000
        T = 216.650
        Po = 22632.06
        P = Po * np.exp(-(GO*(Z-Zi)) / (R*T))
        Rho = P/(R*T)
        atmosphericConditions = np.array([P, Rho, T])
        return atmosphericConditions
    
    elif Z > 20000 and Z <= 32000:
        Zi = 20000
        Ti = 1.0/1000
        To = 216.650
        T = To + Ti*(Z-Zi)
        Po = 5474.89
        P = Po *((T/To)**(-GO/(R*Ti)))
        Rho = P/(R*T)
        atmosphericConditions = np.array([P, Rho, T])
        return atmosphericConditions
    
    elif Z > 32000 and Z <= 47000:
        Zi = 32000
        To = 228.650
        Ti = 2.8/1000
        T = To +Ti*(Z-Zi)
        Po = 868.02
        P = Po *((T/To)**(-GO/(R*Ti)))
        Rho = P/(R*T)
        atmosphericConditions = np.array([P, Rho, T])
        return atmosphericConditions
    
    elif Z > 47000 and Z <= 52000:
        Zi = 47000
        T = 270.650
        Po = 110.91
        P = Po * np.exp(-(GO*(Z-Zi)) / (R*T))
        Rho = P/(R*T)
        atmosphericConditions = np.array([P, Rho, T])
        return atmosphericConditions

    elif Z > 52000 and Z <= 61000:
        Zi = 52000
        To = 270.650
        Ti = -2.0/1000
        T = To + Ti*(Z-Zi)
        Po = 66.939
        P = Po *((T/To)**(-GO/(R*Ti)))
        Rho = P/(R*T)
        atmosphericConditions = np.array([P, Rho, T])
        return atmosphericConditions
  
    elif Z > 61000 and Z <= 79000:
        Zi = 61000
        To = 252.650
        Ti = -4.0/1000
        T = To + Ti*(Z-Zi)
        Po = 3.956
        P = Po *((T/To)**(-GO/(R*Ti)))
        Rho = P/(R*T)
        atmosphericConditions = np.array([P, Rho, T])
        return atmosphericConditions
    elif Z > 79000 and Z <= 90000:
        Zi = 79000
        T = 180.650
        Po = 0.443
        P = Po * np.exp(-(GO*(Z-Zi)) / (R*T))
        Rho = P/(R*T)
        atmosphericConditions = np.array([P, Rho, T])
        return atmosphericConditions
    else:
        print("Too High or Too Low!!")
        return np.array([np.nan,np.nan,np.nan])

#Test and Calculations
def main():
    H = 79000
    atmos = standardAtmosphere(H)
    P = atmos[0]
    rho = atmos[1]
    T = atmos[2]
    print(P)
    print(rho)
    print(T)
    print(atmos)
    Z = (RE*H)/(RE+H)
    print(Z)

if __name__ == "__main__":
    main()
