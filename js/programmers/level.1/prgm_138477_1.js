function solution(k, score) {
  let honor = [];
  let answer = [];

  score.forEach((num) => {
    honor.push(num);
    honor.sort((a, b) => b - a);

    if (honor.length >= k) {
      answer.push(honor[k - 1]);
    } else {
      answer.push(honor.at(-1));
    }
  });
  return answer;
}
