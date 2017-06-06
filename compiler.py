from flask import Flask,request,render_template,redirect
import subprocess

app = Flask(__name__)



def compile():
    cmd = ["gcc /home/ramprasad/PycharmProjects/hack/test.c","-o /home/ramprasad/PycharmProjects/hack/hello"]
    subprocess.call(["gcc", "/home/ramprasad/PycharmProjects/hack/test.c", "-o", "/home/ramprasad/PycharmProjects/hack/test"])

    p=subprocess.Popen("/home/ramprasad/PycharmProjects/hack/test",shell=True,stdout = subprocess.PIPE,
						 stderr=subprocess.PIPE,
						 stdin=subprocess.PIPE,universal_newlines=True)
    out,err = p.communicate()
    return out
@app.route('/', methods=['POST', 'GET'])
def add_note():
    if request.method == 'POST':
        f = open('test.c', 'w')
        print request.form['note']
        f.write(request.form['note'])  # python will convert \n to os.linesep
        f.close()

        out1=compile()
        return out1
    else :
        return render_template("index.html")

if __name__ == "__main__" :
	app.run(host='127.0.0.1', port=2000, debug=True)