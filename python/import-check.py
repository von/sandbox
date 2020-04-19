#!/usr/bin/env python3

try:
    import foo
except ImportError as e:
    print(f"Import of foo failed: {e}")

try:
    import os
except  ImportError as e:
    print("Import of os failed.")

print("Successfully imported 'os'")
print(f"Process pid is {os.getpid()}")
