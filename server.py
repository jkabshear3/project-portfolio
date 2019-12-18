from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/<string:page_name>')
def page_html(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_with_csv(data)
		return redirect('thankyou.html')
	else:
		return 'not post method'
    

def write_with_data(data):
	with open('database.txt', mode="a") as database:
		email = data['email']
		subject = data['subject']
		text = data['text']
		file = database.write(f'\n{email}, {subject}, {text}')


def write_with_csv(data):
	with open('database.csv', mode="a", newline='') as database2:
		email = data['email']
		subject = data['subject']
		text = data['text']
		csv_writer = csv.writer(database2, delimiter=',')
		csv_writer.writerow([email, subject, text])

if __name__ == '__main__':
    app.run()