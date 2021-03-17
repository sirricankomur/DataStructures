#include <stdio.h>

#define MAX_SIZE 5

struct Stack
{
  char stack[MAX_SIZE];
  int top;
};
typedef struct Stack st;

void create_stack(st *s)
{
  s->top = -1;
}

int is_empty(st *s)
{
  if (s->top == -1)
  {
    return 1;
  }
  return 0;
}

int is_full(st *s)
{
  if (s->top == MAX_SIZE - 1)
  {
    return 1;
  }
  return 0;
}

void push(st *s, char item)
{
  if (is_full(s))
  {
    printf("Stack is full!\n");
    return;
  }
  s->top++;
  s->stack[s->top] = item;
}

void pop(st *s)
{
  if (is_empty(s))
  {
    printf("Stack is empty!\n");
  }
  s->stack[s->top] = 0;
  s->top--;
}

void display(st *s)
{
  for (int i = MAX_SIZE - 1; i >= 0; i--)
  {
    printf("%c\n", s->stack[i]);
  }
  printf("-\n");
}

int main(void)
{
  st *s = (st *)malloc(sizeof(st));

  create_stack(s);

  push(s, 'A');
  push(s, 'B');
  push(s, 'C');
  push(s, 'D');
  push(s, 'F');
  display(s);
 
  pop(s);
  pop(s);
  pop(s);  
  display(s);
  
  return 0;
}