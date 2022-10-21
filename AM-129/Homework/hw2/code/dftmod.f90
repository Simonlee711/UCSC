module dftmod

  use utility, only : dp, pi
  
  implicit none
  
contains

  !!! ==== Add your matvecprod function here ==== !!!
  ! Function: MATrix VECtor PRODuct -> MATVECPROD
  ! purpose:  will perform the matrix vector product Ax and store the result in y
  !
  !           [ a1, a2, a3 ]    [ x1 ]     [a1*x1 + a2x2 + a3x3]
  !           [ b1, b2, b3 ] *  [ x2 ]  =  [b1x1 + b2x2 + b3x3 ]
  !           [ c1, c2, c3 ]    [ x3 ]     [c1x1 + c2x2 + c3x3 ]
  !                 3x3      *    3x1   =           3x1
  !
  function matvecprod(A,x) result(y)
    implicit none
    real (dp), intent(in) :: A(:,:) ! Rank 2 Matrix
    real (dp), intent(in) :: x(:) ! Rank 1 vector
    real (dp), dimension(size(A,1)) :: y ! given variable for y which is the matrix product

    integer :: i, j !loop iterators
    !Print*, 'Matrix A'
    !print*, A
    !print*, 'vector x'
    !print*, x
    do i = 1, size(A,1)
        y(i) = 0
        do j = 1, size(A,2)
            y(i) = y(i) + A(i,j) * x(j)
        end do
    end do
    !print *, 'solution y'
    !print *, y

  end function matvecprod 


  ! subroutine: dft_TransMat
  ! purpose: Fill transformation matrix for a discrete Fourier transform
  !          on a given domain
  subroutine dft_TransMat(x,k,T)
    implicit none
    real (dp), intent(in)     :: x(:)
    real (dp), intent(out)    :: k(:)
    real (dp), intent(in out) :: T(:,:)
    ! Local variables
    integer :: M, N, i
    real (dp) :: om, dx
    ! Set sizes and base wavenumber
    M=size(T,1)
    N=size(T,2)
    dx = x(2)-x(1)
    om = 2*pi/(N*dx)
    ! Set wavenumbers
    k(1) = 0.0_dp
    do i=2,M,2
      k(i) = i*om/2
      if (i+1<=M) then
        k(i+1) = k(i)
      end if
    end do
    !!! ==== Add your code to fill T here ==== !!!
    ! set all rows to 1/N
    T(1,:) = 1.d0 / N
    do i = 1, size(T,1)
      ! set the ith row to T(i,:) = 2/N cos(k(i) * x) when i is even
      if (mod(i,2) == 0) then
        T(i,:) = 2.d0/N * cos(k(i) * x)
      end if
      ! set the ith row to T(i,:) = 2/N sin(k(i) * x) when i is odd
      if (mod(i,2) == 1 .and. i /= 1) then
        T(i,:) = 2.d0/N * sin(k(i) * x)
      end if
    end do  
   
  end subroutine dft_TransMat
  
  !!! ==== Add your dft_InvTransMat subroutine here ==== !!!
  subroutine dft_InvTransMat(x,k,Tinv)
    implicit none
    real (dp), intent(in)     :: x(:)
    real (dp), intent(in)     :: k(:)
    real (dp), intent(in out) :: Tinv(:,:)

    ! Local variables
    integer :: j
    
    Tinv(:,1) = 1
    
    do j = 1, size(Tinv,2)
      if (mod(j,2) == 0) then
        Tinv(:,j) = cos(k(j) * x)
      end if
      if (mod(j,2) == 1 .and. j /= 1) then
        Tinv(:,j) =  sin(k(j) * x)
      end if
    end do

  end subroutine dft_InvTransMat

end module dftmod
