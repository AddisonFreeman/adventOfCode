let sortedList = document.getElementsByTagName("pre")[0].innerHTML.split("\n").sort((a,b) => a - b);
console.log(sortedList)
let sort = function(sortedList, head, last) {
    let res = sortedList[head] + sortedList[last];
    console.log(res)
    if(res === 2020) {
        console.log('YOU WIN', head, last, head+last);
    } else if(res > 2020) {
        sort(sortedList, head, last-1)
    } else if(res < 2020) {
        sort(sortedList, head+1, last)
    }
}
sort(sortedList,0,sortedList.length-1) 