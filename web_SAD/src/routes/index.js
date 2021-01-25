const express = require('express');
const products = require('./products');
const admin = require('./admin');
const site = require('./site');
const type = require('./type');
const brand = require('./brand');

function route(app){

    app.use('/admin', admin);
    app.use('/products',products);
    app.use('/type', type);
    app.use('/brand', brand)
    app.use('/', site);

}

module.exports = route;