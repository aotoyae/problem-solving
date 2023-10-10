function solution(rsp) {
  return [...rsp]
    .map((a) => {
      switch (+a) {
        case 2:
          return 0;
        case 0:
          return 5;
        default:
          return 2;
      }
    })
    .join("");
  // 삼항연산자 여러개 활용
  // return rsp.split("").map((v) => v==="2" ? 0 : (v==="0" ? 5 : 2)).join("")
}
