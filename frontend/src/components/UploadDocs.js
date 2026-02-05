import { uploadDocs } from "../api";

export default function UploadDocs() {
  let strategy, action;

  const upload = async () => {
    if (!strategy || !action) {
      alert("Upload both documents");
      return;
    }
    await uploadDocs(strategy, action);
    alert("Documents indexed successfully");
  };

  return (
    <>
      <label>Strategy Document</label>
      <input type="file" onChange={e => strategy = e.target.files[0]} />

      <label style={{ marginTop: "50px" }}>Action Plan</label>
      <input type="file" onChange={e => action = e.target.files[0]} />

      <button style={{ marginTop: "50px", width: "100%" }} onClick={upload}>
        Upload & Index
      </button>
    </>
  );
}
