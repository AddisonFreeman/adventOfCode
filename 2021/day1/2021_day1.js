// let list = document.querySelector("body > pre").innerHTML.split("\n")
// list = list.map((x, idx, arr) => { return parseInt(x) }).filter( x => !Number.isNaN(x) )
// console.log(list)
// let count = 0;
// list.forEach((x, idx, arr) => { 
//     if(idx === arr.length -1)
//         return
//     if (arr[idx+1] > x) {
//         count++ 
//     }
//     console.log(`idx ${idx} is ${arr[idx+1]} > ${x} = ${count}`)
// })
// console.log(count)


let list = document.querySelector("body > pre").innerHTML.split("\n")
list = list.map((x, idx, arr) => { return parseInt(x) }).filter( x => !Number.isNaN(x) )

tup = list.map((x, idx) => {
    return [x, list[idx+1]]
});

trip = list.map((x, idx) => {
    if(idx < list.length-2) 
        return [x, list[idx+1], list[idx+2]]
}).filter((x) => x !== undefined );

let tripSum = trip.map(x => x[0] + x[1] + x[2]);

let count = 0;
tripSum.forEach((x, idx, arr) => { 
    if(idx === arr.length -1)
        return
    if (arr[idx+1] > x) {
        count++ 
    }
    console.log(`idx ${idx} is ${arr[idx+1]} > ${x} = ${count}`)
})
