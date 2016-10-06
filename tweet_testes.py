#!/usr/bin/python
import os
import sys
import csv
import datetime
import time
import twitter
import config as CFG


#Conta do twitter da operadora de internet
CTID=("@vivoemrede" , "@claroBrasil" , "@NEToficial" , "@TIMBrasil", "@SKYresponde", "@digaoi")

def test():
        print 'Iniciando testes...'
        a = os.popen("/usr/bin/speedtest-cli --simple").read()
        #Quebra o retorno para adicionar ao tweet
        lines = a.split('\n')
        print a
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]
        print date,p, d, u
        #Salva o ultimo resultado
	if CFG.KEEPDATA:
	       out_file = open('/opt/scripts/data.csv', 'a')
	       writer = csv.writer(out_file)
	       writer.writerow((ts*1000,p,d,u))
	       out_file.close()

        my_auth = twitter.OAuth(CFG.TOKEN,CFG.TOKEN_KEY,CFG.CON_SEC,CFG.CON_SEC_KEY)
        twit = twitter.Twitter(auth=my_auth)

  	#Tweet das informacoes coletadas
        if "Cannot" in a:
                try:
                        tweet="Ei "+CTID[CFG.CARRIER]+" pq minha "+CFG.HASHTAG+" fica caindo? vao dar desconto na fatura?"
                        twit.statuses.update(status=tweet)
                except:
                        pass

        # Tweeta se a velocidade for menor que o esperado
        elif eval(d)<CFG.THRESHOLD:
                print "Tweetando"
                try:
                    
                        tweet=CTID[CFG.CARRIER]+" por que minha internet esta com " + str(int(eval(d))) + " de down e " + str(int(eval(u))) + "up enquanto eu pago por "+CFG.SPEED+"Mb? "+CFG.HASHTAG
                        twit.statuses.update(status=tweet)
			twit.direct_messages.new(user=CTID[CFG.CARRIER],text=CFG.PDATA)
                except Exception,e:
                        print str(e)
                        pass
        return
        
if __name__ == '__main__':
        test()
        print 'Fim'

