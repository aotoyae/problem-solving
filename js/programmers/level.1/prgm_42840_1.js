function solution(answers) {
  const one = [1, 2, 3, 4, 5];
  const two = [2, 1, 2, 3, 2, 4, 2, 5];
  const three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let total = [0, 0, 0];
  let answer = [];

  for (let i = 0; i < answers.length; i++) {
    if (one[i % one.length] === answers[i]) total[0]++;
    if (two[i % two.length] === answers[i]) total[1]++;
    if (three[i % three.length] === answers[i]) total[2]++;
  }

  const max = Math.max(...total);

  for (let i = 0; i < total.length; i++) {
    if (total[i] === max) answer.push(i + 1);
  }

  return answer;
}
