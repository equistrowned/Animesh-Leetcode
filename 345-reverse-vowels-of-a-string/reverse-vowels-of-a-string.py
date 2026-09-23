class Solution:
    def reverseVowels(self, seq: str) -> str:
        vowels = 'aAeEiIoOuU'
        cons=[]
        vow=[]
        seq = list(seq)
        for s in seq:
            if s not in vowels:
                cons.append(s)
            else:
                vow.append(s)
        
        for i in range(len(seq)):
            if seq[i] in vowels:
                seq[i] = vow.pop()

        return ''.join(seq)

    


        

        