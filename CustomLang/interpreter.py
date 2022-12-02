import os, sys, time

from colorama import init                   # pip install colorama
init()
from colorama import Fore, Back, Style
init(autoreset=True)


def cd():   # changes directory to where the .py file is
    try:
        abspath = os.path.abspath(sys.argv[0])
        dname = os.path.dirname(abspath)
        os.chdir(dname)
    except:
        print(Fore.RED + "cd error")
cd()


indent_scope = 0


def write_var(indent_scope, name, type, value):
    with open("out.py", "a") as out_py:    
        if type == int:
            out_py.write(name + " = int(" + str(value) + ") \n")
        elif type == float:
            out_py.write(name + " = float(" + str(value) + ") \n")
        elif type == str:
            out_py.write(name + ' = str("' + str(value) + '") \n')

# this shouldnt have to take the type. 
# I should be able to pass whatever I want,
# not just a plain message. things like variable should work
# needs indent scope
def write_println(type, message):
    with open("out.py", "a") as out_py:
        if type == str:  
            out_py.write('print("' + message + '") \n')


def write_print(type, message):
    with open("out.py", "a") as out_py:
        if type == str:  
            out_py.write('print("' + message + '", end="''")')
            

def write_conditional(type, expression, code):
     with open("out.py", "a") as out_py:
        if type == "if":
            out_py.write("if " + expression + ":\n")
            out_py.write("    " + code + "\n")


def write_loop(type, expression):   
    with open("out.py", "a") as out_py:
        if type == "while":
            out_py.write("while " + expression + ":\n")


# should be able to add just two numbers, or 2 billion.
# point is, the function shouldnt take a fixed number of arguments
def math(): 
    pass


def delay(ms):
    with open("out.py", "a") as out_py:
        out_py.write("import time\n")
        out_py.write("time.sleep(" + str(ms/1000) + ")\n")


def read_file():
    with open("code.txt", "r") as in_py:
        #all_lines = all_lines.read()
        #all_lines = all_lines.replace('//', '#')
        #for line in in_py:
            #line = line.strip()
            #if line.startswith("//"):
                #pass
        #for line in in_py:
            #line = line.strip()
            #line.replace("//", "#")
                

        for line in in_py:  # main
            line = line.strip()

            if line.startswith("println"):
                #print(line)
                line = line.split("(")
                #line.strip("(")
                write_println(str, line[1])


            elif line.startswith("int"):
                line = line.strip("int ")
                line = line.split(" = ")

                write_var(indent_scope, line[0], int, line[1])

            elif line.startswith("float"):
                line = line.strip("float ")
                line = line.split(" = ")
                write_var(indent_scope, line[0], float, line[1])

            elif line.startswith("delay"):
                line = line.strip("delay(")
                line = line.strip(")")
                delay(int(line))

            elif line.startswith("if"):
                line = line.strip("if ")
                line = line.split(" == ")
                with open("out.py", "a") as out_py:
                    out_py.write("if " + line[0] + " == " + line[1] + ":\n")
                    #indent_scope += 1

            elif line.startswith("while"):
                line = line.strip("while ")
                write_loop("while", line)

    with open("out.py", "a") as out_py: 
        out_py.write("\n" * 3)          
read_file()

#write_var(indent_scope, "test", int, 3 )
#write_var(indent_scope, "test1", float, 3.14159 )
#write_var(indent_scope, "test2", str, "hi mom" )
#write_println(str , "new line!")
#write_print(str , "same line!")



"""in_code = open("code.txt", "r")
print(in_code.read())

#out_code = open("out.py", "a")
with open("out.py", "a") as out_py:
    out_py.write("test")"""