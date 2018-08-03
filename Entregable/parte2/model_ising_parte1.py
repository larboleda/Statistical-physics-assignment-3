# coding: utf-8

# Tarea III: Parte II - Modelo de Ising

# A continuación se describe un algorítmo para la implementación del modelo de Ising en 2 dimensiones. 

import numpy as np
import matplotlib.pyplot as plt
import random 
import collections 
from functions import *


# Temperatura Fija:

#--------------------------------
# parámetros para las pruebas
#--------------------------------

#------------------------------
#tamaño de la malla: L = N x N
#------------------------------

N = [6,32,128]      

#-------------------------------------
# Temperatura fija
#-------------------------------------

T = [0.1,1.0,2.269,5.0]

#---------------------
#pasos de monte carlo
#---------------------

n_steps = 10000

for k in N:

    print("vamos en %dx%d"%(k,k))
    #--------------------------------------------
    #fijar configuración inicial para una T fija
    #--------------------------------------------
    
    Microstate = initial_microstate(k)

    for j in T:

         E = []
         M = []
         t_steps = []
         E_cumulative = []
         E_cum = 0.0

         beta = 1/j
        
         for i in range(n_steps):
        
            monte_carlo_realization(Microstate, k, beta)
        
            #energía
            Ene = microstate_energy(Microstate, k)
        
            #magnetización
            Mag = magnetization(Microstate) 
            
            #guardamos solo los valores del muestreo 
            #respresentativo correspondientes 
            #a la relajación del sistema: equilibrio
             
            if i>(n_steps/3):
                t_steps.append(i)
                E.append(Ene)
                M.append(Mag)
                E_cum =  E_cum + Ene
                E_cumulative.append(E_cum/(i+1))

         Emean = sum(E)/len(E)       
         print("Energía media \t = %f"%Emean)
         #-----------------        
         #archivo de datos
         #-----------------
                
         f = open('datos_tfix_nfix/%dx%d_T%0.1f_nsteps%d.dat'%(k,k,j,n_steps),'w')
        
         for p in range (len(E)):
             f.write("%d %.8f %d %.8f\n"%(t_steps[p], E[p], M[p], E_cumulative[p]))
         f.close()
        
         #-----------------------
         #graficas snap final
         #-----------------------

         plt.figure(figsize=(10,8))
         plt.imshow(Microstate, cmap = 'tab10',interpolation="nearest")
         plt.xlabel(r"x")
         plt.ylabel(r"y")
         plt.title(r"Configuración Final: %d $\times$ %d Espines - T = %0.1f - n = %d"%(k,k,j,n_steps))
         plt.savefig("temperatura_fija_nfijo/finalsnap_%dx%d_T%.0f_nsteps%d.png"%(k,k,j,n_steps))
         plt.clf()
         
         #-----------------------
         #graficas E vs t_steps
         #-----------------------
         
         #plt.figure(figsize=(10,8))
         plt.plot(t_steps,E,'-',color='k')
         plt.xlabel(r"Tiempo(pasos de monte carlo)")
         plt.ylabel(r"Energía")
         plt.grid()
         plt.savefig("temperatura_fija_nfijo/E_time_%dx%d_T%.0f_nsteps%d.png"%(k,k,j,n_steps))
         plt.clf()

         #plt.figure(figsize=(10,8))
         plt.plot(t_steps,E,'o', fillstyle='none' ,color='k')
         plt.xlabel(r"Tiempo(pasos de monte carlo)")
         plt.ylabel(r"Energía")
         plt.grid()
         plt.savefig("temperatura_fija_nfijo/bolitas_E_time_%dx%d_T%.0f_nsteps%d.png"%(k,k,j,n_steps))
         plt.clf()
        
         #--------------------------
         #graficas E_cum vs t_steps
         #--------------------------

         #plt.figure(figsize=(10,8))
         plt.plot(t_steps,E_cumulative,'-',color='k', lw=1.5)
         plt.xlabel(r"Tiempo(pasos de monte carlo)")
         plt.ylabel(r"Energía Cumulativa")
         plt.grid()
         plt.savefig("temperatura_fija_nfijo/Ecum_time_%dx%d_T%.0f_nsteps%d.png"%(k,k,j,n_steps))
         plt.clf()
        
        
       
print("Done")





