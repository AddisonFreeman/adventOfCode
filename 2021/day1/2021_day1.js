let list = document.querySelector("body > pre").innerHTML.split("\n")
list = list.map((x, idx, arr) => { return parseInt(x) }).filter( x => !Number.isNaN(x) )
console.log(list)
let count = 0;
list.forEach((x, idx, arr) => { 
    if(idx === arr.length -1)
        return
    if (arr[idx+1] > x) {
        count++ 
    }
    console.log(`idx ${idx} is ${arr[idx+1]} > ${x} = ${count}`)
})
console.log(count)