const express = require('express');
const router = express.Router();

const productController = require('../controllers/productController');

router.get('/:type', productController.showType);

module.exports = router;