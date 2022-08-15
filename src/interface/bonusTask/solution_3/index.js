const http = require("http");
const fs = require("fs");
const ws = require("ws");

const index = fs.readFileSync("index.html");

console.warn("DO NOT USE THIS SERVER FOR PRODUCTION!!!");

http
  .createServer((req, res) => {
    const file = req.url;
    if (file === "/" || file === "/index.html") {
      res.writeHead(200, { "Content-Type": "text/html" });
      res.end(index);
      return;
    } else if (file === "/final_values.html") {
      res.writeHead(200, { "Content-Type": "text/html" });
      fs.readFile("./final_values.html", { encoding: "utf-8" }, (err, data) => {
        res.end(data);
      });
      return;
    }
    res.writeHead(404, { "Content-Type": "text/html" });
    res.end("<html><head></head><body><h1>Not Found</h1></body></html>");
  })
  .listen(8080, () => {
    console.log("Listening on port 8080");
  });

const wss = new ws.WebSocketServer({ port: 8081 }, () => {
  console.log('WebSocket on port 8081');
});

fs.watchFile("final_values.html", { interval: 200 }, (cur, prev) => {
  wss.clients.forEach((c) => {
    if (c.readyState === ws.WebSocket.OPEN) {
      c.send("changed");
    }
  });
});
