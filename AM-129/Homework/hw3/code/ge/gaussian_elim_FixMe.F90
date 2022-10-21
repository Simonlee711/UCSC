#define PRINTINFO
program gauss
! ################## main ################### !
  implicit none
  real, allocatable, dimension(:,:) :: A, At
  real, allocatable, dimension(:) :: b, b2
  integer :: i

  allocate(A(3,3))
  ! initialize matrix A and vector b
  A = reshape((/2, 4, 7, 3, 7, 10, -1, 1, -4/), (/3,3/))  
  b = (/1, 3, 4/)

  At = reshape((/2, 3, -1, 4, 7, 1, 7, 10, -4/), (/3,3/))
  b2 = (/1, 3, 4/)

#ifdef PRINTINFO
  ! print augmented matrix
  do i = 1, 3           ! i is row
     print*, A(i,:), "|", b(i)
  end do
#endif

#ifdef PRINTINFO  
  print*, ""    ! print a blank line
  print*, "Gaussian elimination........"
  call gaussian_elimination(A,b)
#endif

#ifdef PRINTINFO  
  ! print echelon form
  print*, "***********************"
  do i = 1, 3
     print*, A(i,:), "|", b(i)
  end do

  print*, ""    ! print a blank line
  print*, "back subs......"
  call backsubstitution(A,b)
#endif

#ifdef PRINTINFO  
  ! print the results
  print*, "***********************"
  do i = 1, 3
     print*, A(i,:), "|", b(i)
  end do

  print*, ""
  print*, "The solution vector is;"
  do i = 1, 3
     print*, b(i)
  end do
#endif

#ifdef PRINTINFO
   print*,""
   print*, "***********************"
   print*, "A transposed gaussian elimination...."
   print*, "A^T * x = b"
   ! print augmented matrix
   call gaussian_elimination(At,b2)
   call backsubstitution(At,b2)
   print*, "The solution vector is;"
   do i = 1, 3
      print*, b2(i)
   end do
#endif

! ############# subroutines #################### !

contains
subroutine gaussian_elimination(A, b)
  implicit none
  real, allocatable, dimension(:,:), intent(INOUT) :: A
  real, allocatable, dimension(:), intent(INOUT) :: b
  integer :: i, j
  real :: factor

  ! gaussian elimination
  do j = 1, 2           ! j is column
     do i = j+1, 3       ! i is row
        factor = A(i,j)/A(j,j)
        A(i,:) = A(i,:) - factor*A(j,:)
        b(i) = b(i) - factor*b(j)
     end do
  end do
end subroutine gaussian_elimination


subroutine backsubstitution(A,b)
  implicit none
  real, allocatable, dimension(:,:), intent(INOUT) :: A
  real, allocatable, dimension(:), intent(INOUT) :: b
  integer :: i,j
  real :: factor

  ! doing back substitution
  do j = 3, 2, -1            ! j is column
     do i = j-1, 1, -1        ! i is row
        factor = A(i,j)/A(j,j)
        A(i,:) = A(i,:) - factor*A(j,:)
        b(i) = b(i) - factor*b(j)
     end do
  end do


  ! overwrite the solution vector to b
  do i = 1, 3
     b(i) = b(i)/A(i,i)
  end do
end subroutine backsubstitution

end program gauss