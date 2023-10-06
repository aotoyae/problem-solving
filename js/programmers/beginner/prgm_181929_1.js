function solution(num_list) {
  let answer = 1;
  let answer2 = 0;
  for (i of num_list) {
    answer *= i;
    answer2 += i;
  }
  return answer < answer2 * answer2 ? 1 : 0;
}
