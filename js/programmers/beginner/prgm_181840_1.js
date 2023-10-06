function solution(num_list, n) {
  let answer = 0;
  for (i of num_list) {
    if (i === n) {
      answer = 1;
    }
  }
  return answer;
}
