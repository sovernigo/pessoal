#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Lista{
  int pos_x;
  int pos_y;
  struct Lista *prox;
}Fila;

//void init_Fila(Fila *f);
//int expansao(int ini_x, int ini_y, int dest_x, int dest_y, int tam_x, int tam_y, int matriz[][]);

int main (){

  int tam_x, tam_y;
  int ini_x, ini_y;
  int dest_x, dest_y;
  bool achou = false;

  int coord_x1, coord_y1, coord_x2, coord_y2;

  int num_obs;

  scanf("%d", &tam_x);
  scanf("%d\n", &tam_y);

  int Grid[tam_x][tam_y];

  for (int j = 0; j < tam_x; j++) {
    for (int k = 0; k < tam_y; k++) {
      Grid[j][k] = -3;
    }
  }

  scanf("%d", &ini_x);
  scanf("%d\n", &ini_y);

  scanf("%d", &dest_x);
  scanf("%d\n", &dest_y);

  scanf("%d\n", &num_obs);

  for(int i = 0; i < num_obs; i ++){
    int coord[4];

    scanf("%d ", &coord[0]);
    scanf("%d ", &coord[1]);
    scanf("%d ", &coord[2]);
    scanf("%d ", &coord[3]);

    Grid[coord[0]][coord[1]] = -1;
    Grid[coord[2]][coord[3]] = -1;
  }
  printf("teste" );

  Fila *p;
  p = (Fila *)malloc(sizeof(Fila));
  p->prox = NULL;

  int eixo_x, eixo_y;
  int x = ini_x;
  int y = ini_y;

  #pragma omp{

    while(p->prox != NULL && achou == false){

      #pragma omp for
        for(int k = 0; k < 4; k++){

          if(x == dest_x && y == dest_y){
            achou = true;
          }

          eixo_x = k % 2;
          eixo_y = k / 2;

          if(eixo_y == 0 && 0 >= x < tam_x){
            if(eixo_x == 0){
              x -= x;
              if(-1 < Grid[x][y] <= Grid[x+1][y]){
                continue;
              }
              else{
                Grid[x][y] = Grid[x+1][y] + 1;
              }
            }
            if(eixo_x == 1){
              x += x;
              if(-1 < Grid[x][y] <= Grid[x-1][y]){
                continue;
              }
              else{
                Grid[x][y] = Grid[x-1][y] + 1;
              }
            }
          }

          if(eixo_y == 1 && 0 >= y < tam_y){
            if(eixo_x == 0){
              y -= y;
              if(-1 < Grid[x][y] <= Grid[x][y+1]){
                continue;
              }
              else{
                Grid[x][y] = Grid[x][y-1] + 1;
              }
            }
            if(eixo_x == 1){
              y += y;
              if(-1 < Grid[x][y] <= Grid[x][y-1]){
                continue;
              }
              else{
                Grid[x][y] = Grid[x][y+1] + 1;
              }
            }
          }
          //insere_fila();
        }
      }

      if(achou == true){
        x = dest_x;
        y = dest_y;

        while(pos_x != ini_x || pos_y != ini_y){
          for(int t = 0;t < 4; t++){
            eixo_x = t / 2;
            eixo_y = t % 2;
            if(eixo_x == 0  && 0 >= x < tam_x){
              if(eixo_y == 0 && Grid[x - 1][y] == Grid[x][y] - 1){
                x -= x;
              }
              if(eixo_y == 1 && Grid[x + 1][y] == Grid[x][y] - 1){
                x ++;
              }
            }
            if(eixo_x == 1 && 0 >= y < tam_y){
              if(eixo_y == 0 && Grid[x][y - 1] == Grid[x][y]){
                y --;
              }
              if(eixo_y == 1 && Grid[x][y - 1] == Grid[x][y] - 1){
                y++;
              }
            }
          }
        }
      }


    for (int j = 0; j < tam_x; j++) {
      for (int k = 0; k < tam_y; k++) {
        printf("%d", Grid[j][k]);
      }
    }
}

void insere_fila(){


}

/*void init_Fila(Fila *f){
  Fila *p;
  p = (Fila *)malloc(sizeof(Fila));
  p->prox = NULL;
  return;
}

void lerArquivo(FILE *arquivo){

}

int expansao(int ini_x, int ini_y, int dest_x, int dest_y, int tam_x, int tam_y, int matriz[][]){
  int eixo_x, eixo_y;
  int x = ini_x;
  int y = ini_y;

  int Grid= *matriz;
  Grid[x][y] = 0;
  bool achou = false;
  #pragma omp{

    while(f->prox != NULL && achou == false){

      #pragma omp for{
        for(int k = 0; k < 4; k++){

          if(x == dest_x && y == dest_y){
            achou = true;
          }

          eixo_x = k % 2;
          eixo_y = k / 2;

          if(eixo_y == 0 && 0 >= x < tam_x){
            if(eixo_x == 0){
              x -= x;
              if(-1 < Grid[x][y] <= Grid[x+1][y]){
                continue;
              }
              else{
                Grid[x][y] = Grid[x+1][y] + 1;
              }
            }
            if(eixo_x == 1){
              x += x;
              if(-1 < Grid[x][y] <= Grid[x-1][y]){
                continue;
              }
              else{
                Grid[x][y] = Grid[x-1][y] + 1;
              }
            }
          }

          if(eixo_y == 1 && 0 >= y < tam_y){
            if(eixo_x == 0){
              y -= y;
              if(-1 < Grid[x][y] <= Grid[x][y+1]){
                continue;
              }
              else{
                Grid[x][y] = Grid[x][y-1] + 1;
              }
            }
            if(eixo_x == 1){
              y += y;
              if(-1 < Grid[x][y] <= Grid[x][y-1]){
                continue;
              }
              else{
                Grid[x][y] = Grid[x][y+1] + 1;
              }

            }
          }
          //insere_fila();
        }
      }
  return Grid;
}
*/
