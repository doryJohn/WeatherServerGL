
import json
import FTPLoadFile as FTP
import FTPparse as MyParse
import sendEmail as email

def lambda_handler(event, context):
    forecastID="lsz266"
    ToAddresses = ["johnwilliamturley@yahoo.com", "iterluxlucis@gmail.com", "JohnOnSiren@zoleo.com"]
    # TODO implement
    myBuff = FTP.FTPLoad(forecastID)
    print("full text")
    print(myBuff)
    summaryTxt, forcastTxt =  MyParse.ParseFTPbuff(myBuff,forecastID)
    print("Summary:")
    print(summaryTxt)
    print("Forcast:")
    print(forcastTxt)
    email.sendEmail(ToAddresses, summaryTxt)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
