function solution(hp) {
  let first = ~~(hp / 5);
  let second = ~~((hp % 5) / 3);
  let third = (hp % 5) % 3;

  return first + second + third;
}
