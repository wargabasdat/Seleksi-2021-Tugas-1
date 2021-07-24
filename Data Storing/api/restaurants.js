const router = require('express').Router();
let Restaurant = require('./restaurant.model.js');

router.route('/').get((req, res) => {
	Restaurant.find()
		.then((restaurants) => res.json(restaurants))
		.catch((err) => res.status(400).json('Error: ' + err));
});

module.exports = router;
