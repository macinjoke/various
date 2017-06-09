
// console.log(promisify);
const pify = require('pify');
const fs = require('fs');

pify(fs.readFile)('./promise_ex6.js', 'utf-8').then(out => {
    console.log(out);
});
