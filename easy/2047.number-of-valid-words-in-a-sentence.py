class Solution:
  def countValidWords(self, sentence: str) -> int:
    stuff = sentence.split(" ")
    cnt = 0
    # print(stuff)
    

      
    for word in stuff:
      word = word.replace(" ", "")
      good = True

      if word:
        for punc in ["!", ".", ","]:
          if word[-1] != punc and word.count(punc) == 1:
            good = False
          elif word.count(punc) > 1:
            good = False        
        for i in range(10):
          if word.count(str(i)) >= 1:
            good = False
            
        # print(word)
        if good:
          # print(word)
          # print("GOD IS GOOD")
          good2 = True
          if word[0] != "-" and word[-1] != "-" and word.count("-") < 2:
            for i in range(1, len(word)-1):
              if word[i] == "-" and (word[i-1] in ["!", ".", ","] or word[i+1] in ["!", ".", ","]):
                good2 = False
            # print("yerr")
            if good2:
              print(word)
              cnt += 1
          elif word.count("-") == 0:
            print(word)
            # print("awiojeaoiwef", cnt)
            cnt += 1
            # print(cnt, "!!!")
    
    return cnt
        