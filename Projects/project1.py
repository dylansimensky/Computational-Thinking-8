###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("flowers")
q1 = codesters.Square( 100, 100, 200, 'LightPink')
q2 = codesters.Square( -100, 100, 200, 'Violet')
q3 = codesters.Square(-100, -100, 200, 'SkyBlue')
q4 = codesters.Square(100, -100, 200, 'PeachPuff')
s1 = codesters.Sprite("dog3", 100, 100)
s1.set_size(0.6)
s2 = codesters.Sprite("chicagocity", -100, -100)
s2.set_size(0.4)
s3 = codesters.Sprite("softball1", 100, -100)
s3.set_size(0.4)
s4 = codesters.Sprite("jessie1", -100, 100)
s4.set_size(0.6)