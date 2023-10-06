function solution(num_list) {
  for (i = 0; i < num_list.length; i++) {
    if (num_list[i] < 0) {
      return i;
    }
  }
  return -1;
  // 한 줄로 가능
  // return num_list.findIndex((v) => v < 0);
}
