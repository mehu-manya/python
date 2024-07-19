# import *sys* module,which provide access to system-specific parameters and fns.
# sys.argv[0] represents the script name itself(which can be ignored).
# sys.argv allows you to pass input to your python script from the command line.
passwords={
    'email':'123',
    'twitter':'234',
    'youtube':'345'
}

import sys
import pyperclip

if len(sys.argv)<2:
    print(f"usage: python password_locker.py [account] -copy account password")
    sys.exit()
account=sys.argv[1]
if account in passwords:
    pyperclip.copy(passwords[account])
    print(f'password for {account} copied to clipboard.') 
else:
    print(f'there is no account named{account}')
 
