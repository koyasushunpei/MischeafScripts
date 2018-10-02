# -*- coding: utf-8 -*-
import os
import time
import signal
import socket
import sys


class pycolor:
    GREEN = '\033[32;1m'
    BLUE = '\033[34;1m'
    END = '\033[m'


def prompt():
    path = os.getcwd()
    os.chdir(path)
    user = os.environ.get("USER")
    machine = socket.gethostname()
    path = path.replace(os.environ.get("HOME"), "~")
    print(pycolor.GREEN + " " + user + "@" + machine + pycolor.END + ":" + pycolor.BLUE + path + "\n" + pycolor.END + ">"),



def handler(signum, frame):
    if signum == signal.SIGTSTP:
        print("\n[1]+  停止\t\tbash")
        prompt()
    else:
        print("")
        prompt()
        pass


def instantaneousPDF(pdfName):
    os.system("evince -f " + pdfName + " 2>/dev/null &")
    time.sleep(1)
    os.system("pgrep -f " + "'evince -f " + pdfName + "'" + " |xargs kill")


def yamash(pdfName):
    while(True):
        prompt()

        tmp = raw_input()
        if(tmp == "ls"):
            tmp = "ls --color=auto"
            os.system(tmp)
        elif(tmp == "kill"):
            os.system(tmp)
        elif(tmp.split(" ")[0] == "kill"):
            print("おまえがな！！")
        elif(tmp == "cd"):
            os.chdir(os.environ.get("HOME"))
        elif(tmp.split(" ")[0] == "cd"):
            try:
                os.chdir(tmp.split(" ")[1])
            except:
                print("bash: cd: " + tmp.split(" ")[1] + ": そのようなファイルやディレクトリはありません")
        elif(tmp != "exit"):
            os.system(tmp)
        else:
            os.system("clear")

        instantaneousPDF(pdfName)



def main():
    args = sys.argv
    if len(args) < 2:
        print("pdfファイルを指定してください")
        exit(0)
    pdfName = args[1]

    signal.signal(signal.SIGTSTP, handler)
    signal.signal(signal.SIGINT, handler)

    os.system("clear")

    if pdfName == "":
        print("pdfを指定してください")

    while(True):
        yamash(pdfName)


if __name__ == '__main__':
    main()
