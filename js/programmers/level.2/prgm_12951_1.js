function solution(s) {
  let arr = s.split(' ');
  let arr2 = arr.map(
    (word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
  );

  return arr2.join(' ');
}
