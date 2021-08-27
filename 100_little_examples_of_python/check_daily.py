#Script Name : check_daily.py
#Athor : Craig Richard
#EX : Zhangyueyue

#Description : This simple script loads everything I need to carry out the daily checks for our systems.

import platform # Load Modules
import os
import subprocess
import sys

from time import strftime # Load just the strftime Module from Time

def clear_screen():       # Function to clear the screen
    if os.name == "posix": #Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"): #DOS/Windows
        os.system('CLS')  #clear the screen

def print_docs():
    print("Printing Daily Check Sheets:")
    #The command below passed the command line string to open word, open the document, print it then close word down
    subprocess.Popen(["C:\\Program Files (x86)\Microsoft Office\Office14\winword.exe", "P:\\\\Documentation\\Daily Docs\\Back office Daily Checks.doc", "/mFilePrintDefault", "/mFileExit"]).communicate()

def puttty_sessions(coffilename): #Function to load pytty sessions I need
    for server in open(conffilename): #Open the file server_list.txt, loop through reading each line - 1.1 -Changed - 1.3 Changed name to use variable conffilenam
        dubprocess.Popen(('putty -load ' +server)) #Open the PuTTY sessions - 1.1


def rdp_sessions():
    print("Loading RDP Sessions:")
    subprocess.Popen("mstsc eclr.rdp") #Open up a termianl session connection and load the euroclear session

def euroclear_docs():
    #The command below opens IE and loads the Euroclear password document
    subprocess.Popen('"C:\\Program Files\\Internet Explorer\\iexplore.exe"' '"file://fs1\pub_b\Pub_Admin\Documentation\Settlements_Files\PWD\Eclr.doc"')
    #End of the functions

#Start of the Main Program
def main():
    filename = sys.argv[0]
    confdir = os.getenv("my_config")
    conffile = ('daily_checks_servers.conf')
    conffilename = os.path.join(confdir, conffile)
    clear_screen()

    #The command below prints a little welcome message, as well as the script name, the date and time and where it was run from.
    print ("Good Morning " + os.getenv('USERNAME') + ", "+ filename, "rant at", strftime("%Y-%m-%d %H:%M:%S"), "on", platform.node(), "run from", os.getcwd())

    print_docs()
    putty_sessions(conffilename)
    rdp_sessions()
    euroclear_docs()

if __name__ == "__main__":
    main()
