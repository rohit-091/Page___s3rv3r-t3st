function startServer() {
    fetch('/start', { method: 'POST' })
        .then(res => res.text())
        .then(data => document.getElementById('status').innerText = data);
}
function stopServer() {
    fetch('/stop', { method: 'POST' })
        .then(res => res.text())
        .then(data => document.getElementById('status').innerText = data);
}
