function solution(num_list) {
  let even = [];
  let odd = [];
  for (i = 0; i < num_list.length; i++) {
    if (num_list[i] % 2 === 0) {
      even.push(num_list[i]);
    } else {
      odd.push(num_list[i]);
    }
  }
  return Number(even.join("")) + Number(odd.join(""));
}
