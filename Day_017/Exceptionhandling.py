#packing and unpacking

def process_countries(names):
    nordic_countries = names[:5]
    es = names[-2]
    ru = names[-1]
    return nordic_countries, es, ru
    
    
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
nordic_countries, es, ru = process_countries(names)

print(nordic_countries)  
print(es)  
print(ru)  
