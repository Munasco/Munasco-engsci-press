/**
AUTHOR: SAIMA ALI
LATEST WORKING VERSION 
FEBRUARY 2ND, 2020
ESC190H1S PROJECT
SNAKE API
 **/

#include <stdlib.h>
#include <stdio.h>

#define BOARD_SIZE 10 //default 10
#define CYCLE_ALLOWANCE 1.5

int CURR_FRAME;
int SCORE;
int MOOGLE_FLAG;
int TIME_OUT;

typedef struct SnekBlock{
	int coord[2];
	struct SnekBlock* next;
} SnekBlock;

typedef struct Snek{
	struct SnekBlock* head;
	struct SnekBlock* tail;
	int length;
} Snek;

typedef struct GameBoard {
	int cell_value[BOARD_SIZE][BOARD_SIZE];
	int occupancy[BOARD_SIZE][BOARD_SIZE];
	struct Snek* snek;
} GameBoard;


GameBoard *init_board();
Snek *init_snek(int a, int b);
int hits_edge(int axis, int direction,  GameBoard *gameBoard);
int hits_self(int axis, int direction,  GameBoard *gameBoard);
int is_failure_state(int axis, int direction,  GameBoard *gameBoard);
int advance_frame(int axis, int direction,  GameBoard *gameBoard);
void end_game(GameBoard **board);
void show_board(GameBoard* gameBoard);
