from socket import *
from constCS import *
import pickle
import random
import hashlib

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(f"Text Processing Server listening on {HOST}:{PORT}")

def generate_password(length, use_special=True):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    if use_special:
        chars += "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def analyze_text(text):
    words = text.split()
    chars = len(text)
    chars_no_space = len(text.replace(' ', ''))
    sentences = text.count('.') + text.count('!') + text.count('?')
    return f"Words: {len(words)}, Characters: {chars}, Characters (no spaces): {chars_no_space}, Sentences: {sentences}"

while True:
    (conn, addr) = s.accept()
    print(f"Connection from {addr}")
    
    while True:
        try:
            msg = conn.recv(2048)
            if not msg:
                break
            
            data = pickle.loads(msg)
            print(f"Received operation: {data['OP']}")
            
            op = data["OP"]
            text = data.get("TEXT", "")
            param = data.get("PARAM", "")
            
            if op == "reverse":
                res = text[::-1]
                status = "OK"
            elif op == "upper":
                res = text.upper()
                status = "OK"
            elif op == "lower":
                res = text.lower()
                status = "OK"
            elif op == "count":
                if param:
                    res = text.count(param)
                else:
                    res = "Parameter required for count operation"
                    status = "NOK"
                status = "OK" if param else "NOK"
            elif op == "replace":
                parts = param.split(",", 1)
                if len(parts) == 2:
                    old_text, new_text = parts[0].strip(), parts[1].strip()
                    res = text.replace(old_text, new_text)
                    status = "OK"
                else:
                    res = "Format: old_text,new_text"
                    status = "NOK"
            elif op == "hash":
                hash_type = param.lower() if param else "md5"
                if hash_type == "md5":
                    res = hashlib.md5(text.encode()).hexdigest()
                elif hash_type == "sha256":
                    res = hashlib.sha256(text.encode()).hexdigest()
                else:
                    res = hashlib.md5(text.encode()).hexdigest()
                status = "OK"
            elif op == "password":
                try:
                    length = int(param) if param else 12
                    length = min(max(length, 4), 50)
                    res = generate_password(length)
                    status = "OK"
                except:
                    res = "Invalid length parameter"
                    status = "NOK"
            elif op == "analyze":
                res = analyze_text(text)
                status = "OK"
            else:
                status = "NOK"
                res = "Invalid operation"
            
            response = {"STATUS": status, "RES": res}
            msg = pickle.dumps(response)
            conn.send(msg)
            
        except Exception as e:
            print(f"Error: {e}")
            break
    
    conn.close()
    print(f"Connection from {addr} closed")
