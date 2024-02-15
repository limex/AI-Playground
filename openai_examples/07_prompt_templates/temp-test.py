
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{bcolors.HEADER}Header: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}ok: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.OKCYAN}ok: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}ok: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.FAIL}Fail: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.BOLD}Bold No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.UNDERLINE}Underline: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.WARNING}{bcolors.UNDERLINE}Warning Underline: No active frommets remain. Continue?{bcolors.ENDC}")