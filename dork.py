#!/usr/bin/python3

from dorker_class import my_dorker as dork
from sys import argv, exit

def banner():
    print(" _____   ___       _    ____")
    print("|  __ \ / _ \     | |  |___ \\")
    print("| |  | | | | |_ __| | __ __) |_ __")
    print("| |  | | | | | '__| |/ /|__ <| '__|")
    print("| |__| | |_| | |  |   < ___) | |")
    print("|_____/ \___/|_|  |_|\_\____/|_|")
    print("        [C0ded by br0k3nh34rtz]\n")

def write_file(filename, content):
    try:
        with open(filename, "a+") as file:
            for url in content: file.write(url + "\n")
            print("[+] Saved in {}".format(filename))
    except Exception:
        print("[!] Check your directory permission!")
        exit(1)
    finally:
        file.close()

banner()

if len(argv) != 2:
    print("[!] Usage: {} \"your dork\".".format(argv[0]))
    exit(1)

dorker = dork()
dorker.dork = argv[1]
url_found = dorker.g00gled0rk3r() + list(dorker.b1ngD0rk3r())
url_found = set(url_found)

if url_found:
    for url in url_found:
        print(url)

    ask = input("Wanna save this output (y/n) ?")

    if ask.lower() == "n" or ask.lower() == "no":
        exit(0)
    filename = input("input your filename: ")
    write_file(filename, url_found)
