const { isObject } = require('lodash');
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false,
  },
});

const saveToDB = async (data) => {
  let query1 = "INSERT INTO players(id, name, position, height, weight, dateOfBirth, college, nationality) VALUES";
  let query2 = "INSERT INTO player_stats(player_id, ppg, rpg, apg, bpg, spg, mpg) VALUES";

  for (let i = 0; i < data.length; i++) {
    const obj = data[i];
    if (i < (data.length - 1)) {
      query1 = query1.concat(`(${obj.id}, '${obj.name}', '${obj.position}', ${obj.height}, ${obj.weight}, '${obj.dateOfBirth}', '${obj.college}', '${obj.nationality}'), `);
      query2 = query2.concat(`(${obj.id}, ${obj.ppg}, ${obj.rpg}, ${obj.apg}, ${obj.bpg}, ${obj.spg}, ${obj.mpg}), `);
    } else {
      query1 = query1.concat(`(${obj.id}, '${obj.name}', '${obj.position}', ${obj.height}, ${obj.weight}, '${obj.dateOfBirth}', '${obj.college}', '${obj.nationality}')`);
      query2 = query2.concat(`(${obj.id}, ${obj.ppg}, ${obj.rpg}, ${obj.apg}, ${obj.bpg}, ${obj.spg}, ${obj.mpg})`);
    }
  }

  try {
    const client = await pool.connect();
    await client.query(query1);
    await client.query(query2);
    console.log('Data has been succesfully loaded to DB');
    
    client.release();
    return data;
  } catch (err) {
    console.error(err);
    throw new Error(err);
  }
}

const findAllPlayers = async () => {
  const query = `SELECT id, name, position, height, weight, dateOfBirth, college, nationality, ppg, rpg, apg, bpg, spg, mpg FROM players INNER JOIN player_stats ON id = player_id`;
  try {
    const client = await pool.connect();
    let arr = [];
    const results = await client.query(query);
    for (let row of results.rows) {
      arr.push(row);
    }

    client.release();
    return arr;
  } catch (err) {
    console.error(err);
    throw new Error(err);
  } 
}

const findPlayerById = async (id) => {
  const query = `SELECT id, name, position, height, weight, dateOfBirth, college, nationality, ppg, rpg, apg, bpg, spg, mpg FROM players INNER JOIN player_stats ON id = player_id WHERE id = ${id}`;
  try {
    const client = await pool.connect();
    const results = await client.query(query);
    return results.rows[0];

    client.release();
  } catch (err) {
    console.error(err);
    throw new Error(err);
  }
}

const searchPlayersByName = async (searchQuery) => {
  const query = `SELECT id, name, position, height, weight, dateOfBirth, college, nationality, ppg, rpg, apg, bpg, spg, mpg FROM players INNER JOIN player_stats ON id = player_id WHERE name LIKE '%${searchQuery}%'`;
  try {
    const client = await pool.connect();
    let arr = [];
    const results = await client.query(query);
    for (let row of results.rows) {
      arr.push(row);
    }

    client.release();
    return arr;
  } catch (err) {
    console.error(err);
    throw new Error(err);
  }
}

const findPlayerStatsById = async (id) => {
  const query = `SELECT * FROM player_stats WHERE player_id = ${id}`;
  try {
    const client = await pool.connect();
    const results = await client.query(query);
    
    return results.rows[0];

    client.release();
  } catch (err) {
    console.error(err);
    throw new Error(err);
  } 
}

module.exports = { saveToDB,
  findAllPlayers,
  findPlayerById,
  searchPlayersByName,
  findPlayerStatsById};