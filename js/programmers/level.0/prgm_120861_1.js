function solution(keyinput, board) {
  let result = [0, 0];
  const row = board[0] / 2;
  const column = board[1] / 2;

  for (i = 0; i < keyinput.length; i++) {
    if (keyinput[i] === "right" && result[0] + 1 < row) result[0]++;
    if (keyinput[i] === "left" && result[0] - 1 > -row) result[0]--;
    if (keyinput[i] === "up" && result[1] + 1 < column) result[1]++;
    if (keyinput[i] === "down" && result[1] - 1 > -column) result[1]--;
  }
  return result;
}
