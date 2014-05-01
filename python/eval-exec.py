#!/usr/bin/env python
"""Examples of eval()"""

a = 4
print eval("a")

# Setting a value needs to be done with exec()
exec("a=2")
print eval("a+4")

# Dynamically import modules
for module in ["os", "sys"]:
    exec("import {}".format(module))

# And show above worked...
os.chdir("/")  # noqa
print sys.copyright  # noqa
