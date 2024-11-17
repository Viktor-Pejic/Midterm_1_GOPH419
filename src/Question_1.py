import math

def error_T(error_L, error_a, error_D, dL, da, dD):
    dT_L = dL * error_L
    dT_a = da * error_a
    dT_D = dD * error_D
    dT = dT_L + dT_a + dT_D


    return dT, dT_L, dT_a, dT_D

def L_term(a, D, sigma, c):
    dL = ((1 - a) / (64 * math.pi * sigma * D**2)) * c
    return dL

def a_term(L, D, sigma, c):
    da = (-L / (64 * math.pi * sigma * D**2)) * c
    return da

def D_term(L, a, D, sigma, c):
    dD = (-L * (1 - a) / (32 * math.pi * sigma * D**3)) * c
    return dD

def theoretical_T(L, a, D, sigma):
    T = (L*(1-a)/ (16*math.pi*sigma*D**2)) ** 0.25
    return T

def main():
    L = 3.828e26
    a = 0.306
    D = 1.496e11
    sigma = 5.670374419e-8

    error_L = 0.004e26
    error_a = 0.001
    error_D = 0.025e11

    c = ((L * (1 - a)) / (16 * math.pi * sigma * D**2)) ** (-0.75)

    dL = L_term(a, D, sigma, c)
    da = a_term(L, D, sigma, c)
    dD = D_term(L, a, D, sigma, c)

    delta_T, dT_L, dT_a, dT_D = error_T(error_L, error_a, error_D, dL, da, dD)

    print(f"Relative error in L = {error_L/L:.5f}\n"
          f"Relative error in a = {error_a/a:.5f}\n"
          f"Relative error in D = {error_D/D:.5f}\n")

    expected_T = theoretical_T(L, a, D, sigma)
    print(f"Expected T = {expected_T:.5f} K, {theoretical_T(L, a, D, sigma) - 273:.5f} C\n"
          f"Total error in T = {delta_T:.5f}\n"
          f"Contribution from L (error in L): {(dT_L/delta_T):.5f} K\n"
          f"Contribution from a (error in a): {(dT_a/delta_T):.5f} K\n"
          f"Contribution from D (error in D): {(dT_D/delta_T):.5f} K\n"
          f"Relative error of T = {abs(delta_T / expected_T):.5f}")



if __name__ == "__main__":
    main()

