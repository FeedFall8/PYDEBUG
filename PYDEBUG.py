from _thread import *
import time,os,sys

def check(data,compare,*arg):
    if data != compare:
        return True
    else:
        return False
class history:
    def __init__(self,name,data):
        self.name,self.data = name,data
        
class file:
    def __init__(self,name):
        self.name = name
        self.code = open(name).read()
        self.changed = False
        self.orin = self.code
    def getnow(self):
        return open(self.name,'r').read()
def ex(*arg):
    if check(FILE.code,FILE.orin) == True:
            FILE = file(FILE.name)
    else:
        pass
 #
switch=False
#FILE = file('1')#FILE = file(input("debug:"))
def c(*arg):
    global FILE
    global switch
    if check(FILE.getnow(),FILE.orin) == True:
        FILE = file(FILE.name)
        print('changed... running new window')
        switch = True
        os.system(f'python {FILE.name}')
        os.system('pause')
        switch=False
    else:
        if switch == False:
            switch=True
            try:
                os.system(f'python {FILE.name}')
                switch=False
            except KeyboardInterrupt:
                switch=False
                print('restarting (to close close this window)')
print("DEBUGPY IS IN BETA PLEASE MAKE SURE YOUR SCRIPT is cancelable")          
def main(file=None):        
    try:
        
        print("debugging started..")
        while True:
            time.sleep(2)
            if switch==False:
                start = time.time()
                start_new_thread(c,(10,1))
                print(f'[FINISHED] process took: [{(time.time() - start)/1000}] seconds')
    except Exception as e:
        input(f"{e}   press to close...")
        exit()
if len(sys.argv) >1:
    FILE = file(sys.argv[1])
    main()
else:
    FILE = file(input("debug:"))
    main()
