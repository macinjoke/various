


li = process.argv;

// var result = 0;
// for(let i in li){
//     if(i <= 1){
//         continue;
//     }
//     result += Number(li[i]);
// }

var result = 0;
for(let i = 2; i < li.length; i++){
  result += Number(li[i])
}

console.log(result);

