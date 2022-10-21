CC = clang
CFLAGS = -Wall -Wextra -Werror -Wpedantic 
LFLAGS = -lm
all: encode decode entropy

encode: encode.o stack.o code.o pq.o node.o io.o huffman.o
	$(CC) $(CFLAGS) -o encode encode.o stack.o code.o pq.o node.o io.o huffman.o $(LFLAGS)

decode: decode.o io.o stack.o huffman.o code.o pq.o node.o
	$(CC) $(CFLAGS) -o decode decode.o io.o stack.o huffman.o code.o pq.o node.o $(LFLAGS)

entropy: entropy.o
	$(CC) $(CFLAGS) -o entropy entropy.o $(LFLAGS)

io.o: io.c
	$(CC) $(CFLAGS) -c io.c

stack.o: stack.c
	$(CC) $(CFLAGS) -c stack.c

huffman.o: huffman.c
	$(CC) $(CFLAGS) -c huffman.c

code.o: code.c
	$(CC) $(CFLAGS) -c code.c

pq.o: pq.c
	$(CC) $(CFLAGS) -c pq.c

node.o: node.c
	$(CC) $(CFLAGS) -c node.c

clean:
	rm -f *.o encode decode entropy  

format:
	clang-format -i -style=file *.c *.h


