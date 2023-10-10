function solution(s1, s2) {
  const answer = s1.filter((item) => s2.includes(item));
  return answer.length;
}
