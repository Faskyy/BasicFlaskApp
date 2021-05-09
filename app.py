from flask import Flask, redirect, url_for, render_template, jsonify

app = Flask(__name__)


#added an index route to display numbers using html :) 
@app.route("/")
def home():
    return render_template("index.html")


#all numbers
@app.route('/<int:numbers>', methods=['GET'])
def get_numbers(numbers):
    allNums = []

    for num in range(numbers):
    	if num >= 0:
    		allNums += [num]
        

    #return successful results
    return jsonify({
        'success': True,
        'all numbers': allNums,
    })


#odd numbers
@app.route('/<int:numbers>/odd', methods=['GET'])
def get_odd_numbers(numbers):
    start = 1
    oddNums = []

    for num in range(start, numbers + 1):
        # checking condition
        if num % 2 != 0:
            oddNums += [num]

    #return successful results
    return jsonify({
        'success': True,
        'odd numbers': oddNums,
    })


#even numbers
@app.route('/<int:numbers>/even', methods=['GET'])
def get_even_numbers(numbers):
    evenNums = []

    for num in range(numbers):
        # checking condition
        if num % 2 == 0:
            evenNums += [num]

    #return successful results
    return jsonify({
        'success': True,
        'even numbers': evenNums,
    })

@app.route('/<int:numbers>/prime', methods=['GET'])
def get_prime_numbers(numbers):
	primeNums = []

	for num in range(numbers + 1):
		if num > 1:
			flag = True	
			for i in range(2, num):
				if(num % i) == 0:
					flag = False
			if flag:
				primeNums += [num]				
					

	return jsonify({
		'success': True,
		'prime numbers': primeNums,
	})

if __name__ == "__main__":
	app.run()