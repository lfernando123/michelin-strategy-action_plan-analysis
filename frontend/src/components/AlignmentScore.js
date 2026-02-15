export default function AlignmentScore({ score }) {
  const getColor = () => {
    if (score >= 75) return "#2ecc71";
    if (score >= 50) return "#f39c12";
    return "#e74c3c";
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <h4>Alignment Score: {score}%</h4>
      <div
        style={{
          height: "20px",
          background: "#ddd",
          borderRadius: "10px",
          overflow: "hidden"
        }}
      >
        <div
          style={{
            width: `${score}%`,
            height: "100%",
            background: getColor(),
            transition: "width 0.5s ease-in-out"
          }}
        />
      </div>
    </div>
  );
}
