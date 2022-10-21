! File: pimod.f90
! Author: Simon Lee
! Purpose: Holds the subrouting of the module.

module pimod
    implicit none
    integer, parameter :: dp = kind(0.d0)
    real (dp), parameter :: pi_ref = acos(-1.d0)

contains

subroutine estimate_pi(thresh, N_Max, pi_appx, diff, N)
    implicit none
    ! All the variables
    real (dp), intent(in)     :: thresh             ! the tolerance. If it exceeds threshold program ends
    integer, intent(in)       :: N_Max              ! Maximum number of terms to sum together. Some end point
    real (dp), intent(out)    :: pi_appx            ! the final approximation
    real (dp), intent(out)    :: diff               ! holding the error or the difference between the approximation and pi
    integer (dp), intent(out) :: N                  ! The number of summands needed to achieve tolerance
    !local variables
    integer (dp) :: i 
    
    ! subroutine
    N = 0
    pi_appx = 0.d0
    
    do i = 1, N_Max       ! loop to keep running iterations
        
        !approximate pi
        pi_appx = pi_appx + (16.d0 ** -N) * (4.d0/(8.d0*N+1.) - 2.d0/(8.d0*N+4.d0) - 1.d0/(8.d0*N+5.d0) - 1.d0/(8.d0*N+6.d0))

        !a checker to see what iteration they are on
        N = N + 1

        ! checker to see if it should keep looping
        diff = ABS(pi_appx - pi_ref)
        if (diff < thresh) then
            exit
        endif

        ! print statement
        print*, N, pi_appx, diff
    end do
end subroutine estimate_pi
end module pimod
