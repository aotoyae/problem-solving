function solution(arr1, arr2) {
  let arr1Add = arr1.reduce((a, b) => a + b);
  let arr2Add = arr2.reduce((a, b) => a + b);

  if (arr1.length === arr2.length) {
    if (arr1Add > arr2Add) {
      return 1;
    } else if (arr1Add < arr2Add) {
      return -1;
    } else {
      return 0;
    }
  }
  return arr1.length > arr2.length ? 1 : -1;
}
