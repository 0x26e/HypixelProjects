const fetch = require('node-fetch');
let API_FILE = require('./API_KEY.json');

let API_KEY = API_FILE["API_KEY"]

const playerName = "Hyplex"
const playerUUID = "bec9029b-efb3-4c85-925d-f2e97640cf92"


fetch(`https://api.hypixel.net/player?key=${API_KEY}&name=${playerName}`)
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch(error => console.log("Network Error", error))
