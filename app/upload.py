import os
from flask import Flash, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = `~'
ALLOWED_EXTENSIONS = {'png', 'jpg'}


