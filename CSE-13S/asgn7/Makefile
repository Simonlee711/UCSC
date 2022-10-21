CC = clang
CFLAGS = -Wall -Wextra -Werror -Wpedantic 
LFLAGS = -lm

all: banhammer

banhammer: banhammer.o bf.o bv.o speck.o ht.o ll.o node.o parser.o
	$(CC) $(CFLAGS) -o banhammer banhammer.o bf.o bv.o speck.o ht.o ll.o node.o parser.o

bf.o: bf.c
	$(CC) $(CFLAGS) -c bf.c

bv.o: bv.c
	$(CC) $(CFLAGS) -c bv.c

speck.o: speck.c
	$(CC) $(CFLAGS) -c speck.c

ht.o: ht.c
	$(CC) $(CFLAGS) -c ht.c

ll.o: ll.c
	$(CC) $(CFLAGS) -c ll.c

node.o: node.c
	$(CC) $(CFLAGS) -c node.c

parser.o: parser.c
	$(CC) $(CFLAGS) -c parser.c

clean:
	rm -f *.o banhammer

format:
	clang-format -i -style=file *.h *.c

