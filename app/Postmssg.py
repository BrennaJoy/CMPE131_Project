@myapp_obj.route('/postmessage', methods = ['POST','GET'])
@login_required
def post():
    error = ''
    current_form = postmssgform()
    if current_form.validate_on_submit():
        if len(current_form.text.data) >250:
            error = 'Post is too long! (max characters is 250)'
        else:
            post = Post()
            post.post = current_form.text.data  #save body text to db
            post.user_id = current_user.id      #save current user's id to track poster
            today = date.today()
            post.date = str(today)
            with myapp_obj.app_context():       #add object to db
                db.session.add(post)
                db.session.commit()
            return redirect('/homepage')
    return render_template('postmessage.html', form = current_form, error = error)
