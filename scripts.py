from mpi4py import MPI
import sys 
import hashlib
import time
import random 
setir = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqstuvwxyz"

def find_T(t):
    start = time.time()
    boole = True
    soz =""
    acar = ""
    print("T= ",t)
    for x in range(0,t) : 
        acar = acar + '0'
    print("Acar = ",acar)
    while boole :
        san = random.randint(0,len(setir)) 
        #print("San = {} \n".format(san))
        #print("harp = {} Soz = {} ".format(setir[san-1],soz))
        soz = soz  + setir[san-1] 
        m = hashlib.new('sha256')
        m.update(soz.encode())
        sozlem = m.hexdigest()
        if sozlem[0]=='0' : 
            boole = False
            
        #print(sozlem)
    elapsed_time = time.time()-start 
    print("Sozlem = ",sozlem)
    return elapsed_time, soz 

#print("Setir = {} sany = {} ".format(setir,len(setir)))
t = 1 
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
name = MPI.Get_processor_name()

wagt, sozlem = find_T(t)
sys.stdout.write(f"Process {rank} solved the puzzle in {wagt:.5f} seconds with solution = {sozlem}. \n")

