import axios from "axios";

const API_URL = "http://localhost:8001";

export const analyzeMarket = async (query) => {
  const response = await axios.post(
    `${API_URL}/research`,
    {
      query,
    }
  );

  return response.data;
};