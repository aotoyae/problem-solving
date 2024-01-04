function solution(n) {
  const arr = String(n).split("");
  let answer = 0;
  for (let i of arr) {
    answer += +i;
  }
  return answer;
}
