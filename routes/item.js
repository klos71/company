var express = require("express");
var router = express.Router();
var fs = require("fs");

router.get("/get/:itemid", (req, res) => {
  var item = fs.readFileSync("./items/" + req.params.itemid + ".json");
  res.json(JSON.parse(item));
});
router.post("/set/", (req, res) => {
  var answer = req.body;
  fs.writeFileSync(
    "./items/" + req.body.item.articleNumber + ".json",
    JSON.stringify(req.body)
  );

  res.json(answer);
});

router.get("/list", (req, res) => {
  var list = fs.readdirSync("./items/");
  var returnList = [];
  list.forEach((el) => {
    returnList.push(el.split(".")[0]);
  });
  res.json(returnList);
});

module.exports = router;
