function solution(angle) {
  if (90 > angle) return 1;
  else if (angle === 90) return 2;
  else if (180 > angle) return 3;
  else return 4;
}
