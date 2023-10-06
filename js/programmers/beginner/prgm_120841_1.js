function solution(dot) {
  let [dot1, dot2] = dot;
  if (dot1 < 0 && dot2 < 0) {
    return 3;
  } else if (dot1 < 0 && dot2 > 0) {
    return 2;
  } else if (dot1 > 0 && dot2 < 0) {
    return 4;
  } else {
    return 1;
  }
}
