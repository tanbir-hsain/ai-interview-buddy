import { useState } from "react";
import ReactMarkdown from "react-markdown";
import "./App.css";
import { askAI } from "./api";

function App() {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [loading, setLoading] = useState(false);

    function handleAsk() {
        if (!question.trim()) return;

        setLoading(true);
        setAnswer("");

        askAI(question)
            .then((data) => {
                setAnswer(data.answer);
            })
            .catch(() => {
                setAnswer("⚠️ AI service is unavailable or the free quota has been reached. Please try again later.");
            })
            .finally(() => {
                setLoading(false);
            });
    }

    return (
        <div className="container">
            <h1>AI Interview Buddy</h1>

            <textarea
                placeholder="Ask interview related questions..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
            />

            <button onClick={handleAsk} disabled={loading}>
                {loading ? "Loading..." : "Ask AI"}
            </button>

            <div className="answer">
                <ReactMarkdown>{answer}</ReactMarkdown>
            </div>
        </div>
    );
}

export default App;