
        program locate

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c
c LOCATE - This program transforms I,J coordinates of an SSM/I grid cell
c          to latitude and longitude coordinates. This program provides
c          the inverse functions as well. LOCATE interfaces to the revised
c          forms of the subroutines, MAPXY and MAPLL.
c
c  User-defined Paramters:
c
c     gtype   : Integer supplied by the user to describe one of the three
c               grid cell dimensions (12.5 km, 25.0 km).
c
c     ihem    : Integer supplied by the user to describe one of the two
c               polar regions (1=North , 2=South)
c
c     itrans  : Integer supplied by the user to describe the type of
c               transformation LOCATE will perform (1=I,J-to-Lat,Lon;
c               2=Lat,Lon-to-I,J)
c
c     i,j     : Integers supplied by the user when itrans = 1. These 
c               integers describe the position of a cell in an SSM/I grid.
c
c     lat,lon : Reals supplied by the user when itrans = 2. These
c               integers describe the latitude and longitude in an SSM/I
c               grid which LOCATE will transform to an I,J grid cell position.
c               Note: All latitudes and longitudes must be entered as 
c                     positive numbers!
c
c  Internal:
c
c     x,y     : Distance in kilometers from the origin of the grid 
c               (ie., pole).
c     
c     alat,
c     alon    : Computed latitude and longitude returned from MAPXY.
c
c     SGN     : Sign of the latitude (positive = north latitude, 
c               negative = south latitude)
c
c     delta   : Meridian offset for the SSM/I grids (0 degrees for
c               the South Polar grids; 45 degrees for the North Polar
c               grids. 
c
c     kk      : Integer variable used for reorientation of the grid. The
c               grid is 'flipped' in the Y direction for transformations.
c
c     SLAT    : Standard latitude for the SSM/I grids is 70 degrees.
c
c     numy    : Number of lines in an SSM/I grid. This attribute varies
c               for each of the six grids.
c
c     cell    : Size of the SSM/I grid ( 12.5 km, 25.0 km)
c
c     xydist  : Distance from the origin of the grid in the cartesian plane.
c               The x-y coordinates for the edge of the lower left pixel
c               is (3850.0, 5350.0) for the northern grids and 
c               (3950.0, 3950.0) for the southern grids.
c
c     RE      : Radius of the earth in kilometers.
c
c     E       : Eccentricity of the Hughes ellipsoid
c
c     E2      : Eccentricity squared
c
c     PI      : Pi
c  Written by  V.J.Troisi - January, 1990
c  Updated by  N.A.Sandoval - November, 1995 - Switched i,j in the 
c              equation to be consistent i-row, j-column.
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc


        real SLAT,E,RE,PI
        real alat,alon,x,y
        integer ihem 
        real lat, lon
        real SGN, delta
        integer numy(2,3)
        real cell(2), xydist(2,2)
        data numy / 896, 664, 448, 332, 224, 166 /
        data cell     / 12.5 , 25.0 /
        data xydist   / 3850.0 , 5350.0 , 3950.0 , 3950 /
      
        SLAT = 70.
        RE = 6378.273
        E2 = .006693883
        PI = 3.141592654
        E =  sqrt(E2)
c
c Query for the SSM/I grid cell size.
c
        print *,'Enter the grid cell dimension:'
        print *,' 1. 12.5 Km'
        print *,' 2. 25.0 Km'
        read *,gtype
c
c Query for polar region of interest.
c
        print *,'Enter the hemisphere of interest:'
        print *,' 1. North'
        print *,' 2. South'
        read *,ihem
c
c Define the sign and meridian offset (delta) for the SSM/I grids.
c
        if (ihem.eq.1) then
           SGN   = 1.0
           delta = 45.
        else
           SGN   = -1.0
           delta = 0.0
        endif
c
c Query for translation type.
c
        print *,'Enter one of the following transform functions:'
        print *,' 1. Convert I,J to Latitude, Longitude'
        print *,' 2. Convert Latitude, Longitude to I,J'
        read *, itrans
c
c Start translation
c
        if (itrans.eq.1) then
c
c Obtain the I,J position of the grid cell to transform to Latitude 
c and Longitude
c      
          print *,'Enter the column number'
          if(ihem.eq.1 .and. gtype.eq.1) 
     +      print *,'the valid range is (1-608)'
          if(ihem.eq.1 .and. gtype.eq.2)
     +      print *,'the valid range is (1-304)'
          if(ihem.eq.2 .and. gtype.eq.1)
     +      print *,'the valid range is (1-632)'
          if(ihem.eq.2 .and. gtype.eq.2)
     +      print *,'the valid range is (1-316)'
          read *,j

          print *,'Enter the row number'
          if(ihem.eq.1 .and. gtype.eq.1) 
     +      print *,'the valid range is (1-896)'
          if(ihem.eq.1 .and. gtype.eq.2)
     +      print *,'the valid range is (1-448)'
          if(ihem.eq.2 .and. gtype.eq.1)
     +      print *,'the valid range is (1-664)'
          if(ihem.eq.2 .and. gtype.eq.2)
     +      print *,'the valid range is (1-332)'
          read *,i
c
c Convert I,J pairs to x and y distances from origin. For some image
c display programs, the grid will be 'flipped' in the 'Y' direction.
c+
c Changed j for i and i for j to be consistant, NAS (11/95).
c-
             x=((j-1)*cell(gtype))-(xydist(1,ihem)-cell(gtype)/2.)
             kk=numy(ihem,gtype)-(i-1)           
             y=((kk-1)*cell(gtype))-(xydist(2,ihem)-cell(gtype)/2.)
c
c Transform x and y distances to latitude and longitude
c
             call mapxy (x,y,alat,alon,SLAT,SGN,E,RE)
c
c Transform radians to degrees.
c
             alon=alon*180./PI
             alat=alat*180./PI
             alon=alon-delta   
c
c Convert longitude to positive degrees
c
             if (alon.le.0.0) alon=alon+360.
             if (alon.ge.360.0) alon=alon-360.
c
c Print the latitude and longitude for the center of the I,J cell.
c
             print *,alat,alon
       else
c
c Obtain the latitude and longitude pair and transform to cell where
c that pair is located.
c
             print *,'Enter latitude and longitude (positive values):'
             read *,lat,lon
c
c Transform degrees to radians
c
             alat=abs(lat)*PI/180.
             alon=(lon+delta)*PI/180.
c
c Transform latitude and longitude to x and y distances from origin
c
           call mapll (x,y,alat,alon,SLAT,SGN,E,RE)
           print *,x,y
c
c Convert x and y distances from origin to I,J pair (ii,jj)
c
             ii=nint((x+xydist(1,ihem)-cell(gtype)/2.)/cell(gtype))+1
             jj=nint((y+xydist(2,ihem)-cell(gtype)/2.)/cell(gtype))+1
c
c Flip grid orientation in the 'Y' direction
c 
             kk=numy(ihem,gtype)-(jj-1)
c
c Print the I,J location of the cell.
c
             print *,ii,kk

          endif
      end

