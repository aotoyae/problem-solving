function solution(array) {
  if (array.length === 1) {
    return array[0];
  }

  const obj = {};
  const result = [];

  array.forEach((n) => {
    obj[n] = ++obj[n] || 1;
  });

  for (let key in obj) {
    result.push([key, obj[key]]);
  }

  result.sort((a, b) => b[1] - a[1]);

  if (result.length > 1 && result[0][1] === result[1][1]) return -1;

  return Number(result[0][0]);
}
