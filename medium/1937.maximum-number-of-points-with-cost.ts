function maxPoints(points: number[][]): number {
  let [R, C] = [points.length, points[0].length];
  let dp = [...Array(R+1)].map(row => Array(C).fill(0));
  let rBest, lBest, ans = 0;
  for (let row = 1; row <= R; row++){
    // r to l
    rBest = C-1;
    for (let col = C-1; col > -1; col--){
      if (dp[row-1][col] > dp[row-1][rBest]-(rBest-col)) {
        rBest = col;
      }
      dp[row][col] = Math.max(dp[row][col], dp[row-1][rBest]-(rBest-col)+points[row-1][col]);
      ans = Math.max(ans, dp[row][col]);
    }
    
    // l to r
    lBest = 0;
    for (let col = 0; col < C; col++){
      if (dp[row-1][col] > dp[row-1][lBest]-(col-lBest)) {
        lBest = col;
      }
      dp[row][col] = Math.max(dp[row][col], dp[row-1][lBest]-(col-lBest)+points[row-1][col]);
      ans = Math.max(ans, dp[row][col]);
    }
  }
    
  return ans;
};