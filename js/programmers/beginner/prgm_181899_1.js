function solution(start_num, end_num) {
  let answer = [];
  for (i = 0; i <= start_num - end_num; i++) {
    answer.push(start_num - i);
  }
  return answer;
}
