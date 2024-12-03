class MispConfig {
    constructor(url, token) {
        this.MISP_URL = url;
        this.MISP_TOKEN = token;
        this.MISP_EVENTS_URL = this.MISP_URL + '/events';
        this.MISP_ATTR_URL = this.MISP_URL + '/attributes';
    }
}

const _MispConfig = new MispConfig('http://localhost', 'VpsWeu2TsfqLQ5BTfk2BgRIw6Ca6rj3vzJlIj4TX');

export { _MispConfig as MispConfig };