class DetectSquares {
  public xCoors;
  public yCoors;
  public coors;

  constructor() {
    this.xCoors = [...Array(1001)].map((arr) => Array());
    this.yCoors = [...Array(1001)].map((arr) => Array());
    this.coors = [...Array(1001)].map((arr) => Array(1001).fill(0));
  }

  add(point: number[]): void {
    this.xCoors[point[0]].push(point[1]);
    this.yCoors[point[1]].push(point[0]);
    this.coors[point[0]][point[1]]++;
  }

  count(point: number[]): number {
    let res = 0,
      x = point[0],
      y = point[1],
      xl,
      xr;
    let yVis = new Set<number>();

    this.xCoors[x].forEach((yCoor) => {
      if (y != yCoor && !yVis.has(yCoor)) {
        yVis.add(yCoor);
        xl = x - Math.abs(y - yCoor);
        if (xl >= 0) {
          res +=
            this.coors[x][yCoor] * this.coors[xl][y] * this.coors[xl][yCoor];
        }
        xr = x + Math.abs(y - yCoor);
        if (xr <= 1000) {
          res +=
            this.coors[x][yCoor] * this.coors[xr][y] * this.coors[xr][yCoor];
        }
      }
    });
    return res;
  }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * var obj = new DetectSquares()
 * obj.add(point)
 * var param_2 = obj.count(point)
 */
