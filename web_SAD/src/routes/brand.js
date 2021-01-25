const express = require('express');
const router = express.Router();

const productController = require('../controllers/productController');

router.get('/:brand', productController.showBrand);

module.exports = router;