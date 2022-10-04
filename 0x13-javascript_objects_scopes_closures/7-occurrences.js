#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const newList = list.filter(item => item === searchElement);
  return newList.length;
};
