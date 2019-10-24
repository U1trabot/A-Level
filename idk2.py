PlayerOneScore = 0
PlayerTwoScore = 0
print("How many games?")
NoOfGamesInMatch = int(input())
for NoOfGamesPlayed in range(0,NoOfGamesInMatch):
   print("Did Player One win the game (enter Y or N)?")
   PlayerOneWinsGame = input()
   if PlayerOneWinsGame == "Y":
       PlayerOneScore += 1
   else:
      PlayerTwoScore += 1
print(PlayerOneScore)
print(PlayerTwoScore)
