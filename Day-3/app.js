// Your JavaScript code here
// Give a rectangular matrix of characters ,add a border of asterisks (*) to it .

console.log("day 03");

const myfunction = (array) => {
  const makeWall = "*".repeat(array[0].length + 2);
  array.unshift(makeWall);
  array.push(makeWall);

  for (let i = 0; i < array.length; i++) {
    array[i] = "*".concat(array[i], "*");
  }

  console.log(array);
};

myfunction(["abid", "anis"]);
