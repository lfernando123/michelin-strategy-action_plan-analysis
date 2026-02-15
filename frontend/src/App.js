import { useState } from "react";
import UploadDocs from "./components/UploadDocs";
import { askQuestion } from "./api";
import ReactMarkdown from "react-markdown";
import "./index.css";
import AlignmentScore from "./components/AlignmentScore";

export default function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [alignmentData, setAlignmentData] = useState(null);


  const sendMessage = async () => {
  if (!input.trim()) return;

  const userMsg = { role: "user", content: input };
  setMessages(prev => [...prev, userMsg]);

  const res = await askQuestion(input);

  setAlignmentData(res);

  const aiMsg = {
    role: "ai",
    content: `
### Summary
${res.summary}

### Gaps
${res.gaps}

### Recommendations
${res.recommendations}
`
  };

  setMessages(prev => [...prev, aiMsg]);
  setInput("");
};


  return (
    <div className="app-container">
      {/* Sidebar */}
      <div className="sidebar">
        <h2>Strategy AI Analyst</h2>
        <UploadDocs />
        <p style={{ fontSize: "12px", marginTop: "20px", color: "#aaa" }}>
          MSc Data Science Project<br />
          RAG + Ollama
        </p>
      </div>

      {/* Chat */}
      <div className="chat-container">
        <div className="chat-header">
          Strategy & Action Plan Alignment
        </div>

        <div className="chat-messages">
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`message ${msg.role === "user" ? "user" : "ai"}`}
            >
              <ReactMarkdown>{msg.content}</ReactMarkdown>
            </div>
          ))}
        </div>

        {alignmentData && (
          <AlignmentScore score={alignmentData.alignment_score} />
        )}

        <div className="chat-input">
          <textarea
            rows="2"
            placeholder="Ask about alignment, KPIs, gaps, risks..."
            value={input}
            onChange={e => setInput(e.target.value)}
          />
          <button onClick={sendMessage}>Send</button>
        </div>

      </div>
    </div>
  );
}
