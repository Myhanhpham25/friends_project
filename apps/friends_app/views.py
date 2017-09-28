# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..login_app.models import User


def dashboard(request):
	# User.objects.all().delete()

	curUser = User.objects.get(id = request.session['id'])
	users = User.objects.all()

	context = {
	'myfriends' : [],
	'otherfriends' : []
	}

	for user in users:
		if user not in curUser.friends.all():
			context['otherfriends'].append(user)
		if user in curUser.friends.all():
			context['myfriends'].append(user)


	return render(request, "friends_app/dashboard.html", context)

def create(request, user_id):

	### after fixing the models the friends column no longer works.
	addfriend = User.objects.get(id = user_id)
	user = User.objects.get(id = request.session['id'])
	friendlist= User.objects.get(id = request.session['id']).friends.all(),
	users = User.objects.all()


	for person in users:
		if person not in friendlist:
			friendship = user.friends.add(addfriend)


	if 'email' not in request.session:
		return redirect("/")
	else:
		return redirect("/friends_app/dashboard")


def show(request, user_id):
	try:
		request.session['email']
	except:
		return redirect('/')

	user = User.objects.get(id=user_id)

	url = '/friends_app/show.html' + str(user_id)

	context = {

	'users' : user
	}

	return render(request, 'friends_app/show.html/', context)

def remove(request, user_id):
	try:
		request.session['email']
	except:
		return redirect('/')

	removefriend = User.objects.get(id = user_id)
	user = User.objects.get( id = request.session['id'])
	user.friends.remove(removefriend)

	return redirect("/friends_app/dashboard")



