function send() {
    let msg = document.getElementById("msg").value;

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg})
    })
    .then(res => res.json())
    .then(data => {
        let box = document.getElementById("messages");

        box.innerHTML += `<div class="user">You: ${msg}</div>`;
        box.innerHTML += `<div class="bot">Bot: ${data.response}</div>`;

        document.getElementById("msg").value = "";
        box.scrollTop = box.scrollHeight;
    });
}