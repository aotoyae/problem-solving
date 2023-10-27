function solution(arr) {
  let stk = [];
  for (i = 0; i < arr.length; i++) {
    stk[stk.length - 1] === arr[i] ? stk.pop() : stk.push(arr[i]);
  }
  return stk.length ? stk : [-1];
}
