

var fs = require('fs');

// fs.writeFile('test.txt', 'hello from js', (err) => {
//     if (err) throw err;
//     console.log('The file has been saved');
// });


// fileString = fs.readFileSync('test.txt', 'utf8');
var file = process.argv[2];
fileString = fs.readFileSync(file, 'utf8');

split = fileString.split('\n');
// for (str of split){
//     console.log(str)
// }

console.log(split.length - 1);



