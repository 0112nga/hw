// const express = require('express');
// const app = express();
// const port = 3000;


// app.get('/tintuc', (req,res)=>{
//     return res.send('hello world123');
// })

// app.listen(port, ()=>{
//     console.log('Listening at port 3000');
// })

// const person = require('./person');

// const p1 = new person('Nga', 20);
// p1.greeting();


// const Logger = require('./logger');

// const logger = new Logger();

// logger.on('message', data => console.log('Called Listener:', data));

// logger.log('Hello World');
// logger.log('sdheufeiuw');

const http = require('http');
const path = require('path');
const fs = require('fs');

const server = http.createServer((req, res)=>{
    // if(req.url === '/'){
    //     fs.readFile(path.join(__dirname, 'public', 'index.html'), (err, content)=>{
    //         if(err) throw err;
    //         res.writeHead(200, { 'Content-Type' : 'text/html' });
    //         res.end(content);
    //     })

    //     // res.writeHead(200, { 'Content-Type' : 'text/html' });
    //     // res.end('<h1>HOME PAGE</h1>');
    // }
    // if(req.url === '/about'){
    //     fs.readFile(path.join(__dirname, 'public', 'about.html'), (err, content)=>{
    //         if(err) throw err;
    //         res.writeHead(200, { 'Content-Type' : 'text/html' });
    //         res.end(content);
    //     })
    // }
    // if(req.url === '/api/users'){
    //     const user = [
    //         {name : 'sdhvbj', age: 30},
    //         {name : 'dsbvhj', age: 52}
    //     ]
    //     res.writeHead(200, {'Content-Type' : 'application/json'});
    //     res.end(JSON.stringify(user));
    // }


    //build file path
    let filePath =path.join(__dirname, 'public', req.url === '/' ? 'index.html' : req.url);
    console.log(req.url);
    // console.log(123);

    //extension of file
    let extname = path.extname(filePath);

    //init Content-Type
    let contentType = 'text/html';

    //check extension and check content type
    switch(extname){
        case '.js':
            contentType = 'text/Javascript';
            break;
        case '.css':
            contentType = 'text/css';
            break;
        case '.json':
            contentType = 'application/json';
            break;
        case '.png':
            contentType = 'image/png';
            break;
        case '.jpg':
            contentType = 'image/jpg';
            break;
    }
    //read file
    fs.readFile(filePath, (err, content)=>{
        if(err){
            if(err.code == 'ENOENT'){
                //Page not found
                fs.readFile(path.join(__dirname, 'public', '404.html'), (err, content)=>{
                    res.writeHead(200, {'Content-Type' : 'text/html'});
                    res.end(content);
                })
            }else{
                //some server err
                res.writeHead(500);
                res.end(`Server err ${err.code}`);
            }
        }else{
            //sucess
            res.writeHead(200, {'Content-Type' : contentType});
            res.end(content);
        }
    });
});


const PORT = process.env.PORT || 5000;
server.listen(PORT, ()=> console.log(`Server running at port ${PORT}`));