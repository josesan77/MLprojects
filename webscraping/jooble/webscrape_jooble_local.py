# -*- coding: utf-8 -*-
"""
Jooble Job Search webpage (downloaded local file) scraper for simplifying reading
 the results, with some added highlight for keywords / language.

1. Extract the required `<div>` tags that match the specific `class` value 
(`data-test-name="_jobCard" class="+n4WEb rHG1ci"`).
2. Within those tags, locate `<a>` anchors matching the provided class and extract 
the entire anchor tag, including the `href` attribute.
3. Extract the content of `<p class="b97WnG">` and `<div class="GEyos4">`.
4. Create a new HTML document and add each collected part of the data as separate 
paragraphs inside a new `<div class="content">`.
5. Save the generated file and open it in the browser.

The Python code using `requests` to fetch the page, `BeautifulSoup` to parse the HTML, 
and `html` to generate the output:

### Steps and Explanation:
0. **Save Jooble job search**: Make a search (after login) on Jooble with your keywords 
and settings and download the webpage. This way there is no need for authentication for 
software access to Jooble search data.
Implement OAuth2.0 authentication for Jooble, if you wish.
1. **Fetch the Website Content**: The `requests.get(url)` fetches the HTML content from 
the provided URL (local filepath).
2. **Parse HTML**: The `BeautifulSoup(response.content, 'html.parser')` parses the HTML 
so that we can search for specific elements.
3. **Find Job Cards**: We search for `<div>` tags that match both the `data-test-name` 
and the `class` attributes you provided.
4. **Extract Data**: For each `job_card`, we extract:
    - The `<a>` tag with the specific class and include the full anchor HTML tag.
    - The contents of the `<p class="b97WnG">` and `<div class="GEyos4">`.
5. **Save Output**: The gathered data is written to a new HTML file in the format you 
requested. The `<a>` tag is pasted as-is, while other text contents are added as paragraphs.
6. **Open the File**: After the web scraping is complete, the generated HTML file is 
opened in the default web browser.

### Dependencies:
- ```BeautifulSoup4```: Install it using `pip install beautifulsoup4`.
- ```langdetect```: language detection module (Machine learning, based on a Google ML),
    install using pip if missing
- ```re```, ```datetime``` are typically involved in Python basic module package

dependencies:
1)    try in python (IDE) shell/command line:
import langdetect
import BeautifulSoup
and if some fails install it
2) 
pip install langdetect
pip install BeautifulSoup

Note: Jooble may vary the tags, codes on the website, therefore if the software fails to run
due to error(s) in finding predefined html tags, then use F12 mode in your browser
and search key values which determines the required content to extract -> update the codes in this app.

Created on Wed Jan 15 17:40:16 2025
@author: Josesan77
"""

from bs4 import BeautifulSoup
import re
from langdetect import detect, detect_langs
from datetime import datetime
 
def load_local_file_content(url):
    # Open and read the file content
    with open(url, "r", encoding="utf-8") as file:
        response = file.read()
    return response
 
def filename_creator():
    """ Creates a filename including current time, to know when was the job list processed.
    only filename is generated without FOlder name, hence the html file will be generated in this app's folder."""
    moment = datetime.now()
    moment_string = moment.strftime('%Y%m%d_%H%M') # datetime. %S
    filename = 'webscraped_jooble_at' + moment_string +'.html'  
    return filename
   
# Function to perform web scraping
def scrape_website(url, search_term, searched_langcode):
    """ Open local file, scrape (get) content,  modify and write to a new HTML file """
    
    response = load_local_file_content(url)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response, 'html.parser')

    # Open a new HTML file to store/write the results (for later reading)
    jooble_html_name = filename_creator() #output filename creator
    with open(jooble_html_name, "w", encoding="utf-8") as f:
        # Start the new HTML file structure
        f.write("<html><head><title>Webscraped Content</title></head><body>\n")
        f.write('<div class="content">\n')

        # Find all relevant <div> elements with the specified class
        job_cards = soup.find_all('div', {'class': '+n4WEb rHG1ci', 'data-test-name': '_jobCard'})

        for job_card in job_cards:
            # Extract the <a> (link) tag matching the given class, if it exists
            # the link points to the detailed job position description webpage
            anchor = job_card.find('a', {'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 wtCvxI'})
            pretext = ''
            if anchor is not None and re.search(search_term, anchor.text.lower()):
                pretext = '*** ' #highlight          

            # Extract short description of posted position: 
            # <p> content with class 'b97WnG' and <div> content with class 'GEyos4'
            p_content = job_card.find('p', {'class': 'b97WnG'})
            div_content = job_card.find('div', {'class': 'GEyos4'}) 
            
            #detect language
            div_content_text = div_content.text.replace('\n', '').replace('\xa0', '') 
            language = detect(div_content_text)
                        
            # Languages with probabilities: [de:0.9999970984386382]
            #lang2 = detect_langs(div_content_text)
            # print(f"Languages with probabilities: {lang2}")
            
            stylemod = '' #background color changing for highlighting
            if language == searched_langcode:
                stylemod = ' style="background-color:#779977"' # set your favorit bg color
                div_content_text #debug
                
            if anchor:
                # Add the entire anchor tag with some modifications
                f.write(f'<div{stylemod}>{pretext}{anchor}<br />\n') #add textual/bg-color highlights                  
            if p_content:
                f.write(f"{p_content.get_text()}<br />\n")
            if div_content:
                f.write(f"{div_content.get_text()}</div>\n")

        # Close the content div and the rest of the HTML file
        f.write('</div></body></html>')

    print('Web scraping complete. Output saved to ' + jooble_html_name)

    # Open the newly created HTML file in the default web browser. Ready! -> Read!
    import webbrowser
    webbrowser.open(jooble_html_name)

# ---------------------- APP STARTS HERE ---------------------------------
# Run the function to scrape the website and create the new HTML file
#url ='https://at.jooble.org/SearchResult?date=3&p=2&ukw=junior%20data%20analyst' #example web search
url = '[FILEPATH.html]' # overwrite with the saved Jooble search file's path (or use some python FileBrowser to browse for file)

search_term = 'data' #set your preferred keyword for '***' highlighting
searched_langcode = 'en' #set your preferred language code (one like: en, de, es...) for background color highlighting
scrape_website(url, search_term, searched_langcode)


