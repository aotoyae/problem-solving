function solution(sizes) {
  let width = [];
  let height = [];

  for (let i = 0; i < sizes.length; i++) {
    if (sizes[i][0] < sizes[i][1]) {
      newSize = sizes[i][0];
      sizes[i][0] = sizes[i][1];
      sizes[i][1] = newSize;
    }
    width.push(sizes[i][0]);
    height.push(sizes[i][1]);
  }
  return Math.max(...width) * Math.max(...height);
}
