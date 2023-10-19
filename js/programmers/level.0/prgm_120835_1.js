function solution(emergency) {
  let answer = emergency.slice().sort((a, b) => b - a);
  return emergency.map((a) => answer.indexOf(a) + 1);
}
