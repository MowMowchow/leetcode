class Solution {
public:
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
      
    const int BIGGIE = 9999999999;
    int m = edges.size(), a, b, w, dist1[10010], dist2[10010], curr, node, weight, kur1, kur2;
    vector<vector<int> > adj[10010];

    
    for (int i = 0; i < m; i++){
        a = edges[i][0]; b = edges[i][1];
        adj[a].push_back({b, time});
        adj[b].push_back({a, time});
    }
    for (int i = 0; i <= n; i++){
        dist1[i] = BIGGIE; dist2[i] = BIGGIE;
    }
      
      
    priority_queue<int, vector<int>, greater<int>> queue; queue.push(1);
    dist1[1] = 0;
    while (!queue.empty()){
        curr = queue.top(); queue.pop();

        for (auto temp: adj[curr]){
            node = temp[0]; weight = temp[1];
            kur1 = dist1[curr] + weight; kur2 = dist2[curr] + weight;
          
            if ((dist1[curr]/change) % 2) kur1 += ((dist1[curr]/change)+1)*change - dist1[curr];
            if ((dist2[curr]/change) % 2) kur2 += ((dist2[curr]/change)+1)*change - dist2[curr];

            if (kur1 < dist1[node]){
                dist2[node] = dist1[node];
                dist1[node] = kur1;
                queue.push(node);
            }
            else if (dist1[node] != kur1 && kur1 < dist2[node]){
                dist2[node] = kur1;
                queue.push(node);
            }
            else if (dist1[node] != kur2 && kur2 < dist2[node]){
                dist2[node] = kur2;
                queue.push(node);
            }
        }
    }
       
    return dist2[n];
}
};