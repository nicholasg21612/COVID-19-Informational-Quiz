from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return '''
    <h1 style="font-size:20px"><a href="http://127.0.0.1:5000/">Home</a></h1>
    <h1 style="font-size:35px"><center>Welcome to the main page!</center><h1>
    <center>
    
    </center>

    <h1 style="color:green"><a href="http://127.0.0.1:5000/1"><center>Take Test Here!</center></a></h1>

    '''


@app.route("/1")
def one():
    return '''
    <h1></h1>

     <h2 style="float:right;text-align:right;">Page 1-2</h2>
       <h1 style="float:left;text-align;"><small><small> <a href="http://127.0.0.1:5000/">Home </a></small></small></h1>
      &ensp;
    <h5><h5>
     &nbsp;
     <h1 style="font-size:37px"><center>What is the CoronaVirus?</center><h1>
    <h1></h1>
    <body> 

    <p1 style="font-size:18px"><center>a)Any group of RNA viruses that cause a variety of </center></p1> 
    <p5 style="font-size:18px"><center>diseases in humans and other animals.</p5> 

    <p5 style="font-size:18px"><center>b)A virus that specifically attacks the lungs.</center></p5> 
    <p5 style="font-size:18px"><center>c)The most recent global pandemic.</center></p5>

    <center><input></center> 
    </body>
 &nbsp;
 <h1></h1>
 &nbsp;

 <h1 style="font-size:34px"><center> Where did COVID-19 start?</center><h1>
    <h1></h1>
    <body> 

    <p1 style="font-size:21px"><center>a)Shenzhen, China</center></p1>
    <p5 style="font-size:21px"><center>b)Tianjin, China</center></p5>
    <p5 style="font-size:21px"><center>c)Wuhan, China</center></p5>
    <center><input></center>
    </body>

&nbsp;
 <h1></h1>
 &nbsp;

 <h1 style="font-size:30px"><center>COVID-19 was created in a lab.</center><h1>
    <h1></h1>
    <body> 
    <p1 style="font-size:21px"><center>a) Yes, this is true</center></p1>
    <p5 style="font-size:21px"><center>b)No, this is false</center></p5>
    <center><input></center>
    </body>

    &nbsp;
 <h1></h1>
 &nbsp;

 <h1 style="font-size:27px"><center> How long does it take to kill the virus,when washing</center><h1>
  <h1 style="font-size:27px"><center>your hands under hot water and soap?</center><h1> 
 <h1></h1>
 <body> 

    <p1 style="font-size:21px"><center>a)60 seconds</center></p1>
    <p5 style="font-size:21px"><center>b)40 seconds</center></p5>
    <p5 style="font-size:21px"><center>c)30 seconds</center></p5>
    <p5 style="font-size:21px"><center>d)20 seconds</center></p5>
    <center><input></center>
    </body>


&nbsp;
 <h1></h1>
 &nbsp;

 <h1 style="font-size:27px"><center>You can have COVID-19 without</center><h1>
 <h1 style="font-size:27px"><center> showing any symptoms.</center><h1>
    <h1></h1>
    <body> 

    <p1 style="font-size:21px"><center>a)No, this is false.</center></p1>
    <p5 style="font-size:21px"><center>b)yes, this is true.</center></p5>
    <center><input></center>
    </body>


    &nbsp;
 <h1></h1>
 &nbsp;

 <h1 style="font-size:27px"><center>If you have the virus, you should:</center><h1>
    <h1></h1>
    <body> 

    <p1 style="font-size:18px"><center>a)Stay home when you can.</center></p1>
    <p5 style="font-size:18px"><center>b)Avoid any type of public transportation.</center></p5>
    <p5 style="font-size:18px"><center>c)separate yourself from your pets.</center></p5>
    <p5 style="font-size:18px"><center>d)Call if you need medical attention.</center></p5>
    <p5 style="font-size:18px"><center>e)All of the above.</center></p5>
    <center><input></center>
    </body>

   &nbsp;
 <h1></h1>
 &nbsp;

 <h1 style="font-size:27px"><center>Which of these warning signs show that you may have the disease?</center><h1>
 <h1></h1>
 <body> 

    <p1 style="font-size:19px"><center>a)Trouble breathing</center></p1>
    <p5 style="font-size:19px"><center>b)Persistent pain or pressure in chest</center></p5>
    <p5 style="font-size:19px"><center>c)New confusion or inability to arouse</center></p5>
    <p5 style="font-size:19px"><center>d)bluish lips or face</center></p5>
    <p5 style="font-size:19px"><center>e)All of the above </center></p5>
    <center><input></center>
    </body>

&nbsp;
 <h1></h1>
 &nbsp;

 <h1 style="font-size:27px"><center>Is COVID-19 seasonal like the flu?</center><h1>
 <h1></h1>
 <body> 

    <p1 style="font-size:21px"><center>a)Yes</center></p1>
    <p5 style="font-size:21px"><center>b)Possibly</center></p5>
    <p5 style="font-size:21px"><center>c)No</center></p5>

    <center><input></center>
    </body>

    &nbsp;
 <h1></h1>
 &nbsp;

<h1 style="font-size:27px"><center>What is the best approach to eradicating</center><h1>
<h1 style="font-size:27px"><center>the virus Fast and efficiently?</center><h1>
 <h1></h1>
 <body> 

    <p1 style="font-size:21px"><center>a)No regulations</center></p1>
    <p5 style="font-size:21px"><center>b)Attempted quarantine</center></p5>
    <p5 style="font-size:21px"><center>c)Moderate distancing </center></p5>
    <p5 style="font-size:21px"><center>d)Extensive distancing</center></p5>

    <center><input></center>
    </body>

    &nbsp;
 <h1></h1>
 &nbsp;

    <h1 style="font-size:27px"><center> What is the best approach to keeping the virus at an all time low?</center><h1>
 <h1></h1>
 <body> 

    <p1 style="font-size:21px"><center>a)No regulations</center></p1>
    <p5 style="font-size:21px"><center>b)Attempted quarantine</center></p5>
    <p5 style="font-size:21px"><center>c)Moderate distancing </center></p5>
    <p5 style="font-size:21px"><center>d)Extensive distancing</center></p5>

    <center><input></center>
    </body>

     &nbsp;
 <h1></h1>
 &nbsp;

   <h2 style="float:right;text-align:right;"><a href="http://127.0.0.1:5000/2">Next --></a></h2>
    '''


@app.route("/2")
def two():
    return '''
    <h1 style="float:right;text-align:right;"><small><small> Page 2-2 </small></small></h1>
       <h1 style="float:left;text-align;"><small><small> <a href="http://127.0.0.1:5000/">Home </a></small></small></h1>
      &ensp;
      &ensp;

    <h1><center>This is the last page of the questions, Keep going!</center><h1>

  &nbsp;
 &nbsp;

<h1 style="font-size:27px"><center>What is the worst approach to try with COVID?</center><h1>
 <h1></h1>
 <body> 

    <p1 style="font-size:21px"><center>a)No regulations</center></p1>
    <p5 style="font-size:21px"><center>b)Attempted quarantine</center></p5>
    <p5 style="font-size:21px"><center>c)Moderate distancing </center></p5>
    <p5 style="font-size:21px"><center>d)Extensive distancing</center></p5>

    <center><input></center>
    </body>

 &nbsp;
 <h1></h1>
 &nbsp;

<h1 style="font-size:27px"><center>Can your pets spread COVID-19 as well?</center></h1>
 <h1></h1>
 <body> 

    <p1 style="font-size:21px"><center>a)Yes</center></p1>
    <p5 style="font-size:21px"><center>b)No, There is no conclusive evidence yet</center></p5>

    <center><input></center>
    </body>


    &nbsp;
 <h1></h1>
 &nbsp;

<h1 style="font-size:27px"><center>Should you over budget and/or hoard Items at your</center></h1> <h1></h1> <body> 
<h1 style="font-size:27px"><center>local supermarket in response to COVID-19?</center></h1> <h1></h1> <body> 

    <p1 style="font-size:21px"><center>a)No, this idea is selfish and possibly wasteful under </center></p1> 
    <p1 style="font-size:21px"><center>the right circumstances.</center></p1> 
    <p5 style="font-size:21px"><center>b)Yes, you need to be prepared to undergo quarantine</center></p5> 
    <p5 style="font-size:21px"><center>for months and maybe even years.</center></p5> 

    <center><input></center>
    </body>

   &nbsp;
 <h1></h1>
 &nbsp;

<h1 style="font-size:27px"><center>As of now, which mathematical curve best describes </center><h1> <h1></h1> <body> 
<h1 style="font-size:27px"><center>the increase in COVID-19 cases?</center><h1> <h1></h1> <body> 

    <p1 style="font-size:21px"><center>a)Linear curve</center></p1> 
    <p5 style="font-size:21px"><center>b)Logistic curve</center></p5> 
    <p5 style="font-size:21px"><center>c)Exponential curve</center></p5> 
    <p5 style="font-size:21px"><center>d)Quadratic curve</center></p5> 
    <center><input></center>
    </body>

&nbsp;
 <h1></h1>
 &nbsp;

<h1 style="font-size:27px"><center>If you are going to have a celebration during these</center></h1> <h1></h1> <body> 
<h1 style="font-size:27px"><center>times, can a group of 9 people suffice?</center></h1> <h1></h1> <body> 

    <p1 style="font-size:21px"><center>a)Yes</center></p1>
    <p5 style="font-size:21px"><center>b)No</center></p5>

    <center><input></center>
    </body>


    &nbsp;
 <h1></h1>
 &nbsp;

<h1 style="font-size:27px"><center>According to global statistical odds, How likely are </center></h1> <h1></h1> <body> 
<h1 style="font-size:27px"><center> you to recover in May if you have the virus? </center></h1> <h1></h1> <body> 

    <p1 style="font-size:24px"><center>a)49-57%</center></p1>
    <p5 style="font-size:24px"><center>b)50-60%</center></p5>
    <p5 style="font-size:24px"><center>c)60-70%</center></p5> 
    <p5 style="font-size:24px"><center>d)75-85%</center></p5>
    <center><input></center>
    </body>


     &nbsp;
 <h1></h1>
 &nbsp;

<h1 style="font-size:27px"><center>According to National Statistical odds, How likely are you to survive 
</center></h1> <h1></h1> <body> <h1 style="font-size:27px"><center>the virus during the month of may if you already 
have COVID?</center></h1> <h1></h1> <body> 

    <p1 style="font-size:24px"><center>a)99-91%</center></p1>
    <p5 style="font-size:24px"><center>b)90-85%</center></p5>
    <p5 style="font-size:24px"><center>c)85-80%</center></p5> 
    <p5 style="font-size:24px"><center>d)80-75%</center></p5>
    <center><input></center>
    </body>

&nbsp;
 <h1></h1>
 &nbsp;

<h1 style="font-size:27px"><center>What is the recommended % of isopropyl alcohol that should</center></h1> <h1></h1> 
<body> <h1 style="font-size:27px"><center>be in your hand sanitizer?</center></h1> <h1></h1> <body> 

    <p1 style="font-size:21px"><center>a)65% and up</center></p1>
    <p5 style="font-size:21px"><center>b)70% and up</center></p5>
    <p5 style="font-size:21px"><center>c)75% and up</center></p5>
    <p5 style="font-size:21px"><center>d)80% and up</center></p5>

    <center><input></center>
    </body>

    &nbsp;
 <h1></h1>
 &nbsp;

<h1 style="font-size:27px"><center>If you have pre-existing conditions like Diabetes or advanced age,</center></h1> 
<h1></h1> <body> <h1 style="font-size:27px"><center>The coronavirus can be more of a danger for you.</center></h1> 
<h1></h1> <body> 

    <p1 style="font-size:24px"><center>a)True</center></p1>
    <p5 style="font-size:24px"><center>b)False</center></p5>

    <center><input></center>
    </body>


  &nbsp;
 <h1></h1>
 &nbsp;

<h1 style="font-size:27px"><center>Does the COVID-19 have a cure?</center></h1> 

<h1></h1> 
<body> 

    <p1 style="font-size:24px"><center>a)Yes</center></p1>
    <p5 style="font-size:24px"><center>b)Possibly</center></p5>
    <p5 style="font-size:24px"><center>c)No</button></center></p5> 


    <center><input></center>
    </body>


       <h2 style="float:right;text-align:right;"><a href="http://127.0.0.1:5000/3">Finish --></a></h2>
       <h2 style="float:left;text-align;"><a href="http://127.0.0.1:5000/1"><-- Previous</a></h2>
      &ensp;
'''


@app.route("/3")
def three():
    return '''
 <h1 style="float:right;text-align:right;"><small><small> Analysis page </small></small></h1>
       <h1 style="float:left;text-align;"><small><small> <a href="http://127.0.0.1:5000/">Home </a></small></small></h1>
       &ensp;
      <h3><h3>
      &ensp;
  <h1><center>Good Effort! here are your results:</center><h1>
    &nbsp;
 <h1></h1>
 &nbsp;

 <h1><center>You got x out of 20!</center></h1>
 <h1><center>x/20</center></h1>
 <h1><a href="http://127.0.0.1:5000/1"><center>Try again?</center></a><h1>
 '''


if __name__ == "__main__":
    app.run(use_reloader=True)
