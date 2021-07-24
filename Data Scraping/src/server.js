
const path = require('path');
const logger = require('morgan');
const express = require('express');
const Pool = require('pg');
const scrapPlayers  = require('./app/scraper');

const app = express();
const port = process.env.PORT || 5000;
const pool = new Pool({
  connectionString: "dbname=d4419mdb65kpsl host=ec2-34-233-114-40.compute-1.amazonaws.com port=5432 user=gxakjmbgtplcdj password=b4e78488df9ff1a584c5e0c5cfd9e2555dcf09a2ff7b62ff0ff68df9a3e7a53e sslmode=require",
  ssl: {
    rejectUnauthorized: false,
  }
})

app.set('port', port);
app.use(logger('dev'));
app.use('/', express.static(path.resolve(__dirname, 'public')));

app.get('/', async (req, res, next) => {
  res.send('<h1>Hello, this is an NBA G League scraper!</h1>')
});

app.get('/all-players', async (req, res, next) => {
  const result = await scrapPlayers();
  res.send(result);
});

app.listen(port, () => console.log(`App started on port ${port}.`));