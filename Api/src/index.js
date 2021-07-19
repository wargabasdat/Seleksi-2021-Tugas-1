const apiRouter = require('./players/router');

const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
require('dotenv').config();

const app = express();

app.use(bodyParser.json());

mongoose.connect(
    process.env.MONGO_URI,
    {useNewUrlParser: true, useUnifiedTopology: true, useFindAndModify: false},
    () => console.log('connected to mongodb')
);


port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log('app listening on port' + port)
});

app.get('/', (req,res) => {
    res.send("NBA Players API");
});


app.use('/players', apiRouter);