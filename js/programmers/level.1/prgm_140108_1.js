function solution(s) {
  let firstChar = "";
  let sameCount = 0;
  let deffCount = 0;
  let answer = 0;

  for (let char of s) {
    if (!firstChar) firstChar = char;

    if (firstChar === char) sameCount++;
    else deffCount++;

    if (sameCount === deffCount) {
      answer++;
      sameCount = 0;
      deffCount = 0;
      firstChar = "";
    }
  }
  if (firstChar) answer++;
  return answer;
}
