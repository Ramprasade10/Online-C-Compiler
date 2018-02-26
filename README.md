Online-C-Compiler provides a simple,clean and functional User Interface for Compiling and Executing C Code Online without 
any compiler in the local system.
Technologies used include flask(python),HTML5,CSS,AWS.

Components of the Project:
1.Flask App
2.Webpage

The Code runs from the Flask app during the first run, request method being GET, it loads the Webpage through Jinja2
render_template().
User can input the code in the textArea when compile button is clicked a POST request is initiated.
The Flask app is intitiated ,request being POST,the code is saved locally as test.c through python file handling functions open() and write().compile() is called for compiling test.c.
subprocess.call(["gcc", "test.c", "-o", "test"]) is called to execute terminal command which compiles the C code saved in test.c,which results in a executable file test.
subprocess.Popen("test",shell=True,stdout =subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,
universal_newlines=True) returns the output of the executable file,this in returned to the webpage as output of the code.

The project aims to provide a platform for students to compile their code on the go, capabilities to share and commit
code with ease.
