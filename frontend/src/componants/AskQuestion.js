import { useState } from "react";
import { askQuestion } from "../api";

export default function AskQuestion() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleAsk = async () => {
    const res = await askQuestion(question);
    setAnswer(res.answer);
  };

  return (
    <div>
      <h3>Ask Alignment Question</h3>
      <textarea
        rows="4"
        value={question}
        onChange={e => setQuestion(e.target.value)}
      />
      <br />
      <button onClick={handleAsk}>Analyze</button>
      <pre>{answer}</pre>
    </div>
  );
}
