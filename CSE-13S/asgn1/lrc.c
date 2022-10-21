//////////////////////////////////////
// Assignment 1: Left Right Center  //
// Author: Simon Lee		    //
// Class & Term: CSE 13s Spring 2021//
//////////////////////////////////////
#include "philos.h"

#include <ctype.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

//SOURCE: Darell Long Assignment 1 document
//PARAMETERS:
//pos: The position of the current player
//players:  number of players in the game

static inline uint32_t left_person(uint32_t pos, uint32_t players) {
    return ((pos + players - 1) % players);
}
//SOURCE: Darell Long Assignment 1 document
//PARAMETERS:
//pos: The position of the current player
//players:  number of players in the game

static inline uint32_t right_person(uint32_t pos, uint32_t players) {
    return ((pos + 1) % players);
}

int main(void) {
    uint32_t players;
    uint32_t seed = 0;
    //int winner = 0;

    //enter random seed
    printf("Random seed: ");
    uint32_t valid_seed = scanf("%u", &seed);
    if ((valid_seed != 1 || seed < 1)) {
        fprintf(stderr,
            "Invalid seed\n"); //tutor Tristan told me to use fprintf to print error messages
        return 1;
    }
    srandom(seed);

    //# of players user input
    printf("How many players? ");
    uint32_t valid_players = scanf("%u", &players);
    if (valid_players != 1 || players > 14 || players < 2) {
        fprintf(stderr, "Invalid number of players\n"); //tutor Tristan taught me to use fprintf
        return 1;
    }

    //assign money
    uint32_t money[14]; //assigning money to number of players in the game using arrays
    for (uint32_t i = 0; i < players; i++) {
        money[i] = 3;
    }

    //actual game
    uint32_t players_in = players;
    uint32_t pos = 0;
    uint32_t dice_roll = 0;
    uint32_t money_pot = 0;
    while (players_in > 1) {
        if (money[pos]
            >= 3) { //Eugene's section broke down the structure of how to determine the rolls
            dice_roll = 3;
        } else {
            dice_roll = money[pos];
        }

        //dice enumeration used in roll function
        typedef enum faciem { PASS, LEFT, RIGHT, CENTER } faces;
        faces die[] = { LEFT, RIGHT, CENTER, PASS, PASS, PASS };

        if (dice_roll != 0) { // this print statement does not print for people who do not roll.
            for (uint32_t i = 0; i < 1; i++) {
                printf("%s rolls...", philosophers[pos]);
            }
            for (uint32_t i = 0; i < dice_roll; i++) {
                faces face_die = die[random() % 6];
                switch (face_die) {
                case LEFT:
                    printf(" gives $1 to %s", philosophers[left_person(pos, players)]);
                    money[pos] = money[pos] - 1;
                    money[left_person(pos, players)] += 1;
                    break;
                case RIGHT:
                    printf(" gives $1 to %s", philosophers[right_person(pos, players)]);
                    money[pos] = money[pos] - 1;
                    money[right_person(pos, players)] += 1;
                    break;
                case CENTER:
                    printf(" puts $1 in the pot");
                    money[pos] = money[pos] - 1;
                    money_pot = money_pot + 1;
                    break;
                default: printf(" gets a pass"); break;
                }
            }
        }
        //checking for winner
        players_in = 0;
        for (uint32_t j = 0; j < players;
             j++) { //tutor Miles advised me to incorporate this to check for winner
            if (money[j] != 0) {
                players_in += 1;
            }
        }

        if (players_in == 1) {
            uint32_t winner_money = 0;
            for (uint32_t i = 0; i < players; i++) {
                if (money[i] != 0) {
                    winner_money = money[i];
                    printf("\n%s wins the $%d pot with $%d left in the bank!\n", philosophers[i],
                        money_pot, money[i]);
                    return 0;
                }
            }
        }

        //next iteration
        if (dice_roll > 0) { // so no unnecessary new lines would print
            printf("\n");
        }
        pos = (pos + 1) % players;
        continue;
    }
    return 0;
}
