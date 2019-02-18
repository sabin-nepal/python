import webbrowser
a = input("search video")
print("opening Browser")
webbrowser.open_new_tab('http://youtube.com/search?q=%s'%a)