client = require('https')

mispConfig = require('./config/config.js');

const options = {
    host: mispConfig.MISP_SERVER,
    port: mispConfig.MISP_PORT,
    path: mispConfig.MISP_EVENTS_URL,
    headers: {
        'content-type': 'application/json',
        accept: 'application/json',
        authorization: mispConfig.MISP_TOKEN
    },
    rejectUnauthorized: false,
    method: 'GET'
};

client.request(options, function (res) {
    console.log('STATUS: ' + res.statusCode);
    console.log('HEADERS: ' + JSON.stringify(res.headers));

    res.setEncoding('utf8');

    res.on('data', function (body) {
        console.log('BODY: ' + body);
    });
}).end();
