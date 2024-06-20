#!/usr/bin/node


exports.converter = function(base) {
  return function(number) {
    if (number === 0) {
      return '0';
    }

    function convert(number) {
      if (number === 0) {
        return '';
      }
      const remainder = number % base;
      return convert(Math.floor(number / base)) + (remainder < 10 ? remainder : String.fromCharCode(remainder + 87));
    }

    return convert(number);
  };
};
