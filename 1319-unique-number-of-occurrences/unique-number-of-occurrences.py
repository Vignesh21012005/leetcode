class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1
        seen=set()
        for value in freq.values():
            if value in seen:
                return False
            seen.add(value)
        return True

        