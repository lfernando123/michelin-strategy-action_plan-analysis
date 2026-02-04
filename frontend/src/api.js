const API_URL = "http://localhost:8000";

export async function uploadDocs(strategy, action) {
  const formData = new FormData();
  formData.append("strategy", strategy);
  formData.append("action", action);

  const res = await fetch(`${API_URL}/upload`, {
    method: "POST",
    body: formData,
  });

  return res.json();
}

export async function askQuestion(question) {
  const res = await fetch(`${API_URL}/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });

  return res.json();
}
