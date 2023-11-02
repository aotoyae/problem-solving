function solution(polynomial) {
  const newArray = polynomial.split(" + ");

  let numX = 0;
  let num = 0;

  newArray.forEach((item) => {
    if (item.includes("x")) {
      const xArray = item.split("x");
      if (xArray[0] === "") {
        numX += 1;
      }
      if (xArray[0] !== "") {
        numX += Number(xArray[0]);
      }
    } else {
      num += Number(item);
    }
  });
  if (numX !== 0 && num !== 0) {
    return numX === 1 ? `x + ${num}` : `${numX}x + ${num}`;
  }
  if (numX !== 0 && num === 0) {
    return numX === 1 ? `x` : `${numX}x`;
  }
  if (numX === 0 && num !== 0) {
    return `${num}`;
  }
  return `0`;
}
