function solution(d, budget) {
  d.sort((a, b) => a - b);
  let i = 0;

  for (let n of d) {
    budget -= n;

    if (budget < 0) break;
    i++;
  }

  return i;
}
