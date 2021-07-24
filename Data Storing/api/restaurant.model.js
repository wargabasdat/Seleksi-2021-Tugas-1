const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const restaurantSchema = new Schema({
	id: {
		type: String,
	},
	nama: {
		type: String,
	},
	alamat: {
		type: String,
	},
	daerah: {
		type: String,
	},
	'tipe kuliner': {
		type: Array,
	},
	'kisaran harga': {
		type: String,
	},
	rating: {
		type: Number,
	},
	pembayaran: {
		type: Array,
	},
	cabang: {
		type: Boolean,
	},
	fasilitas: {
		type: Array,
	},
});

const Restaurant = mongoose.model('Restaurant', restaurantSchema);

module.exports = Restaurant;
