import math
from run_TU import find_equilibrium_TU
from run_NTU import find_equilibrium_NTU

import timeit
start = timeit.default_timer()


# TRANSFERABLE UTILITY (TU)

# FIGURE 1
print("FIGURE 1")
delta = 1
rho = 100
r = 1
production_function = lambda x,y : x * y
nList = [10, 50, 100, 500]
for i in range(len(nList)):
    n = nList[i]
    figName = "fig1_" + str(i+1) + ".pdf"
    find_equilibrium_TU(n, delta, rho, r, production_function, figName)




# From here, all the figures (except fig. 2B) are built with n = 500
n = 500




# FIGURE 2
print("FIGURE 2")
# FIGURE 2.1
delta = 1
rho = 100
r = 1
production_function = lambda x,y : (x + y - 1) ** 2
figName = "fig2_1.pdf"
find_equilibrium_TU(n, delta, rho, r, production_function, figName)

# FIGURE 2.2
# Here we take n = 501 because the algorithme does not converge for n=500
nFig2B = 501
delta = 1
rho = 35
r = 1
production_function = lambda x,y : (x + y) ** 2
figName = "fig2_2.pdf"
find_equilibrium_TU(nFig2B, delta, rho, r, production_function, figName)


# FIGURE 2.3
delta = 1
rho = 750
r = 1
production_function = lambda x,y : x + y + x * y
figName = "fig2_3.pdf"
find_equilibrium_TU(n, delta, rho, r, production_function, figName)


# FIGURE 2.4
delta = 0.5
rho = 50
r = 1
production_function = lambda x,y : x + y + x * y
figName = "fig2_4.pdf"
find_equilibrium_TU(n, delta, rho, r, production_function, figName)





# NON-TRANSFERABLE UTILITY (NTU)


# FIGURE 3
print("FIGURE 3")
# FIGURE 3.1
delta = 0.1
rho = 30
r = 0.3
production_function = lambda x,y : math.exp(x * y)
figName = "fig3_1.pdf"
find_equilibrium_NTU(n, delta, rho, r, production_function, figName)


# FIGURE 3.2
delta = 1.1
rho = 30
r = 0.3
production_function = lambda x,y : math.exp(x * y)
figName = "fig3_2.pdf"
find_equilibrium_NTU(n, delta, rho, r, production_function, figName)


# FIGURE 3.3
delta = 0.1
rho = 3
r = 0.3
production_function = lambda x,y : x + y + x * y
figName = "fig3_3.pdf"
find_equilibrium_NTU(n, delta, rho, r, production_function, figName)





# NORMAL DISTIBUTION OF TYPES

# FIGURE 4
print("FIGURE 4")
delta = 1
rho = 1000
r = 1
production_function = lambda x,y : x * y

muList = [0.2, 0.5, 0.8]
sigmaList = [0.01, 0.1, 0.2]
i = 1
for sigma in sigmaList:
    for mu in muList:
        figName = "fig4_" + str(i) + ".pdf"
        find_equilibrium_TU(n, delta, rho, r, production_function, figName, "normal", mu, sigma)
        i += 1



stop = timeit.default_timer()
print('Time: ', stop - start)
