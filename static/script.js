function startBot() {
  const form = document.getElementById("botForm");
  const data = new FormData(form);

  fetch("/save", {
    method: "POST",
    body: data
  })
  .then(() => {
    return fetch("/start", { method: "POST" });
  })
  .then(res => res.text())
  .then(text => {
    document.getElementById("debug").innerText = text;
  });
}

function stopBot() {
  fetch("/stop", { method: "POST" })
    .then(res => res.text())
    .then(text => {
      document.getElementById("debug").innerText = text;
    });
}
