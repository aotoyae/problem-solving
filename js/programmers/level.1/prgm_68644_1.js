function solution(numbers) {
  let answer = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i !== j) {
        num = numbers[i] + numbers[j];
        if (!answer.includes(num)) answer.push(num);
      }
    }
  }

  return answer.sort((a, b) => a - b);
}
