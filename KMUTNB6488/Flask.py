from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy 
from KMUTNB8 import Students ,Registration,Subjects,Teacher, session
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:LAInen57820@110.104.9.228:5432/jj1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def index():
    AA = session.query(Students.student_id,Students.S_f_name,Students.S_l_name,Students.S_e_mail,Registration.sub_id,Subjects.subject_name,Registration.grade,
    Teacher.T_f_name,Teacher.T_l_name)\
        .join(Registration,Students.student_id == Registration.student_id).join(Subjects,Registration.sub_id == Subjects.sub_id)\
        .join(Teacher,Subjects.teacher_id == Teacher.teacher_id)
    return render_template('index.html',TEST = AA) 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)