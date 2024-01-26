function solution(sizes) {
  let width = 0;
  let height = 0;

  sizes.forEach((size) => {
    const [testWidth, testHeight] = size.sort((a, b) => a - b);
    if (testWidth > width) width = testWidth;
    if (testHeight > height) height = testHeight;
  });

  return width * height;
}
