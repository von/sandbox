#!/usr/bin/env python3

class Colors:
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    reset = "\033[0m"


print(f"{Colors.black}Black text {Colors.reset}End of black text")
print(f"{Colors.red}Red text")
print(f"{Colors.green}Green text")
print(f"{Colors.yellow}Yellow text")
print(f"{Colors.blue}Blue text")
print(f"{Colors.cyan}Cyan text")
print(f"{Colors.white}White text {Colors.reset}End of white text")
