function solution(arr, divisor) {
  let result = arr.filter((num) => num % divisor === 0);

  return result.length ? result.sort((a, b) => a - b) : [-1];
}
