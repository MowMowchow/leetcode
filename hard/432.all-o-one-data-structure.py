#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#

# @lc code=start
class AllOne {
    map<string, int> sVal;
    map<int, map<string, int> > arr;
public:
    AllOne() {

    }
    
    void inc(string key) {
      if (sVal[key] > 0) arr[sVal[key]].erase(key);
      if (arr[sVal[key]].size() == 0) arr.erase(sVal[key]);
      sVal[key]++;
      arr[sVal[key]][key]++;
    }
    
    void dec(string key) {
      arr[sVal[key]].erase(key);
      if (arr[sVal[key]].size() == 0) arr.erase(sVal[key]);
      sVal[key]--;
      if (sVal[key] == 0) sVal.erase(key);
      else arr[sVal[key]][key]++;
    }
    
    string getMaxKey() {
      if (arr.size() == 0) return "";
      int cnt = arr.rbegin()->first;
      return arr[cnt].begin()->first;
    }
    
    string getMinKey() {
      if (arr.size() == 0) return "";
      int cnt = arr.begin()->first;
      return arr[cnt].begin()->first;
    }
};

# @lc code=end

