var app = require('http').createServer(),
    io = require('socket.io').listen(app),
    logger  = io.log,
    redis = require('redis').createClient();

var port = process.argv[2];
app.listen(port);

console.log(port)
io.configure( function() {
    io.set('close timeout', 60*60*24); // 24h time out
});

redis.psubscribe("channel_comments_*"); //subscribe by pattern

io.sockets.on("connection", function(socket) {
    redis.on("pmessage", function(pattern, channel, message) {
        socket.emit(channel, message);
    });
});
