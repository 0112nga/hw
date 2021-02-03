const url = require('url');

const myUrl = new URL('http://mywebsite.com:8000/hello.html?id=100&status=active');

//Serialized URL
console.log(myUrl.href); //http://mywebsite.com:8000/hello.html?id=100&status=active
console.log(myUrl.toString()); //same

//host (root domain)
console.log(myUrl.host); //mywebsite.com:8000
console.log(myUrl.hostname) //do not include the port : mywebsite.com

//pathname
console.log(myUrl.pathname); ///hello.html

//serialized query
console.log(myUrl.search); //?id=100&status=active

// Params obj
console.log(myUrl.searchParams);
// add param
myUrl.searchParams.append('abc', '123');
console.log(myUrl.searchParams);
console.log(myUrl.href);

//loop through params
myUrl.searchParams.forEach((value, name)=> console.log(`${name}: ${value}`));



