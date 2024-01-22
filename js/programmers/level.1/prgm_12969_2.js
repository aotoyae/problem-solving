process.stdin.setEncoding("utf8");
process.stdin.on("data", (data) => {
  const arr = data.split(" ");
  const a = Number(arr[0]);
  const b = Number(arr[1]);

  console.log(`${"*".repeat(a)}\n`.repeat(b));
});
