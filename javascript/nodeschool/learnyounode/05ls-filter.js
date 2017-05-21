
var fs = require('fs')
var path = require('path')

var dir = process.argv[2]
// var dir = '.'
var extension = '.' + process.argv[3]
// var extension = '.js'


fs.readdir(dir, (err, files) => {
  if (err) return console.error(err)
  for (var file of files){
    // split = file.split('.')
    // if (split[1] === extension){
    //   console.log(file)
    // }
    if (path.extname(file) === extension){
      console.log(file)
    }
  }
})
