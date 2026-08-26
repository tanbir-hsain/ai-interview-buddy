
export function askAI(question) {
    return fetch("http://127.0.0.1:5000/api/chat/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question })
    }).then(res => res.json());
}


