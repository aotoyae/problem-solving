function solution(s) {
  let count = 0;
  let zero = 0;

  while (s !== '1') {
    count++;
    arr = s.split('0');
    zero += arr.length - 1;
    newNum = arr.join('').length;
    s = newNum.toString(2);
  }

  return [count, zero];
}
