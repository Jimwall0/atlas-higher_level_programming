#!/usr/bin/node
exports.esrever = function (list) {
  const dummylist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    dummylist.push(list[i]);
  }
  return (dummylist);
};
