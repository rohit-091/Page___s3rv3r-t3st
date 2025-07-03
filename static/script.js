function saveInputs() {
  const form = document.getElementById('botForm');
  const data = new FormData(form);
  fetch('/save', {
    method: 'POST',
    body: data
  }).then(res => res.text())
    .then(msg => document.getElementById('status').innerText = msg);
}

function startBot() {
  fetch('/start', { method: 'POST' })
    .then(res => res.text())
    .then(msg => document.getElementById('status').innerText = msg);
}

function stopBot() {
  fetch('/stop', { method: 'POST' })
    .then(res => res.text())
    .then(msg => document.getElementById('status').innerText = msg);
}
