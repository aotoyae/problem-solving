function solution(n, lost, reserve) {
  let lostNum = lost.filter((v) => !reserve.includes(v)).sort((a, b) => a - b);
  let reserveNum = reserve
    .filter((v) => !lost.includes(v))
    .sort((a, b) => a - b);

  reserveNum.forEach((base) => {
    if (lostNum.includes(base - 1)) {
      lostNum = lostNum.filter((v) => v !== base - 1);
    } else if (lostNum.includes(base + 1)) {
      lostNum = lostNum.filter((v) => v !== base + 1);
    }
  });

  return n - lostNum.length;
}
