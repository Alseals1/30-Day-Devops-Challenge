import { useState } from "react";

const WeatherDashboard = () => {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [error, setError] = useState("");

  const fetchWeather = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/weather?city=${city}`
      );
      if (!response.ok) {
        throw new Error("Failed to fetch weather data");
      }
      const data = await response.json();
      setWeather(data);
      setError("");
    } catch (err) {
      setWeather(null);
      setError(`Here is your err: ${err.message}`);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-black">
      <div className="pb-6 text-4xl text-cyan-600">Weather Dashboard</div>
      <div className="text-center p-4 border rounded shadow-lg bg-slate-200">
        <input
          type="text"
          placeholder="Enter city"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          className="mt-2 p-2 border rounded"
        />
        <button
          onClick={fetchWeather}
          className="mt-2 p-2 bg-blue-500 text-white rounded ml-5 hover:bg-blue-700"
        >
          Get Weather
        </button>
        {error && <p className="text-red-500 mt-2">{error}</p>}
        {weather && (
          <div className="mt-4">
            <h2 className="text-xl font-semibold">{weather.name}</h2>
            <p>Temperature: {weather.main.temp}°F</p>
            <p>Feels Like: {weather.main.feels_like}°F</p>
            <p>Condition: {weather.weather[0].description}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default WeatherDashboard;
