namespace GameStore.Api.Dtos;

public record class GameDto(int ID  , string Name , String Genre , decimal price , DateOnly releaseDate)
{

}
