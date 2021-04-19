from urllib import request

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1611100800&period2=1618876800&interval=1d&events=history&includeAdjustedClose=true'


def download_stock_data(csv_url):
    response = request.urlopen(csv_url) #Open a connection to the website and get the csv file
    csv = response.read() #Read the csv file
    csv_str = str(csv) #Convert the csv file to a string

    lines = csv_str.split("\\n") # Split a line if there is a new line towards the end
    dest_url = r'goog.csv' # Create a destination file

    fw = open(dest_url, 'w') # Open the file
    for line in lines: # Get each line from a set of lines
        fw.write(line + '\n') # Write those lines to the file goog.csv

    fw.close() # Close the file


download_stock_data(goog_url) # Call the function

