city_urls_petrol = {'gurgaon':
    'http://www.mypetrolprice.com/40/Petrol-price-in-Gurgaon',
'hyderabad':
    'http://www.mypetrolprice.com/8/Petrol-price-in-Hyderabad',
'port blair':
    'http://www.mypetrolprice.com/29/Petrol-price-in-Port%20Blair',
'agartala':
    'http://www.mypetrolprice.com/9/Petrol-price-in-Agartala',
'panjim':
    'http://www.mypetrolprice.com/26/Petrol-price-in-Panjim',
'guwahati':
    'http://www.mypetrolprice.com/18/Petrol-price-in-Guwahati',
'gandhinagar':
    'http://www.mypetrolprice.com/36/Petrol-price-in-Gandhinagar',
'pondicherry':
    'http://www.mypetrolprice.com/28/Petrol-price-in-Pondicherry',
'ranchi':
    'http://www.mypetrolprice.com/31/Petrol-price-in-Ranchi',
'mumbai':
    'http://www.mypetrolprice.com/3/Petrol-price-in-Mumbai',
'mysore':
    'http://www.mypetrolprice.com/49/Petrol-price-in-Mysore',
'bhubhaneswar':
    'http://www.mypetrolprice.com/14/Petrol-price-in-Bhubhaneswar',
'thane':
    'http://www.mypetrolprice.com/41/Petrol-price-in-Thane',
'vadodara':
    'http://www.mypetrolprice.com/53/Petrol-price-in-Vadodara',
'raipur':
    'http://www.mypetrolprice.com/30/Petrol-price-in-Raipur',
'ambala':
    'http://www.mypetrolprice.com/12/Petrol-price-in-Ambala',
'bengaluru':
    'http://www.mypetrolprice.com/6/Petrol-price-in-Bengaluru',
'patna':
    'http://www.mypetrolprice.com/27/Petrol-price-in-Patna',
'itanagar':
    'http://www.mypetrolprice.com/20/Petrol-price-in-Itanagar',
'kolkata':
    'http://www.mypetrolprice.com/4/Petrol-price-in-Kolkata',
'jalandhar':
    'http://www.mypetrolprice.com/23/Petrol-price-in-Jalandhar',
'bhopal':
    'http://www.mypetrolprice.com/13/Petrol-price-in-Bhopal',
'chandigarh':
    'http://www.mypetrolprice.com/15/Petrol-price-in-Chandigarh',
'gangtok':
    'http://www.mypetrolprice.com/17/Petrol-price-in-Gangtok',
'chennai':
    'http://www.mypetrolprice.com/5/Petrol-price-in-Chennai',
'rajkot':
    'http://www.mypetrolprice.com/52/Petrol-price-in-Rajkot',
'noida':
    'http://www.mypetrolprice.com/37/Petrol-price-in-Noida',
'jammu':
    'http://www.mypetrolprice.com/22/Petrol-price-in-Jammu',
'shimla':
    'http://www.mypetrolprice.com/33/Petrol-price-in-Shimla',
'delhi':
    'http://www.mypetrolprice.com/2/Petrol-price-in-Delhi',
'dehradun':
    'http://www.mypetrolprice.com/16/Petrol-price-in-Dehradun',
'shillong':
    'http://www.mypetrolprice.com/32/Petrol-price-in-Shillong',
'trivandrum':
    'http://www.mypetrolprice.com/35/Petrol-price-in-Trivandrum',
'srinagar':
    'http://www.mypetrolprice.com/34/Petrol-price-in-Srinagar',
'ahmedabad':
    'http://www.mypetrolprice.com/10/Petrol-price-in-Ahmedabad',
'pune':
    'http://www.mypetrolprice.com/7/Petrol-price-in-Pune',
'lucknow':
    'http://www.mypetrolprice.com/25/Petrol-price-in-Lucknow',
'navi mumbai':
    'http://www.mypetrolprice.com/42/Petrol-price-in-Navi%20Mumbai',
'kohima':
    'http://www.mypetrolprice.com/24/Petrol-price-in-Kohima',
'jaipur':
    'http://www.mypetrolprice.com/21/Petrol-price-in-Jaipur',
'gwalior':
    'http://www.mypetrolprice.com/48/Petrol-price-in-Gwalior',
'surat':
    'http://www.mypetrolprice.com/51/Petrol-price-in-Surat',
'aizwal':
    'http://www.mypetrolprice.com/11/Petrol-price-in-Aizwal',
'imphal':
    'http://www.mypetrolprice.com/19/Petrol-price-in-Imphal',
'kolhapur':
    'http://www.mypetrolprice.com/78/Petrol-price-in-Kolhapur',
}

def petrol_urls():
    return city_urls_petrol

def petrol_url(city_name):
    return city_urls_petrol[city_name.lower()]