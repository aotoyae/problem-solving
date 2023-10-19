function solution(order) {
  let array = [...order];
  let result = 0;
  for (i = 0; i < order.length; i++) {
    array[i].includes("cafelatte") ? (result += 5000) : (result += 4500);
  }
  return result;
}
