function longestStrChain(words: string[]): number {
  let isPred = (pred: string, anc: string): boolean => {
    let i = 0,
      j = 0,
      skipped = false;
    while (i < pred.length && j < anc.length) {
      if (pred[i] == anc[j]) {
        i++;
        j++;
      } else if (!skipped) {
        j++;
        skipped = true;
      } else {
        return false;
      }
    }
    return true;
  };

  let wordsL = [...Array(18)].map((temp) => new Set<string>());
  let wordsVis = new Map<string, number>();
  var ans = 0;
  for (let word of words) {
    wordsL[word.length].add(word);
  }

  let rec = (cs: string, cl: number) => {
    ans = Math.max(ans, cl);
    if (!wordsVis.has(cs)) {
      let currBest = 1;
      for (let tempS of wordsL[cs.length + 1]) {
        if (isPred(cs, tempS)) {
          currBest = Math.max(currBest, rec(tempS, cl + 1) + 1);
        }
      }
      wordsVis.set(cs, currBest);
      ans = Math.max(ans, currBest);
      return currBest;
    }
    return wordsVis.get(cs);
  };

  for (let word of words) {
    rec(word, 1);
  }

  return ans;
}
