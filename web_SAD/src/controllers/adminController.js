const Product = require("../models/productSchema");
const { mutipleMongooseToObj } = require('../utils/mongoose');
const { mongooseToObj } = require('../utils/mongoose');

class AdminController{
    // [GET] /admin/create
    create(req, res, next){
        res.render('CRUDproduct/create');
    }
    // [POST] /admin/store
    store(req, res, next){
        let main_detail = {};
        main_detail.title = req.body.main_detail_title;
        main_detail.description = req.body.main_detail_description;
        main_detail.feature = req.body.main_detail_feature.split(",");

        let sub_detail = {};
        sub_detail.title = req.body.sub_detail_title;
        sub_detail.description = req.body.sub_detail_description;
        sub_detail.feature = req.body.sub_detail_feature;
        const sub_detail_2 = req.body.sub_detail_2;
        const detail = {main_detail, sub_detail, sub_detail_2};
        
        const tag = req.body.tag.split(",");
        
        let product = {
            title : req.body.title,
            img: req.body.img,
            brand: req.body.brand,
            price: req.body.price,
            salePrice : req.body.salePrice,
            qty: parseInt(req.body.qty),
            tag: tag,
            detail: detail,
            type: req.body.type,
            createdAt: new Date(),
        };
        console.log(typeof(product));
        product = new Product(product);
        product.save();
        res.status(201).json(product);
    }
    // [GET] /admin/manage
    manage(req, res, next){
        Product.find({})
            .then(products => res.render('CRUDproduct/manageProduct', 
                    {products : mutipleMongooseToObj(products)}))
            .catch(next);
    }
    // [GET] /admin/update/:id
    update(req, res, next){
        Product.findOne({_id : req.params.id})
            .then(product => {
                const feature = product.detail.main_detail.feature;
                res.render('CRUDproduct/update', {product : mongooseToObj(product),feature})
            })
            .catch(next);
    }
    // [PUT] /admin/:id
    save(req, res, next){
        Product.updateOne({_id : req.params.id}, req.body)
            .then(() => res.redirect('/admin/manage'))
            .catch(next)
    }
    // [DELETE] /admin/:id
    delete(req, res, next){
        Product.deleteOne({_id : req.params.id})
            .then(() => res.redirect('back'))
            .catch(next)
    }
}

module.exports = new AdminController;