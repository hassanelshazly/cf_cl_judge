from cf_client import cf_client
import re


def main():
    client = cf_client()
    while True:
        try:
            command = input(">>> ")
            if command == "":
                pass
            elif re.match("help", command):
                print_help()
            elif re.match("quit", command):
                break
            elif re.match("login",command ):
                client.login()
            elif re.match("submit", command):
                client.submit()
            else:
                print("Undefind Command")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
            break
        except:
            print("Excpction occured, Pls try again")

def print_help():
    print("Codeforces command line judge, version 1.0.0")
    print("Type 'help' for more information.")


if __name__ == "__main__":
    print("Codeforces command line judge, version 1.0.0")
    print("Type 'help' for more information.")
    main()