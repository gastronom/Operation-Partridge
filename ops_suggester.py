#!/usr/bin/env python
# Operation Suggester
# 2015may19 ver 1.0
# 2015may26 ver 1.1 added mkdir function if accepted and generation of template readme in each operation.

#original: get_ops.py
#additional: strategy_template.py 
# modification for python3: ops_suggester.py #this file

import subprocess
import random
import datetime
ls = " "
ln = "\n"
lt = "\t"
DONE = "*DONE*" # markar to distinguish used operation
mkdir = "/bin/mkdir "
template = "strategy"
longbar="-------------------------"
#functions
# writing a file
def writefile(listname, filename):
    fw = open(filename,'w')
    if len(listname)==0:
        print("nope")
    else:
        for op in listname:
            fw.write(str(op) + '\n')
    fw.close


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

    print(ops)
    
    # distinguishing used operation
    undnopidcs = [] #list of index for operations not used ever

    idx=0
    for op in ops:
        if not DONE in op: #if DONE marker is not labeled
            undnopidcs.append(idx) #remember its index
        idx = idx + 1
    
    print(undnopidcs)

    # output operation code
    unopsize = len(undnopidcs)

    print("undone operation size =" + str(unopsize))

    if unopsize < 3:
        print("few operation remain undone")
        return ""
    else:
        done = False
        accepted = False
        newop = -1 #null flag
        while not done:
            opidx = output_unused(unopsize)
            #print opidx
            print("---------------------------")
            print(ops[undnopidcs[opidx]])
            yon = input("accept this code? y/n/q ")
            if yon == "y":
                done = True
                accepted = True
                newop = undnopidcs[opidx]
            elif yon == "q":
                break
            
    # label it done
        if accepted:
            print("mission accepted")
            opc = ops[newop]
            print(opc)
            ops[newop] = str(ops[newop]+DONE)
            print(ops[newop])
            writefile(ops,outputfile)
            return opc
        else:
            print("mission not accepted")
            return ""

def output_unused(size):
    rn = random.randint(0,size-1)
    return rn

#writefile(undnopidcs, "tmp.txt")

def makedir(opr):
    if len(opr) > 0:#if operation is accepted
        phrases = opr.split()
        lowopr = ""
        for phrase in phrases:
            if "(" not in phrase:
                if ")" not in phrase:
                    lowopr = lowopr + phrase.lower()
        ret = subprocess.check_call(mkdir + lowopr, shell=True)
        if ret == 0:
            print("new directory made: "+lowopr)
            return lowopr
    else:
        #print "Damn it! this method should not be called if mission was not accepted. operation is null!"
        print("directory was not made.")

def set_templatefile(home, newdir):
    if newdir is not None:
        fw = open(home+newdir+"/"+template,'w')
        fw.write("<operation "+newdir+">"+ln)
        now = datetime.datetime.now()
        ann = now.strftime("%Y")
        mon = now.strftime("%b").lower()
        day = now.strftime("%d")
        fw.write("commenced:"+lt+ann+mon+day+ln)
        fw.write("accomplished:"+lt+ln)
        fw.write(longbar+ln)
        fw.write("mission:"+ln)
        fw.write(ln)
        fw.write(longbar+ln)
        fw.write("primary mission assets:"+ln)
        fw.write(ln)
        fw.write(longbar+ln)
        fw.write("REFERENCES"+ln)
        fw.write(ln)
        fw.write(longbar+ln)
        fw.write("remarks"+ln)
        fw.close


#main script
if __name__ == '__main__':
    print("Operation Suggeter  1.1")
    print("---------------------------")
    dir_now = subprocess.check_output("/bin/pwd ",shell=True)
    print("directory called: "+dir_now)
    opr = output_random_op("./partridge/operations.txt","./partridge/_operations_test.txt")
    dirname=makedir(opr)
    set_templatefile("./",dirname)
