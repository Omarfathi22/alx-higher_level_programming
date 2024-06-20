#!/usr/bin/node


exports.converter = function(base) {
  return function convert(number) {
    if (number === 0) {
      return '';
    } else {
      const remainder = number % base;
      return convert(Math.floor(number / base)) + (remainder < 10 ? remainder : String.fromCharCode(remainder + 87));
    }
  };
};
