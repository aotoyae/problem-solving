function solution(rank, attendance) {
  let result = [];

  for (i = 0; i < rank.length; i++) {
    if (attendance[i] === true) {
      result.push([rank[i], i]);
    }
  }

  result.sort((a, b) => a[0] - b[0]);
  return result[0][1] * 10000 + result[1][1] * 100 + result[2][1];
}
