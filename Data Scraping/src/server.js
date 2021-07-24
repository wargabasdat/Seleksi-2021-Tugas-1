
const path = require('path');
const logger = require('morgan');
const express = require('express');
const scrapPlayers  = require('./app/scraper');
const { saveToDB,
  findAllPlayers,
  findPlayerById,
  searchPlayersByName,
  findPlayerStatsById
} = require('./app/storing');
const Response = require('./utils/Response');
const fs = require('fs');

const app = express();
const port = process.env.PORT || 5000;

app.set('port', port);
app.use(logger('dev'));
app.use('/', express.static(path.resolve(__dirname, 'public')));

app.get('/', async (req, res, next) => {
  res.send('<h1>Hello, this is an NBA G League Players scraper!</h1>')
});

app.get('/scrap-players', async (req, res, next) => {
  const result = await scrapPlayers();
  const jsonString = JSON.stringify(result, null, 2);
  fs.writeFileSync(path.join(__dirname, "files", "data.json"), jsonString);
  res.send(result);
});

app.get('/save-players/:filename', async (req, res, next) => {
  try {
    let rawdata = fs.readFileSync(path.join(__dirname, "files", req.params.filename));
    let arr = JSON.parse(rawdata);
    const result = await saveToDB(arr);
    res.status(200).send(new Response(true, result, '').createResponse());
  } catch (err) {
    console.error(err);
    res.status(400).send(new Response(false, error, 'Internal Error').createResponse());
  }
})

app.get('/players/all', async (req, res, next) => {
  try {
    const result = await findAllPlayers();
    if (!result) {
      res.status(200).send(new Response(true, {}, '').createResponse());
    } else {
      res.status(200).send(new Response(true, result, '').createResponse());
    }
  } catch (err) {
    console.error(err);
    res.status(400).send(new Response(false, error, 'Internal Error').createResponse());
  }
});

app.get('/players/:id', async (req, res, next) => {
  try {
    const result = await findPlayerById(req.params.id);
    if (!result) {
      res.status(200).send(new Response(true, {}, '').createResponse());
    } else {
      res.status(200).send(new Response(true, result, '').createResponse());
    }
  } catch (err) {
    console.error(err);
    res.status(400).send(new Response(false, error, 'Internal Error').createResponse());
  }
});

app.get('/players/search/:query', async (req, res, next) => {
  try {
    const result = await searchPlayersByName(req.params.query);
    if (!result) {
      res.status(200).send(new Response(true, {}, '').createResponse());
    } else {
      res.status(200).send(new Response(true, result, '').createResponse());
    }
  } catch (err) {
    console.error(err);
    res.status(400).send(new Response(false, error, 'Internal Error').createResponse());
  }
});

app.get('/players/stats/:id', async (req, res, next) => {
  try {
    const result = await findPlayerStatsById(req.params.id);
    if (!result) {
      res.status(200).send(new Response(true, {}, '').createResponse());
    } else {
      res.status(200).send(new Response(true, result, '').createResponse());
    }
  } catch (err) {
    console.error(err);
    res.status(400).send(new Response(false, error, 'Internal Error').createResponse());
  }
});

app.listen(port, () => console.log(`App started on port ${port}.`));