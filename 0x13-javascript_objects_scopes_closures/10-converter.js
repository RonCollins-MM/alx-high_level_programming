#!/usr/bin/node
exports.converter = function (base) {
  return value => value.tostring(base);
};
