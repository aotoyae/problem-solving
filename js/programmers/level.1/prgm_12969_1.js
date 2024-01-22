process.stdin.setEncoding("utf8");
process.stdin.on("data", (data) => {
  const arr = data.split(" ");
  const a = Number(arr[0]);
  const b = Number(arr[1]);

  for (let i = 0; i < b; i++) {
    let result = [];

    for (let j = 0; j < a; j++) {
      result.push("*");
    }

    console.log(result.join(""));
  }
});
