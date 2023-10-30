function solution(score) {
  let avg = score.map((v) => (v[0] + v[1]) / 2);
  let ranking = [...avg].sort((a, b) => b - a);
  return avg.map((v) => ranking.indexOf(v) + 1);
}
