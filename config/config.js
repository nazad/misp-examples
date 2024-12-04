class MispConfig {
    constructor(url, token) {
        this.MISP_SERVER = url;
        this.MISP_PORT = 443;
        this.MISP_TOKEN = token;
        this.MISP_EVENTS_URL = '/events';
        this.MISP_ATTR_URL = '/attributes';
    }
}

module.exports = new MispConfig('localhost', 'VpsWeu2TsfqLQ5BTfk2BgRIw6Ca6rj3vzJlIj4TX');