function solution(n, m, section) {
  let arr = new Array(n).fill(0);
  let answer = 0;

  for (let i of section) arr[i] = 1;

  for (let j = 0; j < arr.length; j++) {
    if (arr[j] === 1) {
      for (let k = j; k < j + m; k++) {
        arr[k] = 0;
      }
      answer++;
    }
  }

  return answer;
}
