function solution(arr) {
  let answer = 1;
  for (i = 0; i < arr.length; i++) {
    for (j = 0; j < arr.length; j++) {
      if (arr[i][j] !== arr[j][i]) answer = 0;
    }
  }
  return answer;
}
