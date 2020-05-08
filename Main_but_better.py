from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return '''
    <h1 style="font-size:20px"><a href="http://127.0.0.1:5000/">Home</a></h1>
    <h1 style="font-size:35px"><center>Weome to the main page!</center><h1>
    <center>
    <img src= https://fyi.extension.wisc.edu/safefood/files/2020/03/sars-cov-19.jpg>
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
   
    <h2>Which is the best description of a variable?</h2> <label for="var_string"><input type="radio" name="variable" 
    value="0" id="var_string" />Identifies a portion of a string.</label> <label for="var_join"><input type="radio" 
    name="variable" value="0" id="var_join" />A method to join strings.</label> <label for="var_info"><input 
    type="radio" name="variable" value="25" id="var_info" />Allows you to store information so it can be reused 
    throughout the program</label> <label for="var_condition"><input type="radio" name="variable" value="0" 
    id="var_condition"/>Allows you to make a decision based on a condition.</label> 

<h2>Which is the best description of the substring method?</h2> <label for="sub_string"><input type="radio" 
name="sub" value="25" id="sub_string"/>Identifies a portion of a string.</label> <label for="sub_join"><input 
type="radio" name="sub" value="0" id="sub_join"/>A method to join strings.</label> <label for="sub_info"><input 
type="radio" name="sub" value="0" id="sub_info" />Allows you to store information so it can be reused throughout the 
program</label> <label for="sub_condition"><input type="radio" name="sub" value="0" id="sub_condition" />Allows you 
to make a decision based on a condition.</label> 

<h2>Which is the best description of concatenation?</h2> <label for="cat_string"><input type="radio" name="con" 
value="0" id="cat_string" />Identifies a portion of a string.</label> <label for="cat_join"><input type="radio" 
name="con" value="25" id="cat_join" />A method to join strings.</label> <label for="cat_info"><input type="radio" 
name="con" value="0" id="cat_info" />Allows you to store information so it can be reused throughout the 
program</label> <label for="cat_condition"><input type="radio" name="con" value="0" id="cat_condition" />Allows you 
to make a decision based on a condition.</label> 

<h2>Which is the best description of an if statement?</h2> <label for="if_string"><input type="radio" name="ifstate" 
value="0" id="if_string" />Identifies a portion of a string.</label> <label for="if_join"><input type="radio" 
name="ifstate" value="0" id="if_join" />A method to join strings.</label> <label for="if_info"><input type="radio" 
name="ifstate" value="0" id="if_info" />Allows you to store information so it can be reused throughout the 
program</label> <label for="if_condition"><input type="radio" name="ifstate"  value="25" id="if_condition" />Allows 
you to make a decision based on a condition.</label> 

<button type="submit" value="Submit">Submit</button>

</form>

<p>Your grade is: <span id="grade">__</span></p>
<p id="grade2"></p>



<script>
document.getElementById("form1").onsubmit=function() {
       variable = parseInt(document.querySelector('input[name = "variable"]:checked').value);
sub = parseInt(document.querySelector('input[name = "sub"]:checked').value);
con = parseInt(document.querySelector('input[name = "con"]:checked').value);
ifstate = parseInt(document.querySelector('input[name = "ifstate"]:checked').value);


result = variable + sub + con + ifstate;

document.getElementById("grade").innerHTML = result;

 grading = [
	{score:0,feedback:"I don't think you studied", image: "none.jpg"},
	   {score:25,feedback:"You need to spend more time. Try again", image: "poor.jpg"},
	   {score:50,feedback:"I think you could do better. Try again.", image: "avg.jpg"},
	   {score:75,feedback:"So close. Try again.", image: "above.jpg"},
	   {score:100,feedback:"Excellent! You're a JavaScript pro!", image: "excellent.jpg"}
	   ];

for(i=0; i<grading.length; i++) {
    if(result == grading[i].score) {
    result2 = grading[i].feedback + "<br /><img src='" + grading[i].image + "' width='300'  />";
}
}


document.getElementById("grade2").innerHTML = result2;

return false; // required to not refresh the page; just leave this here
} //this ends the submit function

</script>
'''


if __name__ == "__main__":
    app.run(use_reloader=True)
