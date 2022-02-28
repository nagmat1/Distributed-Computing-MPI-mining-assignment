#Nagmat Nazarov, February 28, 2022. 
#CS791.1006 : Distributed Computing class. Programming Assignment 1. 

from mpi4py import MPI
import sys 
import hashlib
import time
import random 
import argparse


chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqstuvwxyz"

# Function which returns the hashlib with appropriate number of zeros
def find_T(t):
    start = time.time()
    boole = True
    soz =""
    acar = ""
    for x in range(0,t) : 
        acar = acar + '0'
    while boole :
        san = random.randint(0,len(chars)) 
        soz = soz  + chars[san-1] 
        m = hashlib.new('sha256')
        m.update(soz.encode())
        sozlem = m.hexdigest()
        if sozlem.find(acar) == 0 : 
            boole = False
            
    elapsed_time = time.time()-start 
    return elapsed_time, sozlem 


# Function for pruning T from system arguments
def komek(): 
    if len(sys.argv)>=2:
        inp = sys.argv[1]
    else :
        print("No parameter for T was included, please include T as a second parameter on console.")
        exit()

    try : 
        t = int(inp)
    except ValueError:  
        print('Incorrect integer : ', sys.argv[1])
        exit()

    if (t<1) or (t>10): 
        print("T can't be zero, it should be a number between 1 to n=10")
        exit();
    return t


#Begin the main program
t = komek()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
name = MPI.Get_processor_name()

wagt, sozlem = find_T(t)
sys.stdout.write(f"Process {rank} solved the puzzle in {wagt:.5f} seconds with solution = {sozlem}. \n")

