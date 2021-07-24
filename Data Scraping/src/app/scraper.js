const cheerio = require('cheerio');
const bluebird = require("bluebird");
const puppeteer = require('puppeteer');
const moment = require('moment');

const BASE_URL = 'https://gleague.nba.com';


const extractPlayerLinks = (selector, allPlayers) => {
  let links = [];

  allPlayers.each((i, e) => {
    const playersPerColumn = selector(e).find('.players-list__content > ul');
    playersPerColumn.each((i, e) => {
      const playerLinks = selector(e).find('li[class="content__player-summary"]');
      playerLinks.each((i, e) => {
        const link = selector(e).find('a').attr('href');

        if (typeof(link) !== "undefined") links.push(link);
      });
    });
  });
  
  return links;
}

const extractPlayerData = async (page, url) => {
  await page.goto(url, {
    waitUntil: 'networkidle0',
    timeout: 0,
  });
  const content = await page.content();

  const selector = cheerio.load(content);
  const player = selector('body').find('section[class="player"]');

  const upperSection = player.find('header[class="player-header is-full-width"] > div[class="player-header__main cf"]');
  const main = upperSection.find('div[class="player-header-main"]');
  const playerInfo = upperSection.find('div[class="player-header__stats"] > div[class="player-stats"]');
  const id = main.find('#playerId').attr('value');
  const name = main.find('h1').text().trim().replace(/\s+/g, ' ');
  const position = upperSection.find('div[class="player-header-section player-header-section--team"] > p > #playerPosition').text().trim();

  if (!id || !name || !position) {
    return {};
  }

  // Player Info
  let height;
  let weight;
  let dateOfBirth;
  let college;
  let nationality;

  playerInfo.find('#playerPagePlayerInfo > ul[class="bio-about-stats cf"] > li').each((i, e) => {
    if (i === 0) {
      height = parseInt(selector(e).find('div[class="bio-stat"] > div[class="bio-stat__extra"]').text().replace(/(?=\s?cm)/g, '').trim());
    } else if (i === 1) {
      weight = parseInt(selector(e).find('div[class="bio-stat"] > div[class="bio-stat__extra"]').text().replace(/(?=\s?kg)/g, '').trim());
    } else if (i === 2) {
      dateOfBirth = selector(e).find('div[class="bio-stat"] > div[class="bio-stat__stat bio-stat__stat--sm"]').text().trim();
      dateOfBirth = moment.parseZone(dateOfBirth, "MMMM Do, YYYY");
    } else if (i === 3) {
      const cN = selector(e).find('div[class="bio-stat"] > div[class="bio-stat__stat bio-stat__stat--sm"]').text().trim().split('/');
      college = cN[0];
      nationality = cN[1];
    }
  });

  if (!height || !weight || !dateOfBirth || !college || !nationality) {
    return {};
  }

  // Career Stats
  let arrayTemp = [];
  playerInfo.find('#playerPageCareerStats > ul[class="stats-list cf"] > li').each((i, e) => {
    const num = parseFloat(selector(e).find('span[class="stats-list__num"]').text().trim());
    arrayTemp.push(num);
  });

  let ppg = arrayTemp[0];
  let rpg = arrayTemp[1];
  let apg = arrayTemp[2];
  let bpg = arrayTemp[3];
  let spg = arrayTemp[4];
  let mpg = arrayTemp[5];

  if (!ppg || !rpg || !apg || !bpg || !spg || !mpg) {
    return {};
  }

  return {
    id,
    name,
    position,
    height,
    weight,
    dateOfBirth,
    college,
    nationality,
    ppg,
    rpg,
    apg,
    bpg,
    spg,
    mpg
  };
  
}

const withBrowser = async (fn) => {
	const browser = await puppeteer.launch();
	try {
		return await fn(browser);
	} finally {
		await browser.close();
	}
}

const withPage = (browser) => async (fn) => {
	const page = await browser.newPage();
	try {
		return await fn(page);
	} finally {
		await page.close();
	}
}


const scrapPlayers = async () => {
  const url = `${BASE_URL}/all-players`;
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url, {
    waitUntil: 'networkidle0',
  });
  const content = await page.content();

  const selector = cheerio.load(content);

  const allPlayers = selector('body').find('#allPlayersList > section');
  let links = extractPlayerLinks(selector, allPlayers);

  let result = await withBrowser(async (browser) => {
    return bluebird.map(links, async (url) => {
      return withPage(browser)(async(page) => {
        return extractPlayerData(page, url);
      });
    }, { concurrency: 12 });
  });

  return result.filter(value => Object.keys(value).length !== 0);
}


module.exports = scrapPlayers;
