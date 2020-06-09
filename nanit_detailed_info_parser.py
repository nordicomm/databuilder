
import json

# import HTMLParser library to parse the headings and paragraphs
from html.parser import HTMLParser

# TAGS to separate title from paragraph descriptions
SUBSTRING_TITLE_TAG = 'Titl3: '
SUBSTRING_DESCRIPTION_TAG = 'D3scr1ption: '

# class to help us separate start tags, end tags, data, and print outcomes
class MyHTMLParser(HTMLParser):

    c_tag = 'a' # tag is used to figure out whether data belongs to header tag/paragraph tag
    info = [] # varialble to store info.

    # class function called on receiving start of tag as argument
    def handle_starttag(self, tag, attrs):
        if tag in ['h2', 'p']:
            self.c_tag = tag

    # class function called on receiving end of tag as argument
    def handle_endtag(self, tag):
        if tag in ['h2', 'p']:
            self.c_tag = 'a'

    # class function called on receiving tag's data as argument
    def handle_data(self, data):
        if self.c_tag == 'h2': # separate h2 tag data
            self.info.append(SUBSTRING_TITLE_TAG + data)

        if self.c_tag == 'p': # separate paragraph tag data
            self.info.append(SUBSTRING_DESCRIPTION_TAG + data)


    def print_list(self): # print function
        for x in self.info:
            print(str(x) + "\n")

# end of class MyHTMLParser

def parser_function(page_soup, baby_age):

    # finds detailed data based on baby's age
    information = page_soup.findAll("div", {"class": "article-pure-content clearfix"})

    parser_info = MyHTMLParser()
    parser_info.feed(str(information[0]))

    output_list = [] # variable to input the data in JSON

    # baby age tag
    baby_age_tag = {}
    baby_age_tag["baby_age"] = str(baby_age)
    output_list.append(baby_age_tag)

    addtitle = {} # variable to have title and description together
    p_index = 0 # flag to indicate number of paragraph added in "addtitle" list

    substring_title = SUBSTRING_TITLE_TAG
    substring_desc = SUBSTRING_DESCRIPTION_TAG

    fh = open("baby_schedule_details.json", "a+") #open JSON file

    for x in parser_info.info:

        title = {} # loop's local variable

        if substring_title in x: # check if paragraph tag is included in the text
            if p_index > 0: # if previous title already have a paragraph
                title.update(addtitle) # concatinate the dictionaries
                output_list.append(title) # append in the output list
                p_index = 0 # initialize the paragraph index

            addtitle['title'] = x.replace(substring_title, '') # remove the substring tag

        if substring_desc in x: # check if paragraph tag is included in the text
            if p_index > 0: # if its a second paragraph under same title
                addtitle['description'] += x.replace(substring_desc, '')

            else: # if its first paragraph under same title
                addtitle['description'] = x.replace(substring_desc, '')
                p_index = p_index + 1

    output_list.append(addtitle) # append the final title and paragraph after loop

    # for x1 in output_list: # print the output list data
    #    print("\n\n output list" + str(x1))

    fh.write(json.dumps(output_list, indent=4, sort_keys=True)) # dump the list to JSON file

    fh.close()

# end of parser_function