import matplotlib.pyplot as plt
import random
import numpy as np
import os

#T = [3, 2.27, 1]
T = [1]
L = 128
N = L*L
nsteps = N * 4000
Pasos = 5

for t in range(len(T)):
    for it in range(Pasos):
    
        """
        Definiciones iniciales
        """
        def energy(S, N, nbr):
            E=0.0
            for k in range (N):
                E = E - S[k] * sum (S[nn] for nn in (nbr[k]))
            return (0.5*E)
        
        def x_y(k,L):
            y = k // L
            x = k - y * L
            return (x, y)
        
        nbr = {i:( (i // L) * L + (i+1) % L,\
                   (i+L) % N,\
                   (i // L) * L + (i-1) % L,\
                   (i-L) % N )\
                   for i in range(N)}
        
        filename = "Figures/Dat-T-" + str(T[t]) + "-L-" + str(L) + "-nsteps-" + str(nsteps) + ".txt"
        
        """
        Lectura de archivos
        """
        if os.path.isfile(filename):
            f = open(filename,"r")
            S = [0]
            for line in f:
                S.append(int(line))
            f.close()
            print ("Starting from file ", filename)
        else:
            S = [random.choice([1,-1]) for k in range(N)]
            S_inicial = S
            print ("Starting from a random configuration")
            
            """
            Grafica configuración inicial
            """
            conf_inicial = [[0 for x in range(L)] for y in range(L)]
            for k in range (N):
              x, y = x_y(k, L)
              conf_inicial[x][y] = S[k]
 
            plt.imshow(conf_inicial, extent=[0, L, 0, L], interpolation="nearest")
            plt.set_cmap("hot")
            plt.title("Configuración inicial. T = " + str(T[t]) + "; L = "\
                      + str(L) )
            plt.savefig("Figures/Fig-T-" + str(int(T[t])) + "-L-" + str(L) \
                        + ".png", dpi=150)
            plt.show

        """
        Ising
        """
        beta = 1.0 / T[t]
        Energy = energy(S,N,nbr)
        E=[]
        for step in range(nsteps):
            k = random.randint(0,N-1)
            delta_E = 2.0 * S[k] * sum(S[nn] for nn in nbr[k])
            if random.uniform(0.0, 1.0) < np.exp(-beta * delta_E):
                S[k] = S[k]*(-1)
                Energy = Energy + delta_E
            E.append(Energy)
        print ("mean energy per spin", sum(E)/float(len(E) * N))
        
        """
        Escritura de archivos
        """
        f = open(filename, "w")
        for a in S:
            f.write(str(a) + "\n")
        f.close
                                      
        """
        Graficas
        """
        conf = [[0 for x in range(L)] for y in range(L)]
        for k in range (N):
            x, y = x_y(k, L)
            conf[x][y] = S[k]
 
        plt.imshow(conf, extent=[0, L, 0, L], interpolation="nearest")
        plt.set_cmap("hot")
        plt.title("nsteps = " + str(int(nsteps/N)) + "xL$^2$" + \
                  "x" + str(it+1) + "; meps = " + \
                  str( round(sum(E)/float(len(E)*N),4)))
        plt.savefig("Figures/Fig-T-" + str(int(T[t])) + "-L-" + str(L) \
                    + "-nsteps-" + str(int(nsteps/N)) + "x" + str(it+1) \
                    + ".png", dpi=150)
        plt.show
