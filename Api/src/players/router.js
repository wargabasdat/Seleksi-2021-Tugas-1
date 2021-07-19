const express = require('express');
const router = express.Router();

const Player = require('./playerModel');

//Get all players data
router.get('/', async (req, res) => {
  try {
    const playersData = await Player.find();

    res.status(200).json(playersData);
  }
  
  catch(err) {
    console.log(err);
    res.status(404).json({message: err});
  }
});

//Post data
router.post('/', async(req, res) => {
  try {
    const newPlayer = new Player({
      name : req.body.name,
      team : req.body.team,
      number : req.body.number,
      position : req.body.position,
      height : req.body.height,
      weight : req.body.weight,
      school : req.body.school,
      country : req.body.country 
    });

    const savedPlayer = await newPlayer.save();
    res.status(201).json(savedPlayer);
  }
  catch(err) {
    res.status(400).json({message: err});
  }
});

//Get player by id
router.get('/:id', async (req, res) => {
  try{
    var playerId = req.params.id;
    const player = await Player.findById(playerId);

    res.json(player);
  }
  catch(err) {
    res.status(404).json({message: err});
  }
});

//Delete player by id
router.delete('/:id', async(req, res) => {
  try{
    const deletedPlayer = await Player.remove({_id : req.params.id});

    res.json(deletedPlayer);
  }
  catch(err) {
    console.log(err);
    res.status(404).json({message:err});
  }
});


//Update specific player data
router.patch('/:id', async(req, res) => {
  try {
    const updatedPlayer = await Player.findByIdAndUpdate(req.params.id, req.body);

    res.status(200).json(updatedPlayer);
  }
  catch(err){
    res.status()
  }
})


module.exports = router;