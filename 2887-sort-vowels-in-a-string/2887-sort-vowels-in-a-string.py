class Solution:
    def sortVowels(self, s: str) -> str:
        """


 s = "lEetcOde"

hs = {vowal}

    Iterate throguh to collect the vowal
        We stro the ch: index
    
    sort vowal collected on the ASCII values

    Iteratae through the original string
        add the sorted order vowal if its a consonant 
        else add the consonant

        """

        is_vowel = lambda ch: ch in ['a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O','U']

        vowel_arr = []

        for ch in s:
            if is_vowel(ch):
                vowel_arr.append(ch)

        q = collections.deque(sorted(vowel_arr))

        res = ""
        for i, ch in enumerate(s):
            if is_vowel(ch):
                if q:
                    sorted_vowel = q.popleft()
                    res += sorted_vowel
                else:
                    break

            else:
                res += ch

        return res
            


        