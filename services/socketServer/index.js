var express = require("express");
var app = express();
var http = require("http");
var http_server = http.createServer(app).listen(8484);
var http_io = require("socket.io")(http_server, {
    cors: {
        origin: "http://localhost:3000",
        methods: ["GET", "POST"]
      }
});



http_io.on("connection", async function(httpsocket){
    //const channel = await client.channels.fetch('976106571924897843');
    httpsocket.on("message", function (fromPython) {
      console.log("carListUpdate");
      carList = JSON.parse(fromPython);
      console.log(carList);
      console.log("Car list length: " + carList.length)
      httpsocket.broadcast.emit("countUpdate", carList.length);
      httpsocket.broadcast.emit("carListUpdate", fromPython);
    })
    console.log("new user");    
  })