
function printMaxActivities(start, finish) {
    let n = start.length;
    let i = 0;

    let results = [];
    results.push(i);

    for (let j=0; j<n; j++){
        if (start[j] >= finish[i]) {
            results.push(j);
        }
    }
    return results;
}

let start  = [10, 12, 20]
let finish = [20, 25, 30]

res = printMaxActivities(start, finish);
console.log(res);