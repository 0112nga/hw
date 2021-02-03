const { static } = require('express');
const express = require('express');
const exphbs = require('express-handlebars');
const logger = require('./middleware/logger');
const members = require('./members');
// const path = require('path');

const app = express();


//handerbars middleware
app.engine('handlebars', exphbs({defaultLayout : 'main'}));
// create hbs name main.hbs
app.set('view engine', 'handlebars');
app.use(express.json());
app.use(express.urlencoded({ extended: false}));
//Homepage route
app.get('/', (req, res) => res.render('index', {
    title: 'Member App',
    members
}));

// app.use(logger);
app.use(express.static('public'));

app.use('/api/members', require('./routes/api/members'));


app.listen(process.env.PORT || 5000, ()=> console.log('Server running'))