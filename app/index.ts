import { Appsetting } from "./../appsettings";
import * as express from "express";
const spawn = require("child_process").spawn;

const app = express();
const port = 3000;

app.get("/api/nespseindex/", (req, res) => {
  let pythonprocess = spawn("python", [Appsetting.path]);

  let responsedata = "";
  pythonprocess.stdout.on("data", data => {
    responsedata += data.toString();
    responsedata = responsedata.trim();
    res.send({ NEPSE: responsedata });
  });

  pythonprocess.stderr.on("data", data => {
    responsedata += data.toString();
  });
});

app.listen(port, () => {
  console.log(` app is listening in port ${port}`);
});
