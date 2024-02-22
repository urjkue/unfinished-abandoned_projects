#include <stdio.h>
#include <string.h>

#define ROWS 3
#define COLS 3

struct Player {
    char name[25];
    int score;
};

void game(struct Player players[], int numplayers) {

            int maxpt = 0;

            char grid[ROWS][COLS][10] = {
                {"1", "2", "3"},
                {"4", "5", "6"},
                {"7", "8", "9"}
            };

        for(int y =0; y < 9 ; y++){

        for(int i = 0; i < numplayers; i++){



            printf("The grid is:\n");
            for (int i = 0; i < ROWS; i++) {
                for (int j = 0; j < COLS; j++) {
                    printf("%s ", grid[i][j]);
                }
                printf("\n");
            }
            printf("hello\n");
            int place;
            printf("%s, please enter a number: ", players[i].name);
            scanf("%d", &place);
            if(place > 3 && place < 7){
                if(i == 0){
                    strcpy(grid[1][place-4] , "O");
                }else{
                    strcpy(grid[1][place-4] , "X");
                }

            }else if(place >6){
                 if(i == 0){
                    strcpy(grid[2][place-7] , "O");
                }else{
                    strcpy(grid[2][place-7] , "X");
                }

            }else{
                if(i == 0){
                    strcpy(grid[0][place-1] , "O");
                }else{
                    strcpy(grid[0][place-1] , "X");
                }
            }











    }
        }
}

int main() {
    int numPlayers = 2;


    struct Player players[numPlayers];
    for (int i = 0; i < numPlayers; i++) {
        players[i].score = 0;
        sprintf(players[i].name, "Player %d", i + 1);
    }

    for (int i = 0; i < numPlayers; i++) {
        printf("%s\n", players[i].name);
        printf("%d\n", players[i].score);
    }

    game(players, numPlayers);

    return 0;
}
