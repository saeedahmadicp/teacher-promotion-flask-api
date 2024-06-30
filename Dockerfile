FROM python:3.8-slim

# add user
RUN useradd -r -s /bin/bash user1


ENV HOME /app
WORKDIR  /app
ENV PATH="/app/.local/bin:${PATH}"

RUN chown -R user1:user1 /app
USER user1

# set app config option
ENV FLASK_ENV=production

ADD ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt --user
# Add the rest of the files
COPY . /app
WORKDIR /app

# start web server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "flask_app:app", "--workers=5"]
