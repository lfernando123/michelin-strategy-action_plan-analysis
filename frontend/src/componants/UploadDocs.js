import { useState } from "react";
import { uploadDocs } from "../api";

export default function UploadDocs() {
  const [strategy, setStrategy] = useState(null);
  const [action, setAction] = useState(null);

  const handleUpload = async () => {
    if (!strategy || !action) {
      alert("Select both files");
      return;
    }
    await uploadDocs(strategy, action);
    alert("Documents uploaded and indexed");
  };

  return (
    <div>
      <h3>Upload Documents</h3>
      <input type="file" onChange={e => setStrategy(e.target.files[0])} />
      <input type="file" onChange={e => setAction(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}
