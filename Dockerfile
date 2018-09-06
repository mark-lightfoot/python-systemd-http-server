FROM python
COPY app.py /opt/python-http-server/app.py
COPY public /opt/python-http-server/public
ENTRYPOINT ["/opt/python-http-server/app.py"]
