function solution(arr) {
  const row = arr.length;
  const col = arr[0].length;

  if (row > col) {
    const add = Array(row - col).fill(0);
    return arr.map((a) => [...a, ...add]);
  }
  if (row < col) {
    for (i = 0; i < col - row; i++) {
      const add = Array(col).fill(0);
      arr.push(add);
    }
  }
  return arr;
}
