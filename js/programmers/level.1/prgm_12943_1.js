function solution(num) {
  if (num === 1) {
    return 0;
  } else {
    let count = 0;

    while (num !== 1 && count !== 500) {
      num % 2 === 0 ? (num /= 2) : (num = num * 3 + 1);
      count++;
    }
    return num === 1 ? count : -1;
  }
}
