const fetch = require('node-fetch');
const API_FILE = require('./API_KEY.json');

const API_KEY = API_FILE['API_KEY'];

const playerName = 'Hyplex';
const playerUUID = 'bec9029b-efb3-4c85-925d-f2e97640cf92';
fetch(`https://api.hypixel.net/player?key=${API_KEY}&name=${playerName}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch(console.log.bind('Network Error'));
fetch(`https://api.hypixel.net/player?key=${API_KEY}&uuid=${playerUUID}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch(console.log.bind('Network Error'));
