
// https://github.com/maxogden/art-of-node#callbacks


var fs = require('fs')
var myNumber = undefined

function addOne(callback) {
  fs.readFile('number.txt', function doneReading(err, fileContents) {
    myNumber = parseInt(fileContents, 10)
    myNumber++
    callback()
  })
  console.log('tekitou')
}

function logMyNumber() {
  console.log(myNumber)
}

addOne(logMyNumber)
