#! /usr/bin/python3
import random
import time
import os
FUCKMAN = (
"""
This is evil black man.
If you do not answer the question,
he will start to use you.

||||||  ||  ||   ||||||   ||  //   ||||||  ||||))
||      ||  ||   ||       || //    ||      ||  ))
||||||  ||  ||   ||       ||//     |||||   ||||))
||      ((  ))   ||       ||\\\\     ||      ||\\\\
||       (())    ||||||   || \\\\    ||||||  || \\\\

     |   |
     |   |
     |   |
     \   /
      \ /                                                                       |
     ___ _           ////                                                       |
    |   0|_         |*^*|            \\\\  //   ||||||   ||  ||                   |
    |____|          8876              \\\\//    ||  ||   ||  ||                   |
    _|  |__         8877               ||     ||  ||   ||  ||                   |
    |    | +        8877 0 66          ||     ||  ||   ((  ))                   |
    |    |+ +       8877               ||     ||||||    (())                    |
    |    | + +      8877 0                                                      |
    |____|  + +    88877  66                                                    |
    |   |          88777                                                        |
    |   |          88666_                                                       |
    |   |           5555 \                                                      |
    |   |           444   \                                                     |
    |   |           333                                                         |
    |___|_          222                                                         |
    |_____|         1111                                                        |
""",
"""
                                                                                |
     ____                                                                       |
    |   0|_ #                                                                   |
    |____|                                                                      |
    _|  |__                            ///////////                              |
    |    | +                          // ||  ||   //                            |
    |    |+ +                        //  ||  ||    //                           |
    |    | + +                      //   ||||||    //                           |
    |____|  + +           __       //    ||  ||    //                           |
    |   |____886666777777(__)            ||  ||   //                            |
    |   |____886666777777         ////////////////                              |
    |   |   " 5555 \  0 0                                                       |
    |   |       444 \  66 66                                                    |
    |   |      333                                                              |
    |___|_     222                                                              |
    |_____|    1111                                                             |
""",
"""
              ###                                                               |
     ____                                                                       |
    |   0|_                                                                     |
    |____|                                                                      |
    _|  |__                            ///////////////////                      |
    |    | +                          // ||  ||   ||||||  //                    |
    |    |+ +                        //  ||  ||   ||       //                   |
    |    | + +                      //   ||||||   |||||    //                   |
    |____|  + +             __     //    ||  ||   ||       //                   |
    |   |____  886666777777(__)          ||  ||   ||||||  //                    |
    |   |____|)886666777777         //////////////////////                      |
    |   |     " 5555 \  0 0                                                     |
    |   |   "    444 |  66 66                                                   |
    |   |  "     333                                                            |
    |___|_ "    222                                                             |
    |_____|    1111                                                             |
""",
"""
                                                                                |
     ____                                                                       |
    |   0|_ #                                                                   |
    |____|                                                                      |
    _|  |__                            ////////////////////////////             |
    |    | +                          // ||  ||   ||||||   ||      //           |
    |    |+ +                        //  ||  ||   ||       ||       //          |
    |    | + +                      //   ||||||   |||||    ||       //          |
    |____|  + +           __       //    ||  ||   ||       ||       //          |
    |   |____886666777777(__)            ||  ||   ||||||   ||||||  //           |
    |   |____886666777777         /////////////////////////////////             |
    |   |   " 5555 \  0 0                                                       |
    |   |       444 \  66 66                                                    |
    |   |      333                                                              |
    |___|_     222                                                              |
    |_____|    1111                                                             |
""",
"""
              ###                                                               |
     ____                                                                       |
    |   0|_                                                                     |
    |____|                                                                      |
    _|  |__                            /////////////////////////////////////    |
    |    | +                          // ||  ||   ||||||   ||       ||||||  //  |
    |    |+ +                        //  ||  ||   ||       ||       ||  ||   // |
    |    | + +                      //   ||||||   |||||    ||       ||||||   // |
    |____|  + +             __     //    ||  ||   ||       ||       ||       // |
    |   |____  886666777777(__)          ||  ||   ||||||   ||||||   ||      //  |
    |   |____|)886666777777         ////////////////////////////////////////    |
    |   |     " 5555 \  0 0                                                     |
    |   |   "    444 |  66 66                                                   |
    |   |  "     333                                                            |
    |___|_ "    222                                                             |
    |_____|    1111                                                             |

""")
def fuck_him():
    while True:
        for image in range(1,4):
            print(FUCKMAN[image])
            time.sleep()
            os.system('clear')
MISTAKES = len(FUCKMAN) - 1
WORDS = ("RONALDINHO", "BECKHAM", "BRADY", "DURANT", "CROSBY")
puzzle = random.choice(WORDS)
progress = "-" * len(puzzle)
mistake = 0
used = []
print ('Welcome to "Black Fucker"! Try to guess the word. Good luck!')
while mistake < MISTAKES and progress != puzzle:
    print (FUCKMAN[mistake])
    print ("These letters have been: \n", used)
    print ("Word now looks: ", progress)
    assumption = input("\nInsert letter: ")
    assumption = assumption.upper()
    while assumption in used:
        print ("You have already tried this letter", assumption)
        assumption = input("\nInsert letter: ")
        assumption = assumption.upper()
    used.append(assumption)
    if assumption in puzzle:
        print ("Yes, letter", assumption, "in our word!")
        new = ""
        for index in range(len(puzzle)):
            if assumption == puzzle[index]:
                new += assumption
            else:
                new += progress[index]
        progress = new
    else:
        print ("Sorry, this letter,", assumption, ",is absent")
        mistake += 1
    if mistake == MISTAKES:
        print (FUCKMAN[mistake])
        print ("You were fucked!")
        fuck_him()
    else:
        print ("You are champion! It's really", puzzle, "!")

    def fuck_him():
        while True:
            for image in range(1,5):
                print(FUCKMAN[image])
                time.sleep(0.2)
                os.system('clear')



