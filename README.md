# Human-v-s-A.I-Real-World-Chess
Real world chess played between human and A.I (Nov 2015 - Feb 2016)

As the name suggest this project is a real life chess game played between human and AI
- Detected corners of all the squares of a chess board and used it to find centroid of each square of chess board
- Image subtraction is used to recognise which piece was moved.
- Checked if the piece moved overlapped with the previously found centroids of each squares.
- If yes then, generated the move played by the player in the format of '<source co-ordinates><destination co-ordinates>'
- Passed this to the AI chess library which uses Alpha - beta pruning (Code not in the Project file)
- AI generated the move to be played in response to the humans move and returned it in the format mentioned above.
- Move to be played by AI is then sent to Arduino Uno.
- Arduino Uno controls the 2 Stepper motor and a Electromagnet.
- The 2 stepper motors forms a X-Y gantry system with an Electromagnet placed on the top.
- The above mechanism is placed under the chess board.
- Arduino processes the move to played by the AI.
- XY gantry system is used to go to source co-ordinate of the piece to be moved, once reached to the source co-ordinate the elctromagnet is turned ON which attracts the magnetic piece placed on the chess board
- XY gantry sytem then navigates to the destination co-ordinate.
- Once at the destination position the electromagnet is turned OFF.
