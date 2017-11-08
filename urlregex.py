import re
def domain_name(url):
    regex = "http[s]?://(www)?([a-z]|[.-])*.([a-z])*"
    



# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

a = "http://github.com/carbonfive/raygun"
b = "http://www.zombie-bites.com"
c = "https://www.cnet.com"