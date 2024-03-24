import sys
import base64

def encode_to_base64(input_str):
    encoded_bytes = base64.b64encode(input_str.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        encoded_string = encode_to_base64(input_string)
        print("Base64 编码结果:", encoded_string)
    else:
        print("请提供要加密的字符串作为参数")
