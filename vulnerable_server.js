// AUTH: SISU | Script : CRYPTOGRAPHYTUBE
const http = require('http');
const { randomBytes } = require('crypto');
const EC = require('elliptic').ec;

const ec = new EC('secp256k1');
const privateKey = randomBytes(32);
const key = ec.keyFromPrivate(privateKey);

http.createServer((req, res) => {
    if (req.url === '/ecdh') {
        const pubHex = req.headers['x-pubkey'];
        try {
            const clientKey = ec.keyFromPublic(pubHex, 'hex');
            const shared = key.derive(clientKey.getPublic()).toString(16);
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end(shared);
        } catch (e) {
            res.writeHead(400);
            res.end('error');
        }
    } else {
        res.writeHead(404);
        res.end('not found');
    }
}).listen(8080, () => {
    console.log('CRYPTOGRAPHYTUBE vulnerable ECDH server running on port 8080 - AUTH: SISU');
});
