import { useState } from "react";
import { analyzeMarket } from "../services/api";

export default function Dashboard() {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [report, setReport] = useState("");

  const runResearch = async () => {
    if (!query.trim()) {
      alert("Please enter a market research topic");
      return;
    }

    try {
      setLoading(true);

      const result = await analyzeMarket(query);

      setReport(
        result.report ||
          JSON.stringify(result, null, 2)
      );
    } catch (err) {
      console.error(err);

      alert(
        "Backend Error. Check FastAPI logs."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard">

      <div className="hero-card">

        <h1>
          MarketMind AI
        </h1>

        <p>
          Autonomous Market Research Platform
        </p>

        <textarea
          value={query}
          onChange={(e) =>
            setQuery(e.target.value)
          }
          placeholder="Analyze AI Coding Assistants Market 2026"
        />

        <button
          onClick={runResearch}
          disabled={loading}
        >
          {loading
            ? "Running Agents..."
            : "Analyze Market"}
        </button>

      </div>

      <div className="agents-card">

        <h2>
          Agent Workflow
        </h2>

        <div className="agent">
          ✓ Planner Agent
        </div>

        <div className="agent">
          ✓ Research Agent
        </div>

        <div className="agent">
          ✓ Competitor Agent
        </div>

        <div className="agent">
          ✓ SWOT Agent
        </div>

        <div className="agent">
          ✓ Executive Report Agent
        </div>

      </div>

      <div className="report-card">

        <h2>
          Executive Report
        </h2>

        <pre>
          {report}
        </pre>

      </div>

    </div>
  );
}