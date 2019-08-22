var express = require("express");
var bodyParser = require("body-parser");
var path = require("path");

//init libraries
var app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "/client/build")));

//Init routers
var index = require("./routes/index");
var itemRoute = require("./routes/item");

//use routes
app.use("/", index);
app.use("/item", itemRoute);

app.listen(3000, () => {
  console.log("Listening to port: 3000");
});
