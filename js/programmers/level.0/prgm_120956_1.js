function solution(babbling) {
  let result = 0;
  const babble = /^(aya|ye|woo|ma)+$/;

  babbling.forEach((v) => {
    if (babble.test(v)) result++;
  });

  return result;
}
