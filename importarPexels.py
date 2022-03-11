# load the RoboBrowser class from robobrowser
from robobrowser import RoboBrowser
 
# define base site
base = "https://www.pexels.com/"
 
# create browser object, def download_all_search_results(search_query, MAX_PAGE_INDEX = 30):
     
    browser.open(base)
     
    form = browser.get_form()
       
    form['s'] = search_query
     
    browser.submit_form(form)
     
    search_url = browser.url # new URL
     
    # create page index counter
    page_index = 1
 
    # define temporary holder for the photo links
    photos = [None]
 
    # set limit on page index
    # loop will break before MAX_PAGE_INDEX if there are less page results
    while photos != [] and page_index <= MAX_PAGE_INDEX:
         
        browser.open(search_url + "?page=" + str(page_index))
        
        links = browser.get_links()
        urls = [link.get("href") for link in links]
        urls = [url for url in urls if url is not None]
         
        # filter to what we need -- photos
        photos = [url for url in urls if '/photo/' in url]
         
        if photos == []:
            break
         
         
        for url in photos:
             
            full_url = "https://pexels.com" + url
         
            try:    
                browser.open(full_url)
             
                download_link = browser.get_link("Free Download")
                 
                browser.open(download_link.get("href"), stream = True)
                 
                file_name = url.split("/")[-2] + '.jpg'
                with open(file_name, "wb") as image_file:
                    image_file.write(browser.response.content)   
                     
            except Exception:
                 
                pass
 
        print("page index ==> " + str(page_index))
        page_index += 1
# which serves as an invisible web browser
browser = RoboBrowser()
 
# navigate to pexels.com
browser.open(base)
def download_all_search_results(search_query, MAX_PAGE_INDEX = 30):
     
    browser.open(base)
     
    form = browser.get_form()
       
    form['s'] = search_query
     
    browser.submit_form(form)
     
    search_url = browser.url # new URL
     
    # create page index counter
    page_index = 1
 
    # define temporary holder for the photo links
    photos = [None]
 
    # set limit on page index
    # loop will break before MAX_PAGE_INDEX if there are less page results
    while photos != [] and page_index <= MAX_PAGE_INDEX:
         
        browser.open(search_url + "?page=" + str(page_index))
        
        links = browser.get_links()
        urls = [link.get("href") for link in links]
        urls = [url for url in urls if url is not None]
         
        # filter to what we need -- photos
        photos = [url for url in urls if '/photo/' in url]
         
        if photos == []:
            break
         
         
        for url in photos:
             
            full_url = "https://pexels.com" + url
         
            try:    
                browser.open(full_url)
             
                download_link = browser.get_link("Free Download")
                 
                browser.open(download_link.get("href"), stream = True)
                 
                file_name = url.split("/")[-2] + '.jpg'
                with open(file_name, "wb") as image_file:
                    image_file.write(browser.response.content)   
                     
            except Exception:
                 
                pass
 
        print("page index ==> " + str(page_index))
        page_index += 1