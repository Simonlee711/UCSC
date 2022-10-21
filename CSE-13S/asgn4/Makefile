CC = clang
CFLAGS = -Wall -Wextra -Werror -Wpedantic 
LFLAGS = -lm

all: tsp 

tsp: tsp.o stack.o graph.o path.o
	$(CC) $(CFLAGS) -o tsp tsp.o stack.o graph.o path.o $(LFLAGS)

tsp.o: tsp.c
	$(CC) $(CFLAGS) -c tsp.c

stack.o: stack.c
	$(CC) $(CFLAGS) -c stack.c

graph.o: graph.c
	$(CC) $(CFLAGS) -c graph.c

path.o: path.c
	$(CC) $(CFLAGS) -c path.c

clean:
	rm -f *.o tsp

format:
	clang-format -i -style=file tsp.c stack.c graph.c path.c stack.h graph.h path.h vertices.h 
