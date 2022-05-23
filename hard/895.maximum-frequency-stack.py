class FreqStack {
    map<int, vector<int>> stk;
    map<int, int> freq;
public:
    FreqStack() {}
    
    void push(int val) {
      freq[val]++;
      if (stk.find(freq[val]) == stk.end()) {
        vector<int> temp;
        stk[freq[val]] = temp;
      }
      stk[freq[val]].push_back(val);
    }
    
    int pop() {
      auto ind = stk.rbegin()->first;
      if (stk[ind].empty()) {
        stk.erase(ind);
        ind = stk.rbegin()->first;
      }
      int ans = stk[ind][stk[ind].size()-1];
      stk[ind].pop_back();
      freq[ans]--;
      return ans;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */