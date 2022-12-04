class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mList = list(magazine)
        for r in ransomNote:
            if r in mList:
                mList.remove(r)
            else:
                return False
        return True
