CC = clang
CFLAGS = -Wall -Wextra -Werror -Wpedantic
LFLAGS = -lm

all: sorting

sorting: sorting.o bubble.o shell.o quick.o stack.o queue.o
	$(CC) $(CFLAGS) -o sorting sorting.o bubble.o shell.o quick.o stack.o queue.o $(LFLAGS)

sorting.o: sorting.c
	$(CC) $(CFLAGS) -c sorting.c

bubble.o: bubble.c
	$(CC) $(CFLAGS) -c bubble.c

shell.o: shell.c
	$(CC) $(CFLAGS) -c shell.c

quick.o: quick.c
	$(CC) $(CFLAGS) -c quick.c

stack.o: stack.c
	$(CC) $(CFLAGS) -c stack.c

queue.o: queue.c
	$(CC) $(CFLAGS) -c queue.c

clean:
	rm -f *.o sorting

format:
	clang-format -i -style=file sorting.c bubble.c shell.c quick.c stack.c queue.c set.c set.h queue.h stack.h quick.h shell.h bubble.h gaps.h


