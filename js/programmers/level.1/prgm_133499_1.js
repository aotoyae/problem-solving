function solution(babbling) {
  let count = 0;

  for (let word of babbling) {
    if (/(aya|ye|woo|ma)\1+/g.test(word)) continue;
    if (/^(aya|ye|woo|ma)+$/g.test(word)) count++;
  }

  return count;
}
