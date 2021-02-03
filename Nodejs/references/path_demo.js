const path = require('path');

//Base file name
console.log(__filename); //C:\Users\asus\Downloads\Nodejs\references\path_demo.js
console.log(path.basename(__filename)); //path_demo.js

//directory name
console.log(path.dirname(__filename)); //C:\Users\asus\Downloads\Nodejs\references

//File extension
console.log(path.extname(__filename)); //.js

// create path obj
console.log(path.parse(__filename));
//{
//     root: 'C:\\',
//     dir: 'C:\\Users\\asus\\Downloads\\Nodejs\\references',
//     base: 'path_demo.js',
//     ext: '.js',
//     name: 'path_demo'
//   }
 
console.log(path.parse(__filename).base); //path_demo.js

//concatenate paths
console.log(path.join(__dirname, 'test', 'hello.html')); //C:\Users\asus\Downloads\Nodejs\references\test\hello.html