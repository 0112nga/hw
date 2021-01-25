const Product = require("../models/productSchema");
const { mutipleMongooseToObj } = require('../utils/mongoose');
const { mongooseToObj } = require('../utils/mongoose');

class ProductController{

    // [GET] /products/:id
    index(req, res, next){
        Product.findOne({_id : req.params.id})
            .then(product => {
                res.render('products', {product : mongooseToObj(product)})
            })
            .catch(next);
    }
    // [GET] /type/:type
    showType(req, res, next){
        Product.find({ type : req.params.type})
            .then(products => {
                res.render('typeShow', {title : req.params.type ,products : mutipleMongooseToObj(products)})
            })
            .catch(next);
    }
    // [GET] /brand/:brand
    showBrand(req, res, next){
        
        Product.find({ brand : req.params.brand})
            .then(products => {
                res.render('brandShow', {title : req.params.brand ,products : mutipleMongooseToObj(products)})
            })
            .catch(next);
    }
}

module.exports = new ProductController;