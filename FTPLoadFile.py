def FTPLoad(forecastID):
    from ftplib import FTP
    from io import StringIO   # Importing the StringIO module.
    
    def getFile(ftp, filename, outStr):
        print("in getFile")
        try:
            ftp.retrlines('RETR ' + filename, lambda s, w = outStr.write: w(s + '\n'))
        except:
            print("Error")

    ftp = FTP('tgftp.nws.noaa.gov')
    ftp.login()

    ftp.cwd("/data/forecasts/marine/great_lakes/ls") #changing working directory
    outStr = StringIO() # Use a string like a file.
    getFile(ftp,forecastID+".txt", outStr)  #copies the file to an IO Strings
    ftp.close()
    buff=outStr.getvalue()
    outStr.close()
    return(buff)

def main():
    forecastID="lsz266"
    buff=FTPLoad(forecastID)
    print(buff)

if __name__== "__main__" :
    main()
