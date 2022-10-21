! File: pi.f90
! Author: Simon Lee
! Purpose: The Fortran 90 main module to approximate pi

program pi
    use pimod
    implicit none
    ! variables
    real (dp), parameter    :: thresh = 1.0e-16              ! the tolerance. If it exceeds threshold program ends
    integer, parameter      :: N_Max = 50                   ! Maximum number of terms to sum together. Some end point
    real (dp)     :: pi_appx                                ! the final approximation
    real (dp)     :: diff                                   ! holding the error or the difference between the approximation and pi
    integer (dp)  :: N                                      ! The number of summands needed to achieve tolerance

    ! call function
    call estimate_pi(thresh, N_Max, pi_appx, diff, N)
    ! print final approximation
    print*, N, pi_appx, diff


end program pi