import { useState } from "react";

import { runResearch } from "../services/api";

export default function Home() {

  const [query,setQuery]=useState("");

  const [report,setReport]=useState("");

  const submit=async()=>{

    const result=
      await runResearch(query);

    setReport(result.report);
  };

  return (
    <div style={{padding:"30px"}}>

      <h1>
        Market Research Agent
      </h1>

      <input
        value={query}
        onChange={(e)=>setQuery(e.target.value)}
        placeholder="Enter Market"
      />

      <button onClick={submit}>
        Analyze
      </button>

      <pre>
        {report}
      </pre>

    </div>
  );
}