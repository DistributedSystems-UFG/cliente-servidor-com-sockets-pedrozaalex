from socket import *
from constCS import *
import pickle

def show_operations():
    print("\nAvailable text processing operations:")
    print("- reverse: Reverse the text")
    print("- upper: Convert to uppercase") 
    print("- lower: Convert to lowercase")
    print("- count: Count occurrences of a substring")
    print("- replace: Replace text (format: old,new)")
    print("- hash: Generate MD5 or SHA256 hash")
    print("- password: Generate random password")
    print("- analyze: Get text statistics")
    print("- help: Show this menu")
    print("- quit: Exit\n")

s = socket(AF_INET, SOCK_STREAM)
try:
    s.connect((HOST, PORT))
    print(f"Connected to Text Processing Server at {HOST}:{PORT}")
    show_operations()
    
    while True:
        op = input("Operation: ").strip().lower()
        
        if op == "quit":
            break
        elif op == "help":
            show_operations()
            continue
        
        text = ""
        param = ""
        
        if op in ["reverse", "upper", "lower", "analyze"]:
            text = input("Enter text: ")
        elif op == "count":
            text = input("Enter text: ")
            param = input("What to count: ")
        elif op == "replace":
            text = input("Enter text: ")
            param = input("Replace what,with what: ")
        elif op == "hash":
            text = input("Enter text to hash: ")
            hash_type = input("Hash type (md5/sha256) [md5]: ").strip()
            param = hash_type if hash_type else "md5"
        elif op == "password":
            length = input("Password length [12]: ").strip()
            param = length if length else "12"
        else:
            print("Unknown operation. Type 'help' for available operations.")
            continue
        
        data = {"OP": op, "TEXT": text, "PARAM": param}
        msg = pickle.dumps(data)
        s.send(msg)
        
        msg = s.recv(2048)
        data = pickle.loads(msg)
        
        if data["STATUS"] == "OK":
            print(f"Result: {data['RES']}")
        else:
            print(f"Error: {data['RES']}")
        print()

except ConnectionRefusedError:
    print("Could not connect to server. Make sure server is running.")
except Exception as e:
    print(f"Error: {e}")
finally:
    s.close()
