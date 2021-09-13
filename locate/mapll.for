      SUBROUTINE MAPLL (X,Y,ALAT,ALONG,SLAT,SGN,E,RE)
C$*****************************************************************************
C$                                                                            *
C$                                                                            *
C$    DESCRIPTION:                                                            *
C$                                                                            *
C$    This subroutine converts from geodetic latitude and longitude to Polar  *
C$    Stereographic (X,Y) coordinates for the polar regions.  The equations   *
C$    are from Snyder, J. P., 1982,  Map Projections Used by the U.S.         *
C$    Geological Survey, Geological Survey Bulletin 1532, U.S. Government     *
C$    Printing Office.  See JPL Technical Memorandum 3349-85-101 for further  *
C$    details.                                                                *
C$                                                                            *
C$                                                                            *
C$    ARGUMENTS:                                                              *
C$                                                                            *
C$    Variable    Type        I/O    Description                              *
C$                                                                            *
C$    ALAT       REAL*4        I     Geodetic Latitude (degrees, +90 to -90)  *
C$    ALONG      REAL*4        I     Geodetic Longitude (degrees, 0 to 360)   *
C$    X          REAL*4        O     Polar Stereographic X Coordinate (km)    *
C$    Y          REAL*4        O     Polar Stereographic Y Coordinate (km)    *
C$                                                                            *
C$                                                                            *
C$                  Written by C. S. Morris - April 29, 1985                  *
C$                  Revised by C. S. Morris - December 11, 1985               *
C$                                                                     	      *
C$                  Revised by V. J. Troisi - January 1990                    *
C$                  SGN - provides hemisphere dependency (+/- 1)              *
C$		    Revised by Xiaoming Li - October 1996                     *
C$		    Corrected equation for RHO                                *
C$*****************************************************************************
      REAL*4 X,Y,ALAT,ALONG,E,E2,CDR,PI,SLAT,MC
C$*****************************************************************************
C$                                                                            *
C$    DEFINITION OF CONSTANTS:                                                *
C$                                                                            *
C$    Conversion constant from degrees to radians = 57.29577951.              *
      CDR=57.29577951
      E2=E*E
C$    Pi=3.141592654.                                                         *
      PI=3.141592654
C$                                                                            *
C$*****************************************************************************
C     Compute X and Y in grid coordinates.
      IF (ABS(ALAT).LT.PI/2.) GOTO 250
      X=0.0
      Y=0.0
      GOTO 999
  250 CONTINUE
      T=TAN(PI/4.-ALAT/2.)/((1.-E*SIN(ALAT))/(1.+E*SIN(ALAT)))**(E/2.)
      IF (ABS(90.-SLAT).LT.1.E-5) THEN
      RHO=2.*RE*T/((1.+E)**(1.+E)*(1.-E)**(1.-E))**(1/2.)
      ELSE
      SL=SLAT*PI/180.
      TC=TAN(PI/4.-SL/2.)/((1.-E*SIN(SL))/(1.+E*SIN(SL)))**(E/2.)
      MC=COS(SL)/SQRT(1.0-E2*(SIN(SL)**2))
      RHO=RE*MC*T/TC
      END IF
      Y=-RHO*SGN*COS(SGN*ALONG)
      X= RHO*SGN*SIN(SGN*ALONG)
  999 CONTINUE
      END
