const calculate = function (n: number) {
  let sum: number = 0;
  for (let elem = 1; elem <= n; elem++) {
    sum += Math.pow(elem, 2);
  }
  return sum;
};
console.log(calculate(6));
