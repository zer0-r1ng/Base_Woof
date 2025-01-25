import base64
import base91
import re
import binascii

"""Attempts to decode the string and returns a decoded result"""
def is_base(s, type):
    try:
        if type == 1:
            return base64.b16decode(s)
        elif type == 2:
            return base64.b32decode(s)
        elif type == 3:
            return base64.b64decode(s)
        elif type == 4:
            return base64.b85decode(s)
        elif type == 5:
            return base91.decode(s.decode('utf-8', errors='ignore'))  # 使用 'utf-8' 编码并忽略错误
        else:
            raise ValueError("Unknown encoding type")
    except (binascii.Error, UnicodeDecodeError) as e:
        print(f"Decoding error: {e}")
        return None

"""Detects the encoding type of the string and outputs the suspected encoding type"""
def detect(s):
    types = {
        1: "Base16",
        2: "Base32",
        3: "Base64",
        4: "Base85",
        5: "Base91"
    }
#Feature codes for various Base-encoding
    patterns = [
        (1, r"^[0-9A-F]+$"),
        (2, r"^[A-Z2-7=]+$"),
        (3, r"^[A-Za-z0-9+/=]+$"),
        (4, r"^[A-Za-z0-9$%()*+,-./:;?@[\]^_`{|}~]+$"),
        (5, r"^[!-~]+$")
    ]

    for type_id, pattern in patterns:
        try:
            decoded_s = s.decode('utf-8', errors='ignore')
            if re.fullmatch(pattern, decoded_s) is not None:
                print(f"Suspected encoding type：{types[type_id]}")
                return type_id
        except (UnicodeDecodeError, AttributeError):
            pass

    print("Fail to detect to type of code!")
    return 0

"""Automatically decode multi-layer encoding strings"""
def AutoDec(s):
    layer = 0
    while True:
        code = detect(s)
        if code == 0:
            print("The encoding type can not been recognized or the last layer has been reached!")
            break
        decoded = is_base(s, code)
        if decoded is None:
            print("Fail to decode!")
            break
        s = decoded
        layer += 1
        try:
            print(f"The{layer}th layer：\n{s.decode('utf-8', errors='ignore')}")
        except UnicodeDecodeError as e:
            print(f"The{layer}th layer：\nSuccess to decoding but contains unrecognized characters: {e}")
        if not s:
            break

if __name__ == "__main__":
    # Read the user's input and strip out the spaces
    s = input("Please enter the strings to decode: ").strip().encode()
    AutoDec(s)