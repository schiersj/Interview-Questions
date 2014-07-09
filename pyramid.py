import sys
star = 'X'
numSpaces = 0
width = 23

for x in xrange(0,width+1):
    if (x % 2) != 0:
        numSpaces = (width - x) / 2
        for i in xrange(0,numSpaces):
            sys.stdout.write(' ')
        for y in xrange(0,x):
            sys.stdout.write(star)
        sys.stdout.write('\n')

#            X
#           XXX
#          XXXXX
#         XXXXXXX
#        XXXXXXXXX
#       XXXXXXXXXXX
#      XXXXXXXXXXXXX
#     XXXXXXXXXXXXXXX
#    XXXXXXXXXXXXXXXXX
#   XXXXXXXXXXXXXXXXXXX
#  XXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXX
