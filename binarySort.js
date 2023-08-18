const arr = [3, 4, 6, 8];

const onesCount = (num) => {
  let count = 0;
  const binaryNum = num.toString(2);

  binaryNum.split("").forEach((char) => (count += char === "1" ? 1 : 0));

  return count;
};

const compareFn = (aObj, bObj) => {
  if (aObj[1] === bObj[1]) {
    if (aObj[0] < bObj[0]) {
      return -1;
    }
    if (aObj[0] > bObj[0]) {
      return 1;
    }
  }
  if (aObj[1] > bObj[1]) {
    return 1;
  }

  if (aObj[1] < bObj[1]) {
    return -1;
  }
};

const sortArr = (arr) => {
  const countObject = arr.map((num) => {
    return [num, onesCount(num)];
  });
  const result = countObject.sort(compareFn).map((obj) => obj[0]);
  console.log(result);
};

sortArr(arr);
