#import os

# Define the number of folders to create
#num_folders = 100

# Create folders
#for i in range(1, num_folders + 1):
 #   folder_name = f"Day-{i}"
  #  if not os.path.exists(folder_name):
   #     os.mkdir(folder_name)
    #    print(f"Folder '{folder_name}' created.")
    #else:
     #   print(f"Folder '{folder_name}' already exists.")
import os

# Define the number of folders to create
num_folders = 100

# Create folders and place files in each
for i in range(1, num_folders + 1):
    folder_name = f"Day-{i}"
    
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created.")

        # Create and write to the app.js file
        app_js_path = os.path.join(folder_name, "app.js")
        with open(app_js_path, "w") as app_js_file:
            app_js_file.write("// Your JavaScript code here")

        # Create and write to the index.html file
        index_html_path = os.path.join(folder_name, "index.html")
        with open(index_html_path, "w") as index_html_file:
            index_html_file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>My Web Page</title>\n</head>\n<body>\n<h1>Hello, world!</h1>\n<script src=\"app.js\"></script>\n</body>\n</html>")
        
        print(f"Files 'app.js' and 'index.html' added to '{folder_name}'.")
    else:
        print(f"Folder '{folder_name}' already exists.")


