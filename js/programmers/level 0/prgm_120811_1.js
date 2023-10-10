function solution(array) {
  let answer = array.sort((a, b) => a - b);
  return answer[Math.floor(answer.length / 2)];
  // return array.sort((a, b) => a - b)[Math.floor(answer.length / 2)]
  // >> 한 줄로 가능
}
