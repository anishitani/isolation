# Isolation
Isolation game as described in Udacity Artificial Inteligence course.

# Rules
1. Two Players game
1. Players alternate their turns
1. Players can place their move anywhere in the board respecting the following
 1. Moves should respect the board length
 1. Moves aren't allowed to cross trails created by annny of the Players
 1. Moves can take as many cells as wanted as long the same direction is kept
 and the above rules are respected
1. The first Player without legal moves loses

# API
1. Initialize game
 1. Request `POST /games`
 1. Response
 ```json
  {
      "id": "893d672f-e0d3-4de8-b032-814865d770dc",
      "timestamp": "2018-04-16T18:12:48+00:00"
  }
 ```

1. Make a move
 1. Request `POST  /games/893d672f-e0d3-4de8-b032-814865d770dc/moves`
 ```json
 {
   "player_one": true,
   "x": 1,
   "y": 1
 }
 ```
 1. Response
 ```json
 {
   "success": true,
   "message": "Move executed!"
 }
 ```
