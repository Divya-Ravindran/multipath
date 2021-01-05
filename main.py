from flask import Flask, render_template, redirect, request
def create_new_story(line):
    new = {"main_line":line,"top_left":None,"top_right":None,"bottom_right":None,"bottom_left":None}
    return new

def get_sentences_for(path):
    if (path != None):
        return dict_paths[path]["main_line"]

def add_new_path(current_path_id,position,new_sentence):
    path_id = "path"+str(len(dict_paths)+1) #current_path_id
    dict_paths[path_id] = create_new_story(new_sentence)
    print(current_path_id,position,path_id)
    dict_paths[current_path_id][position]=path_id

app = Flask(__name__)

dict_paths = {"path1":create_new_story("Once upon a time, there was a big bad wolf.")}

@app.route("/")
def start_main():
    return redirect("/paths/path1")

@app.route("/paths/<path_id>")
def display_story(path_id):
    current_path_dict = dict_paths[path_id]
    top_left_id = current_path_dict["top_left"]
    top_right_id = current_path_dict["top_right"]
    bottom_left_id = current_path_dict["bottom_left"]
    bottom_right_id = current_path_dict["bottom_right"]

    main_line=current_path_dict["main_line"]

    #get the new sentences
    top_left = get_sentences_for(top_left_id)
    top_right = get_sentences_for(top_right_id)
    bottom_left = get_sentences_for(bottom_left_id)
    bottom_right = get_sentences_for(bottom_right_id)

    return render_template("start.html", top_left=top_left, top_right=top_right, bottom_left=bottom_left,bottom_right=bottom_right,
                           top_left_id=top_left_id,top_right_id=top_right_id,bottom_left_id=bottom_left_id, bottom_right_id=bottom_right_id,
                           current_path_id=path_id, main_line = main_line)

@app.route("/new_path/<current_path_id>", methods = ["POST"])
def new_path(current_path_id):
    #current_path_id = request.form("current_path_id")
    position = request.form["position"]
    new_sentence = request.form["new_sentence"]
    add_new_path(current_path_id,position,new_sentence)
    return redirect("/paths/"+current_path_id)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    app.run(port=5000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
