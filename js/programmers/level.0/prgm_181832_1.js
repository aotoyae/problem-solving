function solution(n) {
  let result = Array.from(Array(n), () => Array(n).fill(0));
  let row = 0;
  let col = 0;
  let num = 1;

  for (i = n; i > 0; i -= 2) {
    for (j = 0; j < i; j++) {
      result[row][col] = num;
      col++;
      num++;
    }
    col--;
    row++;

    for (j = 0; j < i - 1; j++) {
      result[row][col] = num;
      row++;
      num++;
    }
    col--;
    row--;

    for (j = 0; j < i - 1; j++) {
      result[row][col] = num;
      col--;
      num++;
    }
    col++;
    row--;

    for (j = 0; j < i - 2; j++) {
      result[row][col] = num;
      row--;
      num++;
    }
    col++;
    row++;
  }
  return result;
}
