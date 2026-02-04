import { useState } from "react";
import { askQuestion } from "../api";

export default function AskQuestion() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const ask = async () => {
    const res = await askQuestion(question);
    setAnswer(res.answer);
  };

  return (
    <div>
      <h3>Ask Strategy Alignment Question</h3>
      <textarea onChange={e => setQuestion(e.target.value)} />
      <button onClick={ask}>Analyze</button>
      <pre>{answer}</pre>
    </div>
  );
}
