function solution(lines) {
  let result = 0;
  let lineMap = new Array(200).fill(0);

  for (i = 0; i < 3; i++) {
    let left = lines[i][0];
    let right = lines[i][1];

    for (j = left; j < right; j++) {
      lineMap[j + 100]++;
    }
  }

  for (i in lineMap) {
    if (lineMap[i] > 1) {
      result++;
    }
  }

  return result;
}
