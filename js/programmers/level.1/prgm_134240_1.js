function solution(food) {
  let arr1 = [];

  for (i = 1; i < food.length; i++) {
    for (j = 1; j <= Math.floor(food[i] / 2); j++) {
      arr1.push(i);
    }
  }

  return [...arr1, 0, ...arr1.reverse()].join("");
}
