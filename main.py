import pyshorteners
long_url = input("Enter long URL: ")
tiny= pyshorteners.Shortener()
short_url= tiny.tinyurl.short(long_url)   
print("shortened url:"+short_url) 
