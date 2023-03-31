from flask import Flask, render_template, redirect, url_for, request
from db.database import database
from forms import CreateForm, EditorForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'crm_gambling_1403_secret_key'


@app.route('/')
def main():
    try:
        data = dict(database.child('urls').get().val())
        # print(data, data.keys())
        return render_template('index.html', data=data, lenght=len(data), keys=list(data.keys()))
    except Exception as ex:
        data = {}
        return render_template('index.html', data=data, lenght=0, keys=[])


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateForm()
    if form.validate_on_submit():
        id_url = form.id.data
        url = form.url.data
        status = form.status.data
        try:
            if id_url == "":
                return render_template('create.html', form=form, error='Вы не указали id')
            if url == "":
                return render_template('create.html', form=form, error='Вы не указали ссылку')
            else:
                if status == 'True':
                    status = 1
                else:
                    status = 0
                url_data = {'id': id_url, 'url': url, 'status': bool(status)}
                result = database.child("urls").child(id_url).set(url_data)
                print(result)
        except Exception as ex:
            print(ex)
        return redirect('/')
    return render_template('create.html', form=form)


@app.route('/editor/<id_url>', methods=['GET', 'POST'])
def editor(id_url):
    form = EditorForm()
    url_e = database.child('urls').child(id_url).child('url').get().val()
    try:
        id_url = id_url
        url = form.url.data
        status = form.status.data
        if form.validate_on_submit():
            result = ''
            if form.submit.data:
                if url == "":
                    return redirect('/editor/' + id_url)
                if status == 'True':
                    status = 1
                else:
                    status = 0
                url_data = {'id': id_url, 'url': url, 'status': bool(status)}
                result = database.child("urls").child(id_url).update(url_data)
            if form.delete.data:
                result = database.child("urls").child(id_url).remove()
            print(result)
            return redirect('/')
    except Exception as ex:
        print(ex)
    return render_template('editor.html', form=form, id_url=id_url, url_e=str(url_e))


@app.route('/countries', methods=['GET', 'POST'])
def countries():
    if request.method == 'POST':
        c_code = request.form.get('c_code')
        try:
            data = dict(database.child('countries').get().val()).values()
        except Exception as ex:
            data = {}
        if data:
            if c_code == "" or c_code in data:
                pass
            else:
                database.child('countries').push(c_code)
        else:
            database.child('countries').push(c_code)
    try:
        data = dict(database.child('countries').get().val())
        return render_template('countries.html', data=data, lenght=len(data), keys=list(data.keys()))
    except Exception as ex:
        data = {}
        return render_template('countries.html', data=data, lenght=0, keys=[])


@app.route('/ips', methods=['GET', 'POST'])
def ips():
    if request.method == 'POST':
        ip = request.form.get('ip')
        try:
            data = dict(database.child('ips').get().val()).values()
        except Exception as ex:
            data = {}
        if data:
            if ip == "" or ip in data:
                pass
            else:
                database.child('ips').push(ip)
        else:
            database.child('ips').push(ip)
    try:
        data = dict(database.child('ips').get().val())
        return render_template('ips.html', data=data, lenght=len(data), keys=list(data.keys()))
    except Exception as ex:
        data = {}
        return render_template('ips.html', data=data, lenght=0, keys=[])


@app.route('/timezones', methods=['GET', 'POST'])
def timezones():
    if request.method == 'POST':
        timezone = request.form.get('timezone')
        try:
            data = dict(database.child('timezones').get().val()).values()
        except Exception as ex:
            data = {}
        if data:
            if timezone == "" or timezone in data:
                pass
            else:
                database.child('timezones').push(timezone)
        else:
            database.child('timezones').push(timezone)
    try:
        data = dict(database.child('timezones').get().val())
        return render_template('timezones.html', data=data, lenght=len(data), keys=list(data.keys()))
    except Exception as ex:
        data = {}
        return render_template('timezones.html', data=data, lenght=0, keys=[])


@app.route('/del_country/<id_country>', methods=['GET', 'POST'])
def del_country(id_country):
    database.child('countries').child(id_country).remove()
    return redirect('/countries')


@app.route('/del_timezone/<id_timezone>', methods=['GET', 'POST'])
def del_timezone(id_timezone):
    database.child('timezones').child(id_timezone).remove()
    return redirect('/timezones')


@app.route('/del_ip/<id_ip>', methods=['GET', 'POST'])
def del_ip(id_ip):
    database.child('ips').child(id_ip).remove()
    return redirect('/ips')


if __name__ == "__main__":
    app.run()
