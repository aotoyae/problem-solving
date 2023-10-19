function solution(n) {
  let result = [];
  let i = 2;

  while (n >= 2) {
    if (n % i === 0) {
      result.push(i);
      n = n / i;
    } else i++;
  }
  return [...new Set(result)];
  // set = new Set(result)
  // lastArr = [...set]
  // >> 다시 전개 연산자를 통해 배열로 변환해줘야 한다
}
