# coding: utf-8

# Tarea III: Parte II - Modelo de Ising

# A continuación se describe un algorítmo para la implementación del modelo de Ising en 2 dimensiones. 

import numpy as np
import matplotlib.pyplot as plt
import random 
import collections 
from functions import *

#----------------------------------------------------
#  Muestreo de Monte Carlo para varias temperaturas
#----------------------------------------------------

#------------------------------
#tamaño de la malla: L = N x N
#------------------------------

N = [2,4,8,16,64]      

#-------------------------------------
# Temperatura fija
#-------------------------------------

Tc = 2.269
Betac = 0.4407

n_steps = 4000

T =np.arange(0.05,4,0.1)

nt = np.size(T)

n_bins = 100

E_mean         = np.zeros(nt)
E2_mean        = np.zeros(nt)
Magnetization  = np.zeros(nt)
SpecificHeat   = np.zeros(nt)

SpecificHeat_arr = []
plt.figure(figsize=(10,8))
for j in N:
    
    data=open("specific_heat__N=%d.dat"%(j),'w')    
    print("vamos en %dx%d"%(j,j))

    Microstate = initial_microstate(j)
    
    for k in range(len(T)):

        E = []
        M = []
        all_E = []
    
        beta=1.0/T[k]; beta2=beta**2

        for i in range(n_steps):

        
            monte_carlo_realization(Microstate,j, beta)
        
            #energía
            Ene = microstate_energy(Microstate,j)
        
            #magnetización
            Mag = magnetization(Microstate) 

            all_E.append(Ene)
            
            if i>(n_steps/3):
                E.append(Ene)
                M.append(Mag)
                
        E_mean[k]            = sum(E)/len(E)
        E2_mean[k]           = sum(p**2 for p in E)/len(E)
        SpecificHeat[k]      = (beta2/j)*(E2_mean[k] - (E_mean[k]**2)) 
        Magnetization[k]     = sum(M)/len(M)
        data.write("%f %f \n"%(SpecificHeat[k] ,k))
        
        if k%1000==0:
            print("Plotting histogram...")
            plt.hist(all_E, bins = n_bins,histtype='bar',color="k",alpha=0.4,lw = 1.8,label=r"Histograma $\beta = %0.3f$"%beta)
            plt.xlabel(r"$E$")
            plt.ylabel(r"$\Omega(E)$")
            plt.legend()
            plt.grid()
            plt.savefig("cv_images/%dx%dhist_beta%0.3f.png"%(j,j,beta))
            plt.clf()
            
    SpecificHeat_arr.append(SpecificHeat.copy())
    print(SpecificHeat)
    print(SpecificHeat_arr)
    #------------------------
    #graficas individuales
    #------------------------
    
    #energía vs T    
    #plt.figure(figsize=(8,10))
    print("Plotting mean E...")
    plt.plot(T, E_mean, 'o', fillstyle='none',color="k", label=r"%d $\times$ %d"%(j,j))
    plt.xlabel(r"Temperature (T)", fontsize=15)
    plt.ylabel(r"Energy ", fontsize=15)
    plt.legend()
    plt.grid()
    plt.savefig("cv_images/bolitas_%dx%denergia.png"%(j,j))
    plt.clf()
    
    #energía vs T    
    #plt.figure(figsize=(8,10))
    print("Plotting mean E...")
    plt.plot(T, E_mean, '-',color="k", label=r"%d $\times$ %d"%(j,j))
    plt.xlabel(r"Temperature (T)", fontsize=15)
    plt.ylabel(r"Energy ", fontsize=15)
    plt.legend()
    plt.grid()
    plt.savefig("cv_images/%dx%denergia.png"%(j,j))
    plt.clf()
    
    #magnetización vs T
    #plt.figure(figsize=(8,10))
    print("Plotting magnetization...")
    plt.plot(T, abs(Magnetization), 'o', fillstyle='none', color="k",label=r"%d $\times$ %d"%(j,j))
    plt.xlabel(r"Temperature (T)", fontsize=15)
    plt.ylabel(r"Magnetization", fontsize=15)
    plt.legend()
    plt.grid()
    plt.savefig("cv_images/bolitas_%dx%dmagnetizacion.png"%(j,j))
    plt.clf()

    #magnetización vs T
    #plt.figure(figsize=(8,10))
    print("Plotting magnetization...")
    plt.plot(T, abs(Magnetization), '-', color="k",label=r"%d $\times$ %d"%(j,j))
    plt.xlabel(r"Temperature (T)", fontsize=15)
    plt.ylabel(r"Magnetization", fontsize=15)
    plt.legend()
    plt.grid()
    plt.savefig("cv_images/%dx%dmagnetizacion.png"%(j,j))
    plt.clf()
    
    
    #calor específico vs T
    #plt.figure(figsize=(8,10)
    print("Plotting Specific Heat...")
    plt.plot(T, SpecificHeat, 'o', fillstyle='none', color="k", label=r"%d $\times$ %d"%(j,j))
    plt.xlabel(r"Temperature (T)", fontsize=15)
    plt.ylabel(r"Specific Heat", fontsize=15)
    plt.grid()
    plt.legend()
    plt.savefig("cv_images/bolitas_%dx%dcalor_especifico.png"%(j,j))
    plt.clf()
    
    #calor específico vs T
    #plt.figure(figsize=(8,10))
    print("Plotting Specific Heat...")
    plt.plot(T, SpecificHeat, '-', color="k", label=r"%d $\times$ %d"%(j,j))
    plt.xlabel(r"Temperature (T)", fontsize=15)
    plt.ylabel(r"Specific Heat", fontsize=15)
    plt.grid()
    plt.legend()
    plt.savefig("cv_images/%dx%dcalor_especifico.png"%(j,j))
    plt.clf()

#calor específico TODAS

plt.figure(figsize=(10,8))    
print("Plotting all Specific Heat...")
for j in range(len(N)):
    plt.plot(T, SpecificHeat_arr[j], '-', label=r"%d $\times$ %d"%(N[j],N[j]))

plt.xlabel(r"Temperature (T)", fontsize=15)
plt.ylabel(r"Specific Heat", fontsize=15)  
plt.grid()
plt.legend()
plt.savefig("cv_images/cv_todos.png")
plt.clf()
