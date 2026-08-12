export function askAI(question) {
    return fetch("http://127.0.0.1:8000/api/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: question
        })
    })
    .then(res => res.json());
}