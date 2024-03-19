function solution(clothes) {
  let obj = {};
  let count = 1;

  clothes.forEach((item) => {
    const [name, type] = item;
    obj[type] ? obj[type]++ : (obj[type] = 1);
  });

  for (const key in obj) {
    count *= obj[key] + 1;
  }

  return count - 1;
}
