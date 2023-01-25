import wiringpi
import time

SPEAKER = 26
SW = 21
DO=262
RE=294
MI=330
FA=349
SO=392
RA=440
Z=0
NOTE16 = 0.125 #16分音符=125ms
#ドレミファミレド
#ミファソラソファミ
#ド ド ド ド
#ドドレレミミファファミレド
gakufu = [[DO, 4], [RE, 4], [MI, 4], [FA, 4], [MI, 4], [RE, 4], [DO, 4], [Z, 4],
          [MI, 4], [FA, 4], [SO, 4], [RA, 4], [SO, 4], [FA, 4], [MI, 4], [Z, 4],
          [DO, 4], [Z,4], [DO, 4], [Z,4], [DO, 4], [Z,4], [DO, 4], [Z,4],
          [DO, 2], [Z,0.1], [DO, 2], [Z,0.1], [RE, 2], [Z,0.1], [RE, 2], [Z,0.1],
          [MI, 2], [Z,0.1], [MI, 2], [Z,0.1], [FA, 2], [Z,0.1], [FA, 2], [Z,0.1],
          [MI, 4], [RE,4], [DO, 4]]

wiringpi.wiringPiSetupGpio( ) 
wiringpi.softToneCreate(SPEAKER)
wiringpi.pinMode(SW, 0)
wiringpi.pullUpDnControl(SW, 2)

while wiringpi.digitalRead( SW ) == 1 :
    pass

while wiringpi.digitalRead( SW ) == 0 :
    pass

for oto in gakufu:
    if wiringpi.digitalRead( SW ) == 0 :
        break
    wiringpi.softToneWrite(SPEAKER, oto[0])
    if wiringpi.digitalRead( SW ) == 0 :
        break
    time.sleep(oto[1] * NOTE16)
    if wiringpi.digitalRead( SW ) == 0 :
        break
    
wiringpi.softToneWrite(SPEAKER, Z)
