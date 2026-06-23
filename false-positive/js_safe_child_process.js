const cp = require("child_process");

function safeGitStatus() {
  return cp.spawn("git", ["status"], { shell: false });
}

module.exports = { safeGitStatus };

