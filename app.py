from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return '''<html>
    <h1>Welcome!!</h1>
    <br><br>
    <a href="/food1"> Go to the first food photo</a>
    <br><br>
    <a href="/food3"> Go to the 3 food photo!</a>
    <br><br>
    <a href="/pet2"> Go to 2 pet photo!</a>
    <br><br>
    <a href="/space1"> Go to 1 space photo!</a>
    <br><br>
    </html>'''

@app.route('/food1')
def food1():
    return '''<html>
    <body>
    <h1>Welcome to the second page!</h1>
    <br><br>
    <img src="https://media-cdn.tripadvisor.com/media/photo-s/17/9b/5e/5c/soshi-rolls.jpg">
    <h2>I love soshi because it's tasty and healthy!</h2>
    <a href="/home"> Go back to the home page!</a>
    </body>

    </html>'''

@app.route('/food2')
def food2():
    return'''<html>
    <body>
    <h1>Here is the 2 second food photo!</h1>
    <br><br>
<img src="https://lindseyeatsla.com/wp-content/uploads/2021/11/LindseyEats_Spicy_Garlic_Noodles-3.jpg">
<a href="/food3"> Go to the 3 food photo</a>

    </body>
</html>'''

@app.route('/food3')
def food3():
    return'''<html>
    <body>
    <h1>Here is the 3 food photo!</h1>
    <br><br>
    <img src="https://buttermilkbysam.com/wp-content/uploads/2023/07/no-churn-chocolate-ice-cream-7.jpg">
    <a href="/home"> Go back to the home page!</a>
    </body>
    </html>'''

@app.route('/pet1')
def pet1():
    return'''<html>
<body>
<h1>Here is the 1 pet photo!</h1>
<br><br>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQE-MehhHlLqC7wcuTXbX8nW3vYHUeKTgPNA&s">
<a href="/pet2"> Go To the 2 pet photo</a>
</body>
</html>'''

@app.route('/pet2')
def pet2():
    return'''<html>
<body>
<h1>Here is the 2 pet photo!</h1>
<br><br>
<img src="https://www.wfla.com/wp-content/uploads/sites/71/2023/05/GettyImages-1389862392.jpg?w=2560&h=1440&crop=1">
<a href="/pet1"> Go To the 1 pet photo</a>
<a href="/pet3"> Go To the 3 pet photo</a>
<a href="/home"> Go back to the home page!</a>
</body>
</html>'''

@app.route('/pet3')
def pet3():
    return'''<html>
<body>
<h1>Here is the 3 pet photo!</h1>
<br><br>
<img src="https://www.humanesociety.org/sites/default/files/2019/03/rabbit-475261_0.jpg">
<a href="/pet3"> Go To the 3 pet photo</a>
<a href="/home"> Go back to the home page!</a>
</body>
</html>'''

@app.route('/space1')
def space1():
    return'''<html>
<body>
<h1>Here is the 1 space photo!</h1>
<br><br>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgTc2V1FngTfLoX526H97RWBP68sOQE7BJ6Q&s">
<a href="/space2"> Go To the 2 space photo</a>
<a href="/space3"> Go To the 3 space photo</a>
<a href="/home"> Go back to the home page!</a>
</body>
</html>'''

@app.route('/space2')
def space2():
    return'''<html>
<body>
<h1>Here is the 2 space photo!</h1>
<br><br>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPevZcapaw0UrpzSfbp6baVvcO2CFtGalb9w&s">
<a href="/space1"> Go To the 1 space photo</a>
<a href="/space3"> Go To the 3 space photo</a>
</body>
</html>'''

@app.route('/space3')
def space3():
    return'''<html>
<body>
<h1>Here is the 3 space photo!</h1>
<br><br>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5awrRMjYQ68AihQwDAuNbPmAJC_TZ_DpS5w&s">
<a href="/space1"> Go To the 1 space photo</a>
<a href="/space2"> Go To the 2 space photo</a>
</body>
</html>'''

if __name__ == '__main__':
    app.run(debug=True)