#!/usr/bin/node
exports.converter = function (base) {
  let result = 0;

  return function (number) {
    result = parseInt(number, 10).toString(base);
    return result;
  };
};
