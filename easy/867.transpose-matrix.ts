function transpose(matrix: number[][]): number[][] {
  let R = matrix.length,
    C = matrix[0].length;
  let ans = [...Array(C)].map((temp) => Array(R));

  for (let row = 0; row < R; row++) {
    for (let col = 0; col < C; col++) {
      ans[col][row] = matrix[row][col];
    }
  }

  return ans;
}
