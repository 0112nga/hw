const http = require('http');

//create server Obj

http.createServer((req, res) => {
    //write response
    res.write('hello world');
    res.end();
}).listen(5000, () => console.log('Server running'));