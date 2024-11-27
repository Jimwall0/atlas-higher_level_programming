#!/usr/bin/node
exports.logMe = function (item) {
  console.log(console.count('logMe') + ': ' + item);
};
