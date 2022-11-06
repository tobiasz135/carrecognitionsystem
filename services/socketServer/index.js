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
    console.log("new user");
    httpsocket.emit("countUpdate", 15);
    //   httpsocket.on('python-message', function(fromPython){
    //       httpsocket.broadcast.emit('message', fromPython);
    //       //console.log(fromPython);
    //       var count = Object.keys(fromPython).length;
    //       //console.log(count);
    //       for(i = 0; i < count; i++){
    //         item = fromPython[i];
    //         if(item["items_available"] != 0 && enabled){
    //           console.log(item["display_name"] + " available!");
    //           const exampleEmbed = new MessageEmbed()
    //             //.setColor('#0099ff')
    //             .setTitle(item["display_name"])
    //             //.setURL('https://thedrinkitgame.pl/')
    //             .setDescription('Szybko bo ktoś nam zaraz znowu zapierdoli')
    //             .setTimestamp()
    //             .addFields({ name: 'Dostępna ilość', value: item["items_available"].toString() })
  
    //           if(item["display_name"] === "Starbucks Łódź Piotrkowska (Na koniec dnia)")
    //             exampleEmbed.setColor("#32a852")
    //           else
    //             exampleEmbed.setColor("#96651a")
              
    //           channel.send({ embeds: [exampleEmbed] });
    //           //channel.send(item["display_name"] + " dostępny w TGTG!");
    //           //send_notification(item);
    //       }
    //     }
    //   })
  })