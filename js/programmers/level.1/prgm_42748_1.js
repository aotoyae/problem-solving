function solution(array, commands) {
  let answer = [];

  for (let i = 0; i < commands.length; i++) {
    const start = commands[i][0] - 1;
    const end = commands[i][1];
    const k = commands[i][2] - 1;
    let nums = array.slice(start, end).sort((a, b) => a - b);

    answer.push(nums[k]);
  }

  return answer;
}
