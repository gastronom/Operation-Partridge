#!/usr/bin/env python
# Operation Suggester
# 2015may19 ver 1.0

import random
import subprocess
DONE = "*DONE*" # markar to distinguish used operation

#functions
def output_random_op(inputfile,outputfile):

    ops = [] #list of operations
    # reading a file
    fr = open(inputfile,'r') #filename 2bchanged
    data = fr.read()
    data = data.split('\n')
    for line in data:
        if len(line) >= 1: # avoid null string in the end of file
            ops.append(line) 
    fr.close

    print ops
    
    # distinguishing used operation
    undnopidcs = [] #list of index for operations not used ever

    idx=0
    for op in ops:
        if not DONE in op: #if DONE marker is not labeled
            undnopidcs.append(idx) #remember its index
        idx = idx + 1
    
    print undnopidcs

    # output operation code
    unopsize = len(undnopidcs)

    print "unopsize =" + str(unopsize)

    if unopsize < 3:
        print "few operation remain undone"
        return
    else:
        done = False
        accepted = False
        newop = -1 #null flag
        while not done:
            opidx = output_unused(unopsize)
            #print opidx
            print "---------------------------"
            print ops[undnopidcs[opidx]]
            yon = raw_input("accept this code? y/n/q ")
            if yon == "y":
                done = True
                accepted = True
                newop = opidx
            elif yon == "q":
                break
            
    # label it done
        if accepted:
            print "mission accepted"
            opc = ops[newop]
            print opc
            ops[newop] = str(ops[newop]+DONE)
            print ops[newop]
        # update operation file
            writefile(ops,outputfile)
        else:
            print "mission not accepted"


def output_unused(size):
    rn = random.randint(0,size-1)
    return rn


# writing a file
def writefile(listname, filename):
    fw = open(filename,'w')
    if len(listname)==0:
        print "nope!"
    else:
        for op in listname:
            fw.write(str(op) + '\n')
        fw.close

#writefile(undnopidcs, "tmp.txt")


#main script
print "Operation Suggeter 1.0"
print "---------------------------"
dir_now = subprocess.check_output("/bin/pwd ",shell=True)
print "directory called: "+dir_now
output_random_op("./partridge/operations.txt","./partridge/operations.txt")
