Read more about this project here: https://www.nicholasboyce.dev/posts/post-10/

# TicTacToe (a.k.a. Noughts and Crosses)

I made a command-line playable tic-tac-toe game - but the real meat of this program came from implementing the ability to play against the computer.
In order to do this, I had to think deeply about where and how the computer would be making its decisions. Ultimately, I programmed it by implementing first the standard minimax algorithm, in which the computer calculates the best possible next move by exploring all the possibilities from the current game state. See corresponding blog post [here](https://www.nicholasboyce.dev/posts/post-9/).

I then improved upon it by implementing the alpha-beta pruning optimization technique, which allows the computer to determine whether or not it even needs to explore certain possibilities based on the best options it has seen for both players so far. See corresponding blog post [here](https://www.nicholasboyce.dev/posts/post-10/).

This project was a really great way for me to practice depth-first search and backtracking algorithms, and was a nice peek into the kinds of algorithms one would see in the world of machine-learning.

## Implementation Results

Computer Plays First, No Optimization:
||Time Elapsed (ms)|||||
|-|-|-|-|-|-|
|Round #|Game #1|Game #2|Game #3|Game #4|Average|
|1|643.1366|641.2870|634.3617|667.2151|646.5001|
|2|19.4921|20.5665|19.9321|19.5990|19.8974|
|3|0.5115|0.9745|0.7289|0.5960|0.7027|
|4|0.0760|0.1230|0.1138|0.0773|0.0975|
|5|0.0213|0.0224|0.0173|0.0380|0.02475|

Computer Plays Second, No Optimization:
||Time Elapsed (ms)|||||
|-|-|-|-|-|-|
|Round #|Game #1|Game #2|Game #3|Game #4|Average|
| 1 | 90.4679 | 89.6885 | 90.1249 | 89.7079 | 89.9973  |
| 2 | 3.4958  | 3.5244  | 3.4979  | 3.5125  | 3.50765  |
| 3 | 0.2245  | 0.1989  | 0.1756  | 0.2617  | 0.215175 |
| 4 | 0.0748  | 0.0244  | 0.1054  | 0.1210  | 0.0814   |

Computer Plays First, Alpha-Beta Optimization:
|         | Time Elapsed (ms) |         ||||
| ------- | ----------------- | ------- |-|-|-|
| Round # | Game #1           | Game #2 | Game #3 | Game #4 | Average |
| 1       | 42.0022           | 42.8554 | 41.3975 | 42.2872 | 42.135575 |
| 2       | 2.9619            | 3.1567  | 3.9382 | 1.7098 | 2.94165 |
| 3       | 0.2737            | 0.3729  | 0.2037 | 0.3825 | 0.3082 |
| 4       | 0.0627            | 0.0685  | 0.0644 | 0.0264 | 0.0555 |
| 5       | 0.0254            | 0.0241  | 0.0194 | 0.0227 | 0.0229 |

Computer Plays Second, Alpha-Beta Optimization:
|         | Time Elapsed (ms) |||||
| ------- | ----------------- |-|-|-|-|
| Round # | Game #1           | Game #2 | Game #3 | Game #4 | Average |
| 1       | 8.2627            | 8.0057 | 7.9894 | 8.5866 | 8.2111 |
| 2       | 1.2142            | 1.0354 | 1.6300 | 1.2272 | 1.2767 |
| 3       | 0.1367            | 0.1512 | 0.1906 | 0.1863 | 0.1662 |
| 4       | 0.0423            | 0.0422 | 0.0190 | 0.0456 | 0.037275 |

## Tech Stack
Python
