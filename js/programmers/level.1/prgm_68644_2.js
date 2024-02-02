function solution(numbers) {
  let arr = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      num = numbers[i] + numbers[j];
      arr.push(num);
    }
  }

  set = [...new Set(arr)];

  return set.sort((a, b) => a - b);
}
