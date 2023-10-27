function solution(sides) {
  let result = 0;
  const min = Math.min(...sides);
  const max = Math.max(...sides);

  for (x = max - min + 1; x <= max; x++) {
    result += 1;
  }
  for (x = max + 1; x < min + max; x++) {
    result += 1;
  }
  return result;
}
