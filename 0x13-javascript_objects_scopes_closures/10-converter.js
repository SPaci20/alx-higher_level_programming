#!/usr/bin/node
exports.converter = function (base) {
  this.result = 0;

  return function (number) {
    this.result = parseInt(number, 10).toString(base);
    return this.result;
  };
};
