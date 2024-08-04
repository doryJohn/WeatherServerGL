
import json
import FTPLoadFile as FTP
import FTPparse as MyParse
import sendEmail as email
import GetCanadianWeather as GetCan

def lambda_handler(event, context):
    ToAddresses = ["johnwilliamturley@yahoo.com"]  #this is for diagnostic purposes

#### Start with NOAA summary and lsz266
    forecastID="lsz266"
    myBuff = FTP.FTPLoad(forecastID)
    summaryTxt, forcastTxt =  MyParse.ParseFTPbuff(myBuff,forecastID)
#  send out summaryTxt
    email.sendEmail(ToAddresses, summaryTxt)    #send to monitering emails
#    split into chunks and send to zoleo
    chunk_size = 223
    for i in range(0, len(summaryTxt), chunk_size):
        email.sendEmail(["JohnOnSiren@zoleo.com"],summaryTxt[i:i+chunk_size]) 
#### Now do Canadian Forcast
    canforcastTxt = GetCan.GetForcast()
    email.sendEmail(ToAddresses, canforcastTxt)    #send to monitering emails
 #    split into chunks and send to zoleo
    chunk_size = 223
    for i in range(0, len(canforcastTxt), chunk_size):
        email.sendEmail(["JohnOnSiren@zoleo.com"],canforcastTxt[i:i+chunk_size])
#### now go back to forcastTxt for lsz266 and send it out
    email.sendEmail(ToAddresses, forcastTxt)    #send to monitering emails
    
 #    split into chunks and send to zoleo
    chunk_size = 223
    for i in range(0, len(forcastTxt), chunk_size):
        email.sendEmail(["JohnOnSiren@zoleo.com"],forcastTxt[i:i+chunk_size])

       
#### Now do NOAA lsz267      
    forecastID="lsz267"
    myBuff = FTP.FTPLoad(forecastID)
    summaryTxt, forcastTxt =  MyParse.ParseFTPbuff(myBuff,forecastID)
  # Send out forcastTxt first
    email.sendEmail(ToAddresses, forcastTxt)    #send to monitering emails
 #    split into chunks and send to zoleo
    chunk_size = 223
    for i in range(0, len(forcastTxt), chunk_size):
        email.sendEmail(["JohnOnSiren@zoleo.com"],forcastTxt[i:i+chunk_size])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
