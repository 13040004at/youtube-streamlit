import time

from clinic.Clinic import Clinic, Patient
from clinic.file_io import load_file, save_file

myClinic = Clinic()
patients = load_file()
id = len(patients)
while(bool != 'N'):
    name = input('お名前を教えて下さい')
    symptom = input('どのような症状ですか？')
    print('あなたの診察番号は', id,'です')
    if patients == None:
        patients = [[name, id, symptom]]
    else:
        patients.append([name, id, symptom])
    id += 1
    bool = input('他のご用の方はいませんか？ ない場合は"N"を入力')

save_file(patients)

for p in patients :
    name, age, symptom = p

    # loopで取得する name, age, symptomでPatientをインスタンス
    patient = Patient(name, age, symptom)

    # myclinicに予約 *reserveメソッド使用
    myClinic.reserve(patient)

    # 現在の待ち人数を表示
myClinic.show_waiting_count()



print('診察をします')
emergency = input('急患の方はいませんか？ある場合"Y"を入力')
if(emergency == 'Y'):
    time.sleep(1)
    myClinic.diagnosis(int(emergency))
    time.sleep(1)
    myClinic.show_waiting_count()

for i in patients:
    time.sleep(1)
    myClinic.diagnosis()
    time.sleep(1)
    myClinic.show_waiting_count()
