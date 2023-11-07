function solution(common) {
  let gap = [];
  let result = 0;
  for (i = 0; i < 2; i++) {
    gap.push(common[i + 1] - common[i]);
  }
  if (gap[0] === gap[1]) {
    return (result = common[common.length - 1] + gap[0]);
  } else {
    return (result = common[common.length - 1] * (gap[1] / gap[0]));
  }
}
