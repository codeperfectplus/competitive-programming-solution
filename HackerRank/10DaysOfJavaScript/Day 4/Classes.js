'use strict'
class Polygon{
    constructor(sides){
        this.sides = sides;
        this.perimeter = this.perimeter;
    }
    perimeter() {
        let sum = 0;
        for(let i =0;i<this.sides.length;i++) {
            sum = sum + this.sides[i];
        }
        return sum;
    }
}

const triangle = new Polygon([3,4,5]);
console.log(triangle.perimeter());