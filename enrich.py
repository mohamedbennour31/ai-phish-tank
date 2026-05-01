import whois
from datetime import datetime, timezone

def check_domain_age(url):
    print(f"[*] Researching domain history for: {url}")
    try:
        # Extract domain name 
        domain = url.split("//")[-1].split("/")[0]
        w = whois.whois(domain)
        
        creation_date = w.creation_date
        
        # Handle cases where creation_date is a list
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
            
        if creation_date:
            # FIX 1 & 2: Use timezone.utc to match 'aware' datetimes 
            # and prevent the 'offset-naive' error.
            now = datetime.now(timezone.utc)
            
            # If the creation_date from whois doesn't have a timezone, add UTC
            if creation_date.tzinfo is None:
                creation_date = creation_date.replace(tzinfo=timezone.utc)
                
            age_days = (now - creation_date).days
            print(f"[+] Domain Age: {age_days} days")
            
            if age_days < 30:
                print("[!] ALERT: This domain is brand new! High risk.")
            else:
                print(f"[#] Domain is {age_days} days old.")
            return age_days
        else:
            print("[!] No creation date found in Whois record.")
            return None
            
    except Exception as e:
        print(f"[!] Could not retrieve Whois data: {e}")
        return None
