
class MaxStack {
public:
    map<int, vector<list<int>::iterator>>  valCnt;
    list<int> stk;
  
    MaxStack() {
        
    }
    
    void push(int x) {
      stk.push_back(x);
      valCnt[x].push_back(prev(stk.end()));
    }
    
    int pop() {
      int top = stk.back();
      stk.erase(valCnt[top][valCnt[top].size()-1]);
      valCnt[top].pop_back();
      if (valCnt[top].size() == 0) valCnt.erase(top);
      return top;
    }
    
    int top() {
      return stk.back();
    }
    
    int peekMax() {
      return valCnt.rbegin()->first;

    }
    
    int popMax() {
      int removed = valCnt.rbegin()->first;
      stk.erase(valCnt[removed][valCnt[removed].size()-1]);
      valCnt[removed].pop_back();
      if (valCnt[removed].size() == 0) valCnt.erase(removed);
      return removed;
    }
};

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack* obj = new MaxStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->peekMax();
 * int param_5 = obj->popMax();
 */