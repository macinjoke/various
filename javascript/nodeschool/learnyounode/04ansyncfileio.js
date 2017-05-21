

var fs = require('fs')

var file = process.argv[2];
fs.readFile(file, 'utf8', function (err, fileContents) {
// fs.readFile('test.txt', 'utf8', function (err, fileContents) {
  if (err) throw err

  split = fileContents.split('\n')
  console.log(split.length - 1)

})




