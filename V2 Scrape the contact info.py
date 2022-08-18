import csv
import bs4
import requests
contact_page_html=requests.get("https://watchguard.com/wgrd-about/contact")
contact_page_soup=bs4.BeautifulSoup(contact_page_html.text,"lxml")
contacts=contact_page_soup.select(".col-sm-9 .location")
# for i in contacts[:1]:
#     print(i.h3)
#     x=i.select("p")
#     for j in x:
#         for k in j.select("strong"):
            
#             for m in k.select("#text"):
#                 print(m)

new_csv_file=open("contact_info.csv", mode='w',newline="")
csv_writer=csv.writer(new_csv_file, delimiter=',')
csv_writer.writerow(['Name','Tel'])

# i = {<h3> title, <p> address, <p>tel sales tollfree}
for i in contacts:
    try:
        name=i.h3.get_text()
        # print(name)
        all_p_tags=i.select("p")
        # [<p>address</p>, or <p>tel, sales, toll free<p> ], some were having the address and some not 
        # for cur_p_tag in all_p_tags, instead of looping over all p's, take last p
        cur_p_tag_contain_tel=all_p_tags[-1]
        # print(cur_p_tag)
        data = []
        for j in cur_p_tag_contain_tel:
            text = list(j) # converted all the tag contents like, strong, etc and text without tag into the list 
            # print(text)
            data.append(text)
        
        for index, ele in enumerate(data,0):
            if ele==['Tel:'] or ele==['Sales:'] or ele==["Toll Free:"]:
                tel="".join(data[index+1])
                csv_writer.writerow([name,tel])
    except:
        pass
new_csv_file.close()
