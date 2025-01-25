import base64
import base91
import re
import binascii

def is_base(s, type):
    """尝试解码字符串并返回解码结果"""
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

def detect(s):
    """检测字符串的编码类型，并输出疑似编码类型"""
    types = {
        1: "Base16",
        2: "Base32",
        3: "Base64",
        4: "Base85",
        5: "Base91"
    }

    patterns = [
        (1, "^[0-9A-F=]+$"),
        (2, "^[A-Z2-7=]+$"),
        (3, "^[A-Za-z0-9+/=]+$"),
        (4, "^[A-Za-z0-9$%()*+,-./:;?@\$\$^_`{|}~]+$"),
        (5, "^[^-'\\\\]+$")  # 修改了正则表达式以适应Base91的模式
    ]

    for type_id, pattern in patterns:
        try:
            if re.match(pattern, s.decode('utf-8', errors='ignore')) is not None:
                print(f"疑似编码类型：{types[type_id]}")
                return type_id
        except (UnicodeDecodeError, AttributeError):
            pass

    print("无法识别编码类型。")
    return 0

def AutoDec(s):
    """自动解码多层编码的字符串"""
    layer = 0
    while True:
        code = detect(s)
        if code == 0:
            print("无法识别编码类型或已到达最后一层。")
            break
        decoded = is_base(s, code)
        if decoded is None:
            print("解码失败。")
            break
        s = decoded
        layer += 1
        try:
            print(f"第{layer}层：\n{s.decode('utf-8', errors='ignore')}")
        except UnicodeDecodeError as e:
            print(f"第{layer}层：\n解码成功但包含不可识别字符: {e}")
        if not s:
            break

if __name__ == "__main__":
    # 读取用户输入并去除首尾空白字符
    s = input("请输入待解字符串: ").strip().encode()
    AutoDec(s)