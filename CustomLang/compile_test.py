


"""with open("compile_text.txt", "r") as in_py:
    for line in in_py:
        line = line.strip()
        sex = compile(line, 'test', 'eval')
        exec(sex)
"""


"""with open("compile_text.txt", "r") as in_py:
    sex = compile(in_py.read(), 'test', 'eval')
    print(in_py.read())
    exec(sex)

"""


"""x = compile('print(55)', 'test', 'eval')
exec(x)


x = compile('print(55)\n print(88)', 'test', 'exec')
exec(x)
"""


"""x = 'name = "John"\nprint(name)'
exec(x)"""
# read all lines and compile them
# then execute them
raw_code = []
runnable_code = ""

with open("compile_text.txt", "r") as in_py:
    for line in in_py:
        line = line.strip()
        raw_code.append(line)



list_compile = compile(runnable_code, 'test', 'exec')
exec(list_compile)