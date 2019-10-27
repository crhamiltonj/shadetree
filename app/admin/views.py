from flask import Blueprint, render_template, request


admin_bp = Blueprint('admin_bp', __name__, url_prefix="/admin", template_folder='templates', static_folder='static')

@admin_bp.route('/dashboard')
@admin_bp.route('/')
def dashboard():
    return render_template('dashboard.html')


