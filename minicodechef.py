import os, filecmp
codes = {200:'success', 404:'file not found', 400:'error', 408:'timeout'}


def compile(file,lang):
    if lang == 'java':
        class_file = file[:-4]+"class"

    if (os.path.isfile(class_file)):
        os.remove(class_file)
    
    if (os.path.isfile(file)):
        if lang == 'java':
            os.system('javac '+file)
        
        if (os.path.isfile(class_file)):
            return 200
        
        else:
            return 400
    
    else:
        return 404


def run(file,input,timeout,lang):
    if lang == 'java':
        cmd = 'java '+file

    if lang == 'python':
        cmd = 'python '+file+'.py'
    
    r = os.system('timeout '+timeout+' & '+cmd+' < '+input+' > out.txt')

    if r==0:
        return 200
    
    elif r==31744:
        os.remove('out.txt')
        return 408
    
    else:
        os.remove('out.txt')
        return 400


def match(output):
    if os.path.isfile('out.txt') and os.path.isfile(output):
        b = filecmp.cmp('out.txt', output)
        return b
    
    else:
        return 404


file = 'Main.java'
lang = 'java'
testin = 'testin.txt'
testout = 'testout.txt'
timeout = '2' # secs


if lang == 'java':
    print(codes[compile(file, lang)])

print (codes[run('Main',testin,timeout,lang)])

print (match(testout))  # True implies that code is accepted.