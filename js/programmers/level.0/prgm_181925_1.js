function solution(numlog) {
  let answer = [];
  for (i = 0; i < numlog.length; i++) {
    if (numlog[i] - numlog[i + 1] === -1) {
      answer.push("w");
    }
    if (numlog[i] - numlog[i + 1] === 1) {
      answer.push("s");
    }
    if (numlog[i] - numlog[i + 1] === -10) {
      answer.push("d");
    }
    if (numlog[i] - numlog[i + 1] === 10) {
      answer.push("a");
    }
  }
  return answer.join("");
}
