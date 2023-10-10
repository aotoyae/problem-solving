function solution(my_string) {
  let answer = [];
  for (i = 1; i <= my_string.length; i++) {
    answer.push(my_string.substr(my_string.length - i));
  }
  return answer.sort();
}
