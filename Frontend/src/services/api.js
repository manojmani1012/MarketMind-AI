import axios from "axios";

export const runResearch = async (query) => {

  const response = await axios.post(
    "http://localhost:8000/research",
    {
      query,
    }
  );

  return response.data;
};