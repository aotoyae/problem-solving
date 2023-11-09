function solution(num, total) {
  let result = [];
  const averageNum = Math.ceil(total / num);
  const minusNum = Math.trunc(num / 2);
  const startNum = averageNum - minusNum;

  for (i = 0; i < num; i++) {
    result.push(startNum + i);
  }

  return result;
}
