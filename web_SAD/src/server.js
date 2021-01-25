const express = require('express');
const handlebars = require('express-handlebars');
const mongoose = require('mongoose');
const path = require('path');
const bodyParser = require('body-parser');
const override = require('method-override');
const route = require('./routes/index');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(bodyParser.json());
app.use(express.urlencoded({ extended: false}));
app.use(express.json());
app.use(override('_method'));

app.use(express.static(path.join(__dirname, 'public')));

//route init
route(app);


//template engine
app.engine('handlebars', handlebars({
    helpers:{
        sum: (a,b) => a+b,
    }
}));
app.set('view engine', 'handlebars');
app.set('views', path.join(__dirname, 'views'));


async function startServer(){
    try {
        await mongoose.connect('mongodb://localhost:27017/web_SAD', 
        { useUnifiedTopology: true , useNewUrlParser: true }, ()=> console.log('connect to Mongodb'));
        await app.listen(PORT);
        console.log(`Server running at ${PORT}`);
    }catch(err){
        console.log('Connect failure!!!');
    }
    
}
startServer();