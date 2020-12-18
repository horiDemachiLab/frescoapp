const express = require('express');
const session = require("express-session");
const http = require('http');
const path = require('path');
const socketio = require('socket.io');
const spawn = require("child_process").spawn;
const fs = require('fs');
const ejs = require('ejs')
const app = express();
const fft_frame = 441;

var bodyParser = require('body-parser');
var pcm = require('pcm');
var i18n = require("i18n");

i18n.configure({
    locales: ['ja', 'en', 'pt'],
    defaultLocale: 'ja',
    autoReload: true,
    directory: __dirname + "/locales"
});

app.set('ejs',ejs.renderFile);
app.set('views', path.join(__dirname, '/public/views'));
app.use(i18n.init);
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use(session({
    secret: 'keyboard cat',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: true }
}));

app.use(function (req, res, next) {
    if (req.session.locale) {
        i18n.setLocale(req, req.session.locale);
    }
    next();
});

app.use('/', express.static(path.join(__dirname, 'public')));

app.get('/index', (req, res) => {
    res.render('index.ejs');
});
app.get('/player', (req, res) => {
    res.render('player.ejs');
});
app.get('/howtouse', (req, res) => {
    res.render('howtouse.ejs');
});
app.get('/language', (req, res) => {
    res.render('language.ejs');
});
app.post('/gameoption', (req, res) => {
    res.render('gameoption.ejs', {player1:req.body.player1, player2:req.body.player2});
});
app.post('/startgame', (req, res) => {
    res.render('startgame.ejs', {player1:req.body.player1,
                                player2:req.body.player2,
                                distance:req.body.distance});
});

app.get('/chlanguage/:locale', function(req, res, next){
    i18n.setLocale(req, req.params.locale);
    res.redirect('/index');
});
server = http.createServer(app).listen(80, function() {
    console.error('Example app listening on port 4040');
});

const io = socketio.listen(server);

io.on('connection', (socket) => {
    let sampleRate = 44100;
    var fname = new Date().getTime();
    var pythonProcess = spawn('python3',["find_hit_sync.py", String(fname)]);
    pythonProcess.stdout.setEncoding('utf-8');
    var wfs = fs.createWriteStream(String(fname), 'utf8');
    socket.on('start', (data) => {
        sampleRate = data.sampleRate;
    });

    socket.on('send_pcm', (data) => {
        for (var k in data) {
            wfs.write(String(data[k]));
            wfs.write('\n');
        }
    });

    socket.on('stop', (data, ack) => {
        console.log('stop recording');
    });

    socket.on('start_sample', () => {
        var buf = new Float32Array(4096);
        var idx = 0;
        pcm.getPcmData('public/sample/sample_fresco.wav', { stereo: false, sampleRate: 44100 },
            function(sample, channel) {
                buf[idx++] = sample;
                wfs.write(String(sample));
                wfs.write('\n');
                if (idx == buf.length) {
                    socket.emit('sample_message', buf);
                    buf = new Float32Array(4096);
                    idx = 0;
                }
            },
            function() {
                socket.emit('stop_sample');
            }
        );
    });
    pythonProcess.stdout.on('data', (data) => {
        var rm_paths = data.split('\n');

        for (let rm_path of rm_paths) {
            if (rm_path.length > 1) {
                socket.emit('get_result', rm_path);
            }
        }
    });
});
