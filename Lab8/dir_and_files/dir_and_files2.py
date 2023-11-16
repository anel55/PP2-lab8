import os
print('Exist:', os.access('C:\\pp2\\week6\\builtin_functions\\builtin_functions1.py', os.F_OK))
print('Readable:', os.access('C:\\pp2\\week6\\builtin_functions\\builtin_functions1.py', os.R_OK))
print('Writable:', os.access('C:\\pp2\\week6\\builtin_functions\\builtin_functions1.py', os.W_OK))
print('Executable:', os.access('C:\\pp2\\week6\\builtin_functions\\builtin_functions1.py', os.X_OK))