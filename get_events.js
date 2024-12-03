http = require('https')
mispConfig = require('./config/config.js');

const options = {
    host: mispConfig.MISP_URL,
    path: mispConfig.MISP_EVENTS_URL,
    rejectUnauthorized: false,
    method: 'GET',
    auth: mispConfig.MISP_TOKEN
};

http.request(options, function (res) {
    console.log('STATUS: ' + res.statusCode);
    console.log('HEADERS: ' + JSON.stringify(res.headers));
    res.setEncoding('utf8');
    res.on('data', function (chunk) {
        console.log('BODY: ' + chunk);
    });
}).end();
