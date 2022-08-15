const http = require("http");
const fs = require("fs");

const index = fs.readFileSync("index.html").toString();
var randomNubers = [];

function genNewRandomNumber() {
  let randomNum;
  do {
    randomNum = Math.floor(Math.random() * 10000000);
  } while (randomNubers.includes(randomNum));
  randomNubers.push(randomNum);
  return randomNum;
}

http
  .createServer((req, res) => {
    const file = req.url;
    if (file === "/" || file === "/index.html") {
      res.writeHead(200, { "Content-Type": "text/html" });
      res.end(index.replace("{}", genNewRandomNumber()));
      return;
    } else if (file.startsWith("/final_values.html")) {
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
    console.warn('DO NOT USE THIS SERVER FOR PRODUCTION!!!');
    console.log('Listening on port 8080');
  });
