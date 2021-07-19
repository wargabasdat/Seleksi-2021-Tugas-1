const mongoose = require('mongoose');

const playerSchema = new mongoose.Schema({
    name : {
        type: String,
        required: true
    },
    team : String,
    number : Number,
    position : {
        type: String,
        required: true
    },
    height : {
        type: Object,
        required: true
    },
    weight : {
        type: Number,
        required: true
    },
    school : String,
    country : String
},
  {versionKey : false}
);

const playerModel = mongoose.model('Player', playerSchema, 'NBAPlayers')

module.exports = playerModel;