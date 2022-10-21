FC = gfortran
FFLAGS = -Wall -Wextra -Wimplicit-interface -fPIC -fmax-errors=1 -g -fcheck=all -fbacktrace

OBJ = pimod.o pi.o

pi: $(OBJ)
	$(FC) -o $@ $(OBJ) $(FFLAGS)

%.o: %.f90
	$(FC) -c $< $(FFLAGS)

.PHONY: clean

clean:
	rm -f pi *.o *.mod *~

