import { useState } from "react";
import { uploadDocs } from "../api";

export default function UploadDocs() {
  const [strategy, setStrategy] = useState(null);
  const [action, setAction] = useState(null);

  const upload = async () => {
    await uploadDocs(strategy, action);
    alert("Documents indexed!");
  };

  return (
    <div>
      <h3>Upload Strategy & Action Plans</h3>
      <input type="file" onChange={e => setStrategy(e.target.files[0])} />
      <input type="file" onChange={e => setAction(e.target.files[0])} />
      <button onClick={upload}>Upload</button>
    </div>
  );
}
