#! /usr/bin/env python
#  -*- coding: utf-8 -*-


import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font
import os
import sys
import platform
import datetime
from PIL import Image, ImageTk
from screeninfo import get_monitors

import articlesLookup
import articlesLookup_support
 
""".....Author : Halvard Tislavoll, 2024
released under : MIT License
......filename : toolkit.py
.GUI File Name : textboxLookup.py
.......Purpose : give textboxLookup access to my toolkit functions"""


# ######################################################################
#
#   Toplevel Place Support Section
#
# ======================================================================


def center_toplevel(window, wid, hei, monitors, screen_number):
    # Place on screen center
    # from screeninfo import get_monitors
    # monitors = get_monitors()
    if 1 <= screen_number <= len(monitors):
        screen = monitors[screen_number - 1]
        window_width = wid
        window_height = hei
        x = screen.x + (screen.width - window_width) // 2
        y = screen.y + (screen.height - window_height) // 2
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")


def place_toplevel(window, _w1):
    # Place Toplevel form on screen center
    # from screeninfo import get_monitors
    monitors = get_monitors()
    if len(monitors) == 1:
        # print("There is only one monitor.")
        screen = 1
    else:
        # I want to put my app at screen 2 if it is present
        # print(f"There are {len(monitors)} monitors.")
        screen = 2
    # from GUI: top.geometry("930x576+602+158")
    wid=930
    hei=576
    center_toplevel(window, wid, hei, monitors, screen)
    ### write screen info to labels=====================================
    _w1.LblName.configure(foreground="#210000", text=f"  Name: {monitors[screen-1].name}")
    _w1.LblResolution.configure(foreground="#210000", text=f"  Resolution: {monitors[screen-1].width}x{monitors[screen-1].height}")
    _w1.LblPosition.configure(foreground="#210000", text=f"  Position: +{monitors[screen-1].x}+{monitors[screen-1].y}")


# ######################################################################
#
#   System Info Support Section
#
# ======================================================================


def give_sysem_info(root, tk, _w1):
    '''Write information about this Application'''
    # import sys
    # import datetime
    # remember to update myFile !!!
    # import os
    # import platform
    # import datetime
    import shared as sh
    # get system info
    osVersion = platform.system()
    release = platform.release()
    py_f_name =    os.path.basename(sys.argv[0])
    current_path = os.path.abspath(__file__)
    patchlevel = root.tk.call("info", "patchlevel")
    tkVer = tk.TkVersion
    tclVer = tk.TclVersion

    py_version =   platform.python_version()
    author =       'Halvard Tislavoll'
    current_time = datetime.datetime.now()
    sh.current_time_1 = f'{current_time.hour:02}:{current_time.minute:02}:{current_time.second}'
    # read this file and get page version on line 4
    myFile="./articlesLookup_support.py"
    signal, all_text=read_text_file_lines(myFile)
    if signal:
        txt_lst=all_text.split('\n')
        sh.page_version=txt_lst[3][-4:]   # list out last of a function line, the "8.0G" from "... PAGE version 8.0G"
        # It is in line 4 but count from 0 it is 3
    else:
        print('Trouble, no _support file is found. Have you give the right name?')
    # print system info
    print('\nSystem and Program Information:')
    print('')
    print(f'             Current  {current_time.year}-{current_time.month}-{current_time.day}')
    print(f'          Start time  {sh.current_time_1}')
    print(f'        Program name  "{py_f_name}"')
    print(f'      System running  {osVersion} {release}')
    print(f'Running under Python  {py_version}')
    print(f'     Tkinter Version {sh.page_version}')
    print(f'         Tcl Version  {tclVer}')
    print(f'          Tk Version  {tkVer}')
    print(f'     Tcl Patch Level  {patchlevel}')
    print(f'        Current path  {current_path}\n')
    print('‒'*sh.decoration)
    print('''
MIT License   : https://opensource.org/licenses/MIT
Copyright (c) [2024] [halvard.tislavoll@haugnett.no]
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n''')
    print('‒'*sh.decoration, '\n')
    _w1.lblStatus.configure(text='''READY''')


def tot_time(current_time):
    # import datetime
    import shared as sh
    current_time_2 = f'{current_time.hour}:{current_time.minute}:{current_time.second}'
    h1,m1,s1 = sh.current_time_1.split(':')
    h2,m2,s2 = current_time_2.split(':')
    tot_h=int(h2)-int(h1)
    tot_m=int(m2)-int(m1)
    tot_s=int(s2)-int(s1)
    if tot_s < 0:
        remainder=tot_s
        tot_m-=1
        tot_s=60+remainder
    if tot_m < 0:
        remainder=tot_m
        tot_h-=1
        tot_m=60+remainder
    tot_time=f'{tot_h}:{tot_m}:{tot_s}'
    return tot_time 


# ######################################################################
#
#   Splash Screen Support Section
#
# ======================================================================  

  
def set_splash_screen(_w1):
    import shared as sh
    # Load the fac simile images for splshscreen
    sh.Fac_simile_image = Image.open("assets/graphic/Fac_simile.png")

    # Resize images if necessary
    sh.Fac_simile_image = ImageTk.PhotoImage(sh.Fac_simile_image.resize((597, 460)))

    # set the image on label
    _w1.TLblFac_simile.configure(image=sh.Fac_simile_image)
    
    # make a intro text
    txt="""I have subscribed to this
service from «Pycoder's 
weekly» for a while. Here I 
have found many interesting 
and inspiring Python-related 
articles. I see this service
as a source of knowledge.

So far I have read through the
selection on their site and 
selected which articles I find 
relevant to me.

Now I got an idea for an
application that can help 
retrieve the pages in a new 
way. Hope it can be of help 
to someone else as well.

           Halvard Tislavoll, 2024
    """

    # put an introtext on the intro label for this application
    _w1.TLblIntro.configure(text=txt)  


# ######################################################################
#
#   Support Section
#
# ======================================================================


def init_widgets(_w1):
    import shared as sh
    print(f"A temporary module «{sh.sharedfilename}» to share info between modules, is established!\n")   # a variable test
    print('‒'*sh.decoration)
    # set bind method to widgets
    _w1.TEntry1.bind("<Return>",  lambda e: _w1.TEntry2.focus_set()) and \
    _w1.TEntry1.bind("<Key-Tab>", lambda e: _w1.TEntry2.tk_focusNext().focus())
    _w1.TEntry2.bind("<Return>",  lambda e: articlesLookup_support.on_TBtnGo1())
    # correct an type error
    _w1.TBtnListAdd.configure(text='''Add an Issue''')
    # trick to get right tab order by G.D.Walter
    widgets=[_w1.TEntry1, _w1.TEntry2]
    for wl in widgets:
        wl.lift()
    ''' While I use the .lift() method to hide the frame widget, 
        I use the place() method to move out of sight, 
        to hide widgets on the frame '''
    # set widget place
    _w1.TFrameMenu.lower()
    _w1.ScrolledlistboxUrl.place(x=5000)   # place(x=36, y=90, height=168, width=428)
    # animation support
    set_filenames()
    sh._image1 = tk.PhotoImage(file=sh.h)   # set label image for the hambuger menu
    _w1.TLblHamburger.configure(image= sh._image1)
    sh.hamburgermenu=True   # set up a hamburger menu frame
    # set warning label text
    set_warning(_w1)
    # Folder path where files are located
    sh.folder_path = "./assets"
    # Create a StringVar to store the result
    sh.result = tk.StringVar()
    # set height of button and the gap between buttons
    sh.buttonY=20
    _w1.Scrolledwindow1_f.configure(background="#919191")

    sh.txtbox=_w1.Scrolledtext1
    sh.txtbox.configure(background="#919191", relief="flat")

    '''
    txt="""⇖ 
    There is a hamburger menu here.
It will show you the options: 
"Home" which is this page, 
"Add an Issue" there you can register
               new issues from 
               Pycoder's weekly.
"Edit Items" is a page to edit urls.
"Preferences" is a settings page.
    
    All Weekly Issues registered in
.json format in the archive will be
listed here   ⇒

    Select a button and all articles
from selected Issue will be listed on
the next page so you can choose which
article you will read in your browser."""
    _w1.TLblAboutWeeklyList.configure(text=txt)
    '''

def set_lower(_w1):
    # set widget lower on stack
    _w1.frmStartupSplashScreen.lower()
    _w1.TFrameMenu.lower()
    _w1.frmArticles.lower()
    _w1.frmPreferences.lower()
    _w1.TfrmAbout.lower()
    _w1.TfrmHelp.lower()
    _w1.frmMoveBetweenLists.lower()
    _w1.frmAddIssues.lower()
    _w1.frmStartupSplashScreen.lower()


def set_warning(_w1):
    txt="""Do not tuch mouse or keyboard when
I operate on your webbrowser to scrape, 
and open and closing pages in tabs.

Note: this will possibly take a few minutes,
        please wait!
    """
    _w1.TLbl_warning.configure(text=txt)
    

def on_time_update():
    # ======================================================
    # Callback function for the Time display
    # ======================================================
    import shared as sh
    used_time=""
    current_time = datetime.datetime.now()
    used_time = tot_time(current_time)
    #nowstring = f"{datetime.datetime.now():%X}"
    sh._w.StatusTime.set(used_time)   # StatusTime   nowstring
    sh.timer_id = sh._t.after(500, on_time_update)


def is_valid_date(date_string):
    from datetime import datetime
    try:
        # Specify the format that matches "Oct. 29, 2024"
        datetime.strptime(date_string, "%b. %d, %Y")
        return True
    except ValueError:
        return False


def show_message(message):
    from tkinter import messagebox
    messagebox.showinfo("Information", message)   # "This is an informational message."
 

# ######################################################################
#
#   Textbox Support Section
#
# ======================================================================


def populate_help():
    from tkinter import font
    from PIL import Image,ImageTk
    import shared as sh
    global img1, img2, img3
    # It is a good habit to clear the textbox before new text is inserted
    sh.txtbox.delete('1.0', 'end')   
    # Build a paragraph heading
    txt="""~ hamburger menu"""
    transmit_heading_to_txtbox(txt)
    # Build a body text
    txt="""If you toggle the menu button with tree bars, it will change icon on button to an X so you can
hide the menu with the same button, and when it is open you will see these options:"""
    transmit_bodytxt_to_txtbox(txt)
    # Create a picture in the text
    img1 = tk.PhotoImage(file = "assets/graphic/Hamburgermenu_open.png")
    transmit_img_to_txtbox(img1)
    # Build a image text to the picture
    txt="""


 "Home" is the page where you can pick an Issue #, 

 "Add an Issue" where you can register an new issue from Pycoder's weekly.

 "Edit Items" where you can edit heading or url on an Issue. 

 "Preferences" A settings page for this Application.
    """
    transmit_imgtxt_to_txtbox(txt, 'Right')
    # Build a paragraph heading number two
    txt="""~ retrieve weekly issue"""
    transmit_heading_to_txtbox(txt)
    # Build a body text number two
    txt="""All Weekly Issues registered in .json format in the archive will be listed at "Home" page.
    """
    transmit_bodytxt_to_txtbox(txt)
    # Create a picture number two in the text
    img2 = tk.PhotoImage(file = "assets/graphic/buttonList.png")
    transmit_img_to_txtbox(img2)
    # Build a image text to the picture number two
    txt="""
    Select a button and all articles from selected Issue will be
    listed on the next page so you can choose which article you will
    read in your browser.
    """
    transmit_imgtxt_to_txtbox(txt, 'Right')
    sh.txtbox.insert(tk.END, '\n')   # put a empty line to make space in text


    # Build a paragraph heading number tree
    txt="""~ Retrieve an article from an Issue"""
    transmit_heading_to_txtbox(txt)
    # Build a body text number tree
    txt="""All articles from selected Issue is listed here:.
    """
    transmit_bodytxt_to_txtbox(txt)
    # Create a picture number tree in the text
    img3 = tk.PhotoImage(file = "assets/graphic/articleList.png")
    transmit_img_to_txtbox(img3)
    sh.txtbox.insert(tk.END, '\n')   # put a empty line to make space in text
    # Build a image text to the picture number tree
    txt="""
 Here are all the articles and URLs taken from the selected issue. You can choose which
 articles you want to read in your browser. You can even choose more than one at a time.
    """
    transmit_imgtxt_to_txtbox(txt, 'Below')
    

def transmit_heading_to_txtbox(msg):
    import shared as sh
    # Define a custom font for the heading
    heading_font = font.Font(family="TkFixedFont", size=20, weight="bold")
    # Configure the tag to use the custom font
    sh.txtbox.tag_configure("heading", font=heading_font)   # , justify='center'
    # Insert text with the 'heading' tag
    #sh.txtbox.insert(tk.END, '\n\t')
    sh.txtbox.insert(tk.END, '\t\t'+msg+'\n', "heading")


def transmit_bodytxt_to_txtbox(msg):
    import shared as sh
    sh.txtbox.configure(font='TkFixedFont 14')
    sh.txtbox.insert(tk.END, msg+'\n')


def transmit_img_to_txtbox(img):
    import shared as sh
    sh.txtbox.image_create(tk.END, image = img) # Example 1


def transmit_imgtxt_to_txtbox(msg, direction):
    import shared as sh
    if direction == 'Right':
        sh.txtbox.window_create(tk.END, window = ttk.Label(sh.txtbox, 
                                                            text = msg,
                                                            justify='left', 
                                                            font='TkFixedFont 13'
                                                          )
                                )
        sh.txtbox.insert(tk.END, '\n')
    else:
        transmit_bodytxt_to_txtbox(msg)
 
 
# ######################################################################
#
#   Scrolledwindow Support Section
#
# ======================================================================


def display_all_issues(_w1):
    '''Build a Scrolledwindow with scrollbars and buttons'''
    # import sys
    import shared as sh
    global b, button, button_data, key_list, current   # globals data to share 
    # make a instance of the inner frame of the Scrolledwindow
    inner_frame = _w1.Scrolledwindow1_f
    # make a dict to hold the new buttons
    b = {}
    button_data = create_buttons_from_files(_w1, sh.folder_path)
    # Build buttons from button_data dict for the the inner frame widget
    key_list=list(button_data.keys())
    button_data_number = len(button_data)  # number of units in dict
    for cntr in range(button_data_number):
        current=cntr
        row, col = divmod(cntr, 1)   # set: row = 0..18 col = 0
        b[cntr] = ttk.Button(
            inner_frame,   # parent widget
            width=18,      # letter width depends on the selected font
            text=button_data[key_list[cntr]][:-5],   # exclude .json            
        )   # anchor="w",    # justify left   activebackground="lawngreen",   # color on actual button, pointer on
        # place button on the grid in inner_frame widget
        b[cntr].grid(row=cntr * row, column=col, padx=5, pady=4)
        # bind an event to this button
        b[cntr].bind("<Button-1>", lambda e, w=_w1, cnt=cntr: on_btnClick(e, w, cnt))
    # let button show up in the inner_frame     
    b[0].wait_visibility()   
    # to show up the scrollbars
    bbox = inner_frame.bbox()
    _w1.Scrolledwindow1.configure(scrollregion=bbox)
    _w1.Scrolledwindow1.place(x=574)
    _w1.TLabel10.place(x=2000)   # x=563


def on_btnClick(event, _w1, current):
    '''Function to set the result variable with the filename'''
    
    import shared as sh
    global button_data, key_list
    text=button_data[key_list[current]]
    sh.result.set(text[:-5])  # Update the variable with the button's filename
    sh.pycoder_date = text[:-5]
    # set heading label
    h = text[:-5]
    i,d=h.split('_')
    heading = f"# {i} articles {chr(8212)} {d}:"
    _w1.TLabel3.configure(text=heading)
    _w1.lblStatus.configure(text='''Pick the Article you want to open in your web browser''')
    populate_data()
    # init a treeview widget with current data
    init_treeview(_w1)
    _w1.frmArticles.lift()


def create_buttons_from_files(_w1, folder_path):
    '''Function to create buttons for each file in a specified folder'''
    # import os
    import shared as sh
    button_data={}
    # Get a list of all files in the folder
    files = sorted(list_files(), reverse=True)
    # Create a button for each file
    num=1
    for filename in files:
        if os.path.isfile(os.path.join(folder_path, filename)):  # Ensure it's a file, not a directory
            # Create a button and associate it with a command to update the result variable
            key=str(num)
            button_data[key] = filename
            num+=num
    return button_data


def list_files():
    import shared as sh
    # Funksjon for å lese oppdatert liste over filer
    f = os.listdir(sh.folder_path)
    files=[]
    for item in f:
        if item.endswith('.json'):
            files.append(item)
    return files


def display_issues():
    import webbrowser
    # set url to pycoders.com/issues
    url = f"https://pycoders.com/issues"
    # open a html-file in browser
    webbrowser.open(url, new=1)   # by me   (new=0 in the same browser, new=1 in a new browser, new=3 in new tab)


def handle_entry(_w1):
    import shared as sh
    import concurrent.futures
    import urllib.request
    import webbrowser
    wich1=int(_w1.TEntry1.get())
    wich2=str(_w1.TEntry2.get())

    # test whether the inbox contains a valid value 
    if (wich1 > 0) and (wich1 < 656):
        if is_valid_date(wich2):
            
            _w1.TLbl_warning.place(x=111)   # 5000
            
            # initiate an empty list to hold urls
            sh.URLS=[]
            # add issue number to url
            url = f"https://pycoders.com/issues/{str(wich1)}"
            # scrap all urls from pycoder's
            links = scrape_links(url)
            for link in links:
                l = link[:6]
                if l == "https:":
                    if not link in sh.URLS:  
                        sh.URLS.append(link)
            # use concurrent.futures to open actual web pages quickly
            #import concurrent.futures
            #import urllib.request
            #import webbrowser
            try:
                print('\nPlease wait while I load the web page ...\n')

                # We can use a with statement to ensure threads are cleaned up promptly
                with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                    # Start the load operations and mark each future with its URL
                    future_to_url = {executor.submit(load_url, url, 60): url for url in sh.URLS}
                    for future in concurrent.futures.as_completed(future_to_url):
                        url = future_to_url[future]
                        
                        # open a html-file in browser
                        # webbrowser.open(url, new=2)   # by me   (new=0 in the same browser, new=1 in a new browser, new=3 in new tab)
                        webbrowser.open_new_tab(url)    # by me
                        try:
                            data = future.result()
                        except Exception as exc:
                            print('%r generated an exception: %s' % (url, exc))
                        else:
                            print('%r page is %d bytes' % (url, len(data)))
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc)) 

            length = len(sh.URLS)
            #print('-----> ',URLS)
            #print('len--> ',len(URLS))   # len-->  38   
            NEW_URLS=[]
            for i in range(length):
                # Usage example
                url = get_active_firefox_url()
                print("Active tab URL:", url)   # Active tab URL: https://twitter.com/pycoders
                NEW_URLS.append(url)
                
                # Usage example
                close_active_firefox_tab()
                print("Active tab closed.")
            sh.myURLset=set(NEW_URLS)   # no dublicate
            # hide warning label
            _w1.TLbl_warning.place(x=5000)   # 111
            # display the listbox for urls
            #_w1.ScrolledlistboxUrl.place(x=36)   # place(x=5000
            var1 = tk.StringVar()
            var1.set(list(sh.myURLset))
            # populate listbox
            #_w1.ScrolledlistboxUrl.configure(listvariable=var1)
            # scrape header from this urls
            for myurl in sh.myURLset:
                # print(myurl)
                header_text = get_header_text(myurl)
                print("Header text:", header_text)       
            mydict={}
            num=37
            try:
                # read header tags
                for url in sh.myURLset:
                    #url = "https://realpython.com/podcasts/rpp/224/"  # Replace with the URL of your choice
                    header_text = get_header_text(url)
                    print('header_text :', header_text)
                    if header_text != None:
                        if header_text != 'No <h1> tag found.':
                            mydict.setdefault(f'{num}', [f'{header_text}', f'{url}'])
                            #print(num, '  ', header_text)
                            num+=1
                # sh.data.update(mydict)
                #for key, value in mydict.items():
                #    print(repr(key), ':', repr(value))
            except:
                pass
        else:
            message="Date format is invalid!"
            show_message(message)
    else:
        message="This is not a legal issue number"
        show_message(message)
    var2 = tk.StringVar()
    # display the listbox for urls
    _w1.ScrolledlistboxUrl.place(x=36, width=860)   # place(x=36, y=90, height=168, width=428)
    aList=[]
    num=1
    for key, value in mydict.items():
        aList.append(f"[{num:>3}.) {wich2} - {value[0]}  -  {value[1]}],")
        num+=1
    #print(aList)
    var2.set(aList)
    _w1.ScrolledlistboxUrl.configure(listvariable=var2)

    # save file to json
    num=1
    dump_dict={}
    # format: '1': ["Asyncio gather() In The Background", "https://superfastpython.com/asyncio-gather-background/"],
    for item in aList:
        # print(item[7:])
        dump_dict[f'{num}'] = item[7:]
        num+=1
    json_file_name=f"assets/{wich1}_{wich2}.json"
    assets_folder_path = "./assets"
    # check if file exist
    import os
    j_files = os.listdir(assets_folder_path)
    if not json_file_name in j_files: 
        import json
        # Store it in a JSON file
        with open(json_file_name, "w") as f:
            json.dump(dump_dict, f)


# ######################################################################
#
#   Scrolledtreeview Support Section
#
# ======================================================================

def init_treeview(_w1):
    import shared as sh
    
    # Load the images for unchecked and checked boxes
    sh.unchecked_image = Image.open("assets/graphic/unchecked.png")
    sh.checked_image = Image.open("assets/graphic/checked.png")

    # Resize images if necessary
    sh.unchecked_image = ImageTk.PhotoImage(sh.unchecked_image.resize((25, 25)))
    sh.checked_image = ImageTk.PhotoImage(sh.checked_image.resize((25, 25)))

    # Dictionary to store checked/unchecked state for each item
    sh.checkbox_states = {key: False for key in sh.data.keys()}
        
    # Define the custom font
    custom_font = font.Font(family="Times new roman", size=13)
    
    # make a tree object
    sh.tree = _w1.Scrolledtreeview1   # using a widget from GUI file

    # Create a style and set the font for the Treeview
    style = ttk.Style()
    style.configure("Custom.Treeview", font=custom_font)  # Apply custom font to Treeview rows
    style.configure("Custom.Treeview.Heading", font=custom_font)  # Apply custom font to headers

    # Create ScrolledTreeview widget with the custom style
    sh.tree.configure(style="Custom.Treeview")

    # init treeview column, heading and populate it
    create_treeview_columns()
    create_treeview_heading()
    populate_treeview()

    # Bind mouse click event to toggle checkbox
    sh.tree.bind("<Button-1>", toggle_checkbox)


def create_treeview_columns():
    import shared as sh
    # Define the columns in the Treeview
    sh.tree["columns"] = ("ID", "Description")
    sh.tree.column("#0", width=45, stretch=tk.NO)  # Adjust as needed
    sh.tree.column("ID", anchor=tk.N, width=1)
    sh.tree.column("Description", anchor=tk.W, width=800)    


def create_treeview_heading():
    import shared as sh
    # Create column headers
    sh.tree.heading("#0", text="Chk", anchor=tk.CENTER)
    sh.tree.heading("ID", text="ID", anchor=tk.CENTER)
    sh.tree.heading("Description", text="Description", anchor=tk.W)


def populate_treeview():
    import shared as sh
    
        # Clear all rows in the Treeview
    for item in sh.tree.get_children():
        sh.tree.delete(item)
        
    # Insert dictionary data into the Treeview
    for key, value in sh.data.items():
        #print('value', value)
        sh.tree.insert(parent="", 
                    index="end", 
                    iid=key, 
                    values=(key, value), 
                    image=sh.unchecked_image
                    )


def toggle_checkbox(event):
    import shared as sh
    '''Function to toggle checkbox state'''
    # Identify the clicked item
    item_id = sh.tree.identify_row(event.y)
    than_pop=False
    if item_id:  # If an item was clicked
        # Toggle state
        if item_id in sh.actual_list:
            than_pop=True
        if than_pop:
            sh.actual_list.remove(item_id)
        else:        
            sh.actual_list.append(item_id)
        print('---> ', sh.actual_list)
            
        sh.checkbox_states[item_id] = not sh.checkbox_states[item_id]
        # Update checkbox image based on state
        new_image = sh.checked_image if sh.checkbox_states[item_id] else sh.unchecked_image
        sh.tree.item(item_id, image=new_image)

    d,h,a_url = sh.data[item_id].split(' - ')
    sh.url_current= a_url[1:-2]

    if not sh.url_current in sh.URLS:
        sh.URLS.append(sh.url_current)
    else:
        sh.URLS.remove(sh.url_current)


def toggle_all_checkboxes(state):
    import shared as sh
    '''Function to toggle all checkboxes in the Treeview'''
    for item_id in sh.tree.get_children():  # Get all items in the Treeview

        # Toggle the state in the dictionary
        sh.checkbox_states[item_id] = not sh.checkbox_states[item_id]
        
        # Set the image based on the new state
        # new_image = checked_image if checkbox_states[item_id] else unchecked_image
        
        # Set the image based on the specified state
        new_image = sh.unchecked_image
        sh.tree.item(item_id, image=new_image)
    sh.actual_list=[]
    sh.URLS=[]


def update_tree():
    print('my_filetree_explorer_support.update_tree')
    # sys.stdout.flush()
    import shared as sh
    # Insert dictionary data into the Treeview
    for key, value in sh.data.items():
        #print('value', value)
        sh.tree.insert(parent="", 
                    index=0, 
                    iid=key, 
                    values=(key, value[0]), 
                    image=sh.unchecked_image
                    )


"""        
def tree_close(p1):
    print('my_filetree_explorer_support.tree_close')
    sys.stdout.flush()
    global folder
    sel = tree.selection()
    tree.item(sel,image=folder)

def tree_open(p1):
    print('my_filetree_explorer_support.tree_open')
    sys.stdout.flush()
    global openfold
    sel = tree.selection()
    tree.item(sel,image=openfold)
"""


# ######################################################################
#
#   I/O Support Section
#
# ======================================================================


def load_file():   # ?
    """In «Text Box Demo» from Greg,  Mar 21, 2018"""
    global txtbox
    #clear_text()
    if py3 != True:
        filename = tkFileDialog.askopenfilename(
            initialdir="/home/",
            title="Select file",
            filetypes=(("Python files", "*.py"),
            ("text files", "*.txt"),
            ("all files", "*.*")))
    else:
        filename = filedialog.askopenfilename(
            initialdir="/home/",
            title="Select file",
            filetypes=(("Python files", "*.py"),
                       ("text files", "*.txt"),
                       ("all files", "*.*")))
    print('Filename = {0}'.format(filename))
    if not filename:
        pass
    else:
        clear_text()
        data = read_file(filename)
        txtbox.insert('end', data)


def read_text_file_lines(filename):   # ?
    '''function which read text from file and return the
     file content in a string'''
    try:
        with open(filename, 'r') as f:
            f_text = f.read()
            signal = True   # Done.
            return signal, f_text
    except IOError:
        signal = False   # Something went wrong !!
        return signal, ''


def read_file(filename):   # ?
    """In «Text Box Demo» from Greg,  Mar 21, 2018"""
    # ======================================================
    # function read_file()
    # ======================================================
    # Read file, leaving end of lines
    # ======================================================
    with open(filename) as f:
        lines = f.read()
    return lines


def set_icon(root):   # set icon on Linux meubar
    '''place avatar icon on taskbar'''
    # by G.D. Walters
    # import tkinter as tk
    # import tkinter.ttk as ttk
    p1 = tk.Image("photo", file='assets/graphic/avatar.png')
    root.tk.call('wm', 'iconphoto', root._w, p1)


def populate_data():   # treeview support
    import shared as sh
    import json
    json_file_name=f"assets/{sh.pycoder_date}.json"
    print(json_file_name)
    with open(json_file_name, "r") as f:
        data = json.load(f)
    sh.data = {}
    sh.data = data


def set_filenames():    # .gif animation support
    import shared as sh
    # set up filenames using share module sh
    sh.h = "./assets/graphic/h.png"
    sh.h2x_filename = "./assets/graphic/h2x.gif"
    sh.x2h_filename = "./assets/graphic/x2h.gif"


def remove_temp_files():   # cleanUp()
    import shared as sh
    # import os
    filename = sh.module_name
    try:
        os.remove(filename)
        print(f'«{filename}» : the temporary file has been removed!')
    except:
        print(f'«{filename}» : Sorry, the temporary file could not be removed!!')


# ######################################################################
#
#   .gif Animation Support Section
#
# ======================================================================


def open_hamburger(_top1, _w1):
    import shared as sh
    displayfile(_top1, _w1, sh.h2x_filename)
    _w1.TFrameMenu.lift()
    sh.hamburgermenu=False


def close_hamburger(_top1, _w1):
    import shared as sh
    displayfile(_top1, _w1, sh.x2h_filename)
    _w1.TFrameMenu.lower()
    sh.hamburgermenu=True


def number_of_frames(gif):
    "Prints and returns the number of frames of the gif"
    return gif.n_frames


def update(_top1, _w1, ind):
    global root, label
    import shared as sh
    try:
        frame = sh.frames[ind]
        ind += 1
        _w1.TLblHamburger.configure(image=frame)
        root.after(5, update, ind)   # duration of image shift
    except:
        pass


def displayfile(_top1, _w1, filename):
    # import tkinter as tk
    import shared as sh
    # from PIL import Image, ImageTk
    global _image
    file = Image.open(filename)
    frameCnt = number_of_frames(file)
    sh.frames = [tk.PhotoImage( file=filename, format = f'gif -index {i}')
                for i in range(frameCnt)]
    update(_top1, _w1, 0)


# ######################################################################
#
#   Subprocess Section
#
# ======================================================================


def run(cmd):
    import psutil
    import subprocess
    
    print("+ DEBUG exec({0})".format(cmd))
    
    try:
        # Start the subprocess
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        print(f"Started subprocess with PID: {p.pid}")
        return p  # Return the process object so you can control it later
    
    except Exception as e:
        print(f"Failed to start subprocess: {e}")
        return None


# ######################################################################
#
#   Web Support Section
#
# ======================================================================


def load_url(url, timeout):
    import requests
    import urllib.request
    '''Retrieve a single page and report the URL and contents'''
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def scrape_links(url):
    '''Function to scrape links from a webpage'''
    import requests
    from bs4 import BeautifulSoup
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: Status code {response.status_code}")
        return []
    
    # Parse the HTML content of the page with https://shedevspythonworkshop.co.zw/cgi-sys/suspendedpage.cgiBeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <a> tags with href attributes
    links = [a['href'] for a in soup.find_all('a', href=True)]
    
    return links


def get_active_firefox_url():
    ''' Get the url from active window in firefox'''
    import subprocess
    import time        
    # Focus on the active Firefox window
    subprocess.run(["xdotool", "search", "--onlyvisible", "--class", "firefox", "windowactivate"])

    # Simulate Ctrl+L to focus the address bar, then Ctrl+C to copy the URL
    time.sleep(0.5)  # Wait for the window to become active
    subprocess.run(["xdotool", "key", "ctrl+l"])
    time.sleep(0.2)  # Wait for the address bar to be selected
    subprocess.run(["xdotool", "key", "ctrl+c"])
    time.sleep(0.2)  # Give time for the clipboard to update

    # Use xclip to get the URL from the clipboard
    url = subprocess.run(["xclip", "-selectsh.URLSion", "clipboard", "-o"], capture_output=True, text=True).stdout.strip()
    return url


def get_header_text(url):
    import requests
    from bs4 import BeautifulSoup
    # Send a GET request to the URL
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve the webpage: Status code {response.status_code}")
            return None
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the first <h1> tag and get its text
        header = soup.find('h1')
        header_text = header.get_text(strip=True) if header else "No <h1> tag found."
        return header_text
    except:
        return ""


def close_active_firefox_tab():
    # close active tab / window in firefox
    import subprocess
    import time    

    # Focus on the active Firefox window
    subprocess.run(["xdotool", "search", "--onlyvisible", "--class", "firefox", "windowactivate"])

    # Wait for the window to become active
    time.sleep(0.5)

    # Simulate Ctrl+W to close the active tab
    subprocess.run(["xdotool", "key", "ctrl+w"])


# ######################################################################
#
#   Callback Section
#
# ‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒


def on_bindEntryReturnKey():   #---?
    '''supporting def for binding return key on _w1.TEntry1 widget'''
    if _debug:
        print('articlesLookup_support.on_bindEntryReturnKey')
    wich=int(_w1.TEntry1.get())


# ######################################################################
#
#   Roundup Section
#
# ======================================================================


def cleanUp():
    # import datetime
    import atexit
    import shared as sh
    # print('‒'*sh.decoration, '\n')
    # give finish time

    # Register cleanup function to be called when the program exits
    atexit.register(xreader_cleanup)
        
    current_time = datetime.datetime.now()
    finish_time = tot_time(current_time)
    """
    current_time_2 = f'{current_time.hour}:{current_time.minute}:{current_time.second}'
    h1,m1,s1 = sh.current_time_1.split(':')
    h2,m2,s2 = current_time_2.split(':')
    tot_h=int(h2)-int(h1)
    tot_m=int(m2)-int(m1)
    tot_s=int(s2)-int(s1)
    if tot_s < 0:
        remainder=tot_s
        tot_m-=1
        tot_s=60+remainder
    if tot_m < 0:
        remainder=tot_m
        tot_h-=1
        tot_m=60+remainder
    tot_time=f'{tot_h}:{tot_m}:{tot_s}'
    """
    print(f'finish time : {str(current_time)[:19]}')
    print('time used   :', finish_time )
    remove_temp_files()
    print('‒'*sh.decoration, '\n')
    print('Done.')


def xreader_cleanup():
    import os
    import shared as sh
    
    if sh.result:
        kill_process_and_children(sh.result)
    else:
        pass


def kill_process_and_children(p):
    import psutil
    try:
        # Get the parent process by PID
        parent = psutil.Process(sh.result.pid)
        # Terminate all child processes first
        for child in parent.children(recursive=True):
            child.terminate()
        parent.terminate()  # Terminate the parent process
        print(f"Subprocess with PID {sh.result.pid} and its children killed.")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {sh.result.pid}.")
    except Exception as e:
        print(f"Failed to kill subprocess: {e}")
        

"""
# Example usage
p = run("xreader myfile.pdf")

# Later, when you want to kill it:
if p:
    kill_process_and_children(p)
"""
