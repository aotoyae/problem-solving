function solution(myStr) {
  const answer = myStr.split(/[abc]/g).filter(Boolean);
  return answer.length ? answer : ["EMPTY"];
}
