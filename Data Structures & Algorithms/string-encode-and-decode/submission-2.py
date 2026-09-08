import base64

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for s in strs:
            b64_text = base64.b64encode(s.encode('utf-8')).decode('utf-8')
            encoded_list.append(b64_text)
            
        return ":".join(encoded_list)

    def decode(self, s: str) -> List[str]:

        if not s:
            return [""]
        encoded_list = s.split(":")
        # 2. Decode each base64 chunk back into the original string
        decoded_list = []
        for encoded_str in encoded_list:
            original_text = base64.b64decode(encoded_str.encode('utf-8')).decode('utf-8')
            decoded_list.append(original_text)
        print(decoded_list)
        return decoded_list
        