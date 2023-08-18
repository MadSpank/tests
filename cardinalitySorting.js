const arr = [3, 4, 16, 2, 1, 26];

const onesCount = (num) => {
  let count = 0;
  const binaryNum = num.toString(2);

  binaryNum.split("").forEach((char) => (count += char === "1" ? 1 : 0));

  return count;
};

const compareFn = (aObj, bObj) => {
  let result = null;
  const elA = parseInt(aObj[0]);
  const elB = parseInt(bObj[0]);
  const countA = aObj[1];
  const countB = bObj[1];
  if (countA === countB) {
    if (elA < elB) {
      result = -1;
    }
    if (elA > bObj) {
      result = 1;
    }
  }
    if (countA > countB) {
      result = 1;
    }

    if (countA < countB) {
      result = -1;
    }
  return result;
};

const sortArray = (arr) => {
  const numberedObj = arr.reduce(
    (acc, num) => ({ ...acc, [num]: onesCount(num) }),
    {}
  );
  console.log(numberedObj);
  const result = Object.entries(numberedObj)
    .sort(compareFn)
    .map((sortedArr) => sortedArr[0]);
  return result;
};

console.log(sortArray(arr));
