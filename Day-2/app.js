// Your JavaScript code here
// Day 02
// write a function that returns the sum of two numvers
//  write a funtion that returns the sum of all numbers regardless of   params

console.log("day 02");

const totalSum = (...parms) => {
  let total = 0;
  parms.map((element) => {
    total += element;
  });

  return total;
};

console.log(totalSum(4, 6, 85));
