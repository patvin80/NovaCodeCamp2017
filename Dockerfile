FROM tiangolo/uwsgi-nginx-flask:flask

COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt