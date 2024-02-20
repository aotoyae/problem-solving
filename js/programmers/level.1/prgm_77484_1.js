function solution(lottos, win_nums) {
  const correct = lottos.filter((num) => win_nums.includes(num)).length;
  const zeros = lottos.filter((num) => num === 0).length;

  let min = 7 - correct >= 6 ? 6 : 7 - correct;
  let max = min - zeros < 1 ? 1 : min - zeros;

  return [max, min];
}
