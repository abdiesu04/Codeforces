using GameStore.Api.Dtos;
// using GameStore.Dtos;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

List<GameDto> games = new List<GameDto>
{
    new GameDto(1, "Game 1", "Action", 59.99m, new DateOnly(2022, 3, 15)),
    new GameDto(2, "Game 2", "Adventure", 39.99m, new DateOnly(2021, 7, 10)),
    new GameDto(3, "Game 3", "RPG", 49.99m, new DateOnly(2023, 11, 27)),
    new GameDto(4, "Game 4", "Sports", 29.99m, new DateOnly(2020, 5, 3)),
    new GameDto(5, "Game 5", "Strategy", 69.99m, new DateOnly(2024, 1, 1))
    // Add more GameDto objects as needed
};
// Get games
app.MapGet("games",() => games);
// get Games by ID
app.MapGet("games/{id}",(int id) => games.Find(game => game.ID == id ));
app.MapGet("/", () => "Hello World!");
app.Run();
