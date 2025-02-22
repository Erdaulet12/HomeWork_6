import { useState, useEffect } from "react";

function Favourites() {
  const [favourites, setFavourites] = useState([]);

  useEffect(() => {
    const savedFavourites =
      JSON.parse(localStorage.getItem("favourites")) || [];
    setFavourites(savedFavourites);
  }, []);

  const removeFromFavourites = (id) => {
    const updatedFavourites = favourites.filter((movie) => movie.id !== id);
    setFavourites(updatedFavourites);
    localStorage.setItem("favourites", JSON.stringify(updatedFavourites));
  };

  const clearFavourites = () => {
    localStorage.removeItem("favourites");
    setFavourites([]);
  };

  return (
    <div className="movies-container">
      <h1>Избранные фильмы</h1>
      {favourites.length > 0 ? (
        <>
          <div className="movies-grid">
            {favourites.map((movie) => (
              <div key={movie.id} className="movie-card">
                <img src={movie.poster} alt={movie.title} />
                <h3>
                  {movie.title} ({movie.year})
                </h3>
                <button
                  className="delete-button"
                  onClick={() => removeFromFavourites(movie.id)}
                >
                  Удалить из избранного
                </button>
              </div>
            ))}
          </div>
          <button
            className="clear-button"
            onClick={clearFavourites}
            style={{
              backgroundColor: "red",
              color: "white",
              marginTop: "20px",
            }}
          >
            Очистить все избранное
          </button>
        </>
      ) : (
        <p>У вас нет избранных фильмов</p>
      )}
    </div>
  );
}

export default Favourites;
