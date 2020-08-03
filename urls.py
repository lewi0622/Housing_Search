# add or remove from the list as necessary. create a new dict in the list using the {sitename: url} convention

urls = [
    {
        'zillow': r'https://www.zillow.com/homes/for_rent/1-_beds/1.0-_baths/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-93.50802635404175%2C%22east%22%3A-93.10633873197143%2C%22south%22%3A44.868132495735146%2C%22north%22%3A45.062947488470165%7D%2C%22mapZoom%22%3A12%2C%22customRegionId%22%3A%222df575f09eX1-CR14087aax9bs72_uh1re%22%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A282815%2C%22max%22%3A450470%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22sqft%22%3A%7B%22min%22%3A700%7D%2C%22doz%22%3A%7B%22value%22%3A%221%22%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A1000%2C%22max%22%3A1700%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22cat%22%3A%7B%22value%22%3Atrue%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22sdog%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    },
    {
        'craigslist': r'https://minneapolis.craigslist.org/search/apa?sort=date&hasPic=1&postedToday=1&bundleDuplicates=1&search_distance=4&postal=55402&min_price=1000&max_price=1700&minSqft=600&maxSqft=1400&availabilityMode=0&pets_cat=1&pets_dog=1&no_smoking=1&sale_date=all+dates'
    },
    {
        'apartments': r'https://www.apartments.com/houses/minneapolis-mn/min-1-bedrooms-1-bathrooms-1000-to-1700-pet-friendly/?bb=0gtmxlgn9K-t1tirG&so=8'
    },
    {
        'trulia': r'https://www.trulia.com/for_rent/Minneapolis,MN/44.92109,44.96865,-93.32918,-93.24888_xy/1p_beds/1p_baths/1000-1700_price/600-1300_sqft/APARTMENT,APARTMENT_COMMUNITY,APARTMENT%7CCONDO%7CTOWNHOUSE,CONDO,COOP,LOFT,SINGLE-FAMILY_HOME,TIC_type/date;d_sort/lg_dogs,sm_dogs_pets/14_zm/'
    },
    {
        'trulia': r'https://www.trulia.com/for_rent/Minneapolis,MN/44.9861,45.03361,-93.27425,-93.19396_xy/1p_beds/1p_baths/1000-1700_price/600-1300_sqft/APARTMENT,APARTMENT_COMMUNITY,APARTMENT%7CCONDO%7CTOWNHOUSE,CONDO,COOP,LOFT,SINGLE-FAMILY_HOME,TIC_type/date;d_sort/lg_dogs,sm_dogs_pets/14_zm/'
    }
]
