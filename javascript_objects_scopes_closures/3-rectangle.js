#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w <= 0 || w === undefined || h <= 0 || h === undefined) {
      // This Block does nothing
    } else {
      this.width = w;
      this.height = h;
    }
  }

    print () {
        for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
        }
    }
};
module.exports = Rectangle;
