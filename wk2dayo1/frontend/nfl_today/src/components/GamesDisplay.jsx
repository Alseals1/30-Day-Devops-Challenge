import { useEffect, useState } from "react";

const NFLGames = () => {
  const [games, setGames] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Replace this URL with your actual API endpoint
    const apiURL = "/api/sports";

    const fetchGames = async () => {
      try {
        const response = await fetch(apiURL);
        const data = await response.json();

        setGames(data.games);
      } catch (error) {
        console.error("Error fetching games:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchGames();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen bg-gray-100">
        <p className="text-xl font-semibold text-gray-600">
          Loading NFL games...
        </p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center text-gray-800 mb-6">
        NFL Game Schedule
      </h1>
      {games.length === 0 ? (
        <p className="text-center text-lg text-gray-600">No games available.</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {games.map((game, index) => (
            <div
              key={index}
              className="bg-white shadow-md rounded-lg p-4 border border-gray-200"
            >
              <p className="text-gray-700">
                <span className="font-semibold">Date:</span> {game.date}
              </p>
              <p className="text-gray-700">
                <span className="font-semibold">Time:</span> {game.time}
              </p>
              <p className="text-gray-700">
                <span className="font-semibold">Venue:</span> {game.venue}
              </p>
              <p className="text-gray-700">
                <span className="font-semibold">Home Team:</span>{" "}
                {game.home_team}
              </p>
              <p className="text-gray-700">
                <span className="font-semibold">Away Team:</span>{" "}
                {game.away_team}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default NFLGames;
