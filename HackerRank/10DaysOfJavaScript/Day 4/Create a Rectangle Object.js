/*
* Complete the Rectangle function
*/
function Rectangle(a, b) {
    this.length = a;
    this.width = b;
    this.perimeter = 2 * (this.length + this.width);
    this.area = this.length * this.width;
}
const rec = new Rectangle(4,5);
console.log(rec.perimeter);