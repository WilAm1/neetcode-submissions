from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Prepends the length and a '#' to every string
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the '#' separating the length from the string
            j = s.find("#", i)
            length = int(s[i:j])
            
            # Extract the substring using the exact length
            res.append(s[j + 1 : j + 1 + length])
            
            # Move the pointer to the start of the next item
            i = j + 1 + length
            
        return res
