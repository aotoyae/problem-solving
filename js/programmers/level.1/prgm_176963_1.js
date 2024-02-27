function solution(name, yearning, photo) {
  const obj = {};
  const result = [];

  for (let i = 0; i < name.length; i++) {
    obj[name[i]] = yearning[i];
  }

  for (let j = 0; j < photo.length; j++) {
    let count = 0;

    for (let k = 0; k < photo[j].length; k++) {
      count += obj[photo[j][k]] || 0;
    }

    result.push(count);
  }

  return result;
}
