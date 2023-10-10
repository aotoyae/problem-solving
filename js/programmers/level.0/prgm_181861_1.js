function solution(arr) {
  let answer = [];
  for (i = 0; i < arr.length; i++) {
    for (j = 1; j <= arr[i]; j++) {
      answer.push(arr[i]);
    }
  }
  return answer;
}
