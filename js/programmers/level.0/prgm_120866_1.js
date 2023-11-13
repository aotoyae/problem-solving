function solution(board) {
  const dx = [1, 0, -1, 0, 1, 1, -1, -1];
  const dy = [0, 1, 0, -1, 1, -1, 1, -1];
  const n = board.length;
  let result = n * n;
  const bomb = [];

  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      if (board[i][j] === 1) {
        bomb.push([i, j]);
        result--;
      }
    }
  }

  if (result === 0) return 0;

  bomb.forEach((v) => {
    for (k = 0; k < 8; k++) {
      const nx = v[0] + dx[k];
      const ny = v[1] + dy[k];

      if (nx >= 0 && ny >= 0 && nx < n && ny < n && board[nx][ny] === 0) {
        board[nx][ny] = 1;
        result--;
      }
    }
  });

  return result;
}
