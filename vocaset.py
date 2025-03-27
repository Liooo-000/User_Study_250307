import streamlit as st
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import random
import poplib
from email.parser import Parser
from datetime import datetime, timedelta

random_range = 10

@st.cache_data
def send_email(email, password, array):
    # 构建邮件主体
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email  # 收件人邮箱
    msg['Subject'] = fr'{dataset} Number of submissions {sum(array)}/{random_range*3}'
    
    # 邮件正文
    string = ''.join([str(element) for element in array])
    text = MIMEText(string)
    msg.attach(text)
     
    # 发送邮件
    try:
        smtp = smtplib.SMTP('smtp.126.com')
        smtp.login(email, password)
        smtp.sendmail(email, email, msg.as_string())
        smtp.quit()
    except smtplib.SMTPException as e:
        print('邮件发送失败，错误信息：', e)

@st.cache_data
def read_email(myemail, password):
    try:
        pop3_server = 'pop.126.com'
        subject_to_search = f'{dataset} Number of submissions'

        # 连接到 POP3 服务器
        mail_server = poplib.POP3_SSL(pop3_server, 995)
        mail_server.user(myemail)
        mail_server.pass_(password)

        # 搜索符合特定主题的邮件
        num_messages = len(mail_server.list()[1])
        content = None  # 初始化变量
        found = False
        for i in range(num_messages, 0, -1):
            raw_email = b'\n'.join(mail_server.retr(i)[1]).decode('utf-8')
            email_message = Parser().parsestr(raw_email)
            subject = email_message['Subject']
            
            if subject and subject.startswith(subject_to_search):
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        content = part.get_payload(decode=True).decode(part.get_content_charset())
                        found = True
                        break  # 找到满足条件的邮件后及时跳出循环
                if found:
                    break

        # 关闭连接
        mail_server.quit()
        array = [int(char) for char in content]
        return array

    except Exception as e:
        st.error('网络问题，请刷新页面')

@st.cache_data
def read_email_(myemail, password):
    try:
        pop3_server = 'pop.126.com'
        subject_to_search = f'{dataset} Number of submissions'

        # 连接到 POP3 服务器
        mail_server = poplib.POP3_SSL(pop3_server, 995)
        mail_server.user(myemail)
        mail_server.pass_(password)

        # 搜索符合特定主题的邮件
        num_messages = len(mail_server.list()[1])
        content = None  # 初始化变量
        found = False
        for i in range(num_messages, 0, -1):
            raw_email = b'\n'.join(mail_server.retr(i)[1]).decode('utf-8')
            email_message = Parser().parsestr(raw_email)
            subject = email_message['Subject']
            
            if subject and subject.startswith(subject_to_search):
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        content = part.get_payload(decode=True).decode(part.get_content_charset())
                        found = True
                        break  # 找到满足条件的邮件后及时跳出循环
                if found:
                    break

        # 关闭连接
        mail_server.quit()
        array = [int(char) for char in content]
        return array

    except Exception as e:
        st.error('网络问题，请刷新页面')

def instrunction():
    st.subheader("Instructions: ")
    # text1 = 'Please watch the short videos (duration 4~7s) of two animated talking heads. \
            # You need to choose the talking head (the :blue[left] or the :blue[right]) that moves more naturally in terms of the full :blue[face] and the :blue[lips]. '
    # text2 = 'Please :blue[turn on the sound] on your computer while you are watching the videos.'
    text1 = "请观看以下含两个说话者的视频（时长2～8s），判断哪个（:blue[左边]或:blue[右边]）说话者的:blue[嘴唇]动作和:blue[脸部]动作更自然。"
    text2 = "看视频时请打开设备上的声音。"
    st.markdown(text1)
    st.markdown(text2)

def QA(Lip_Sync, Motion_Flu, num):
    # 定义问题和选项
    # question_1 = "Comparing the two full :blue[faces], which one looks more :blue[realistic]?"
    # options_1 = ["", "Left", "Right"]
    # question_2 = "Comparing the :blue[lips] of two faces, which one is more :blue[in sync with audio]?"
    # options_2 = ["", "Left", "Right"]
    question_1 = "哪个说话者的:blue[嘴唇]运动和:blue[音频]更:blue[同步]？"
    options_1 = ["", "左边", "右边"]
    # question_2 = f"说话者的情感为:blue[{emotion}],  哪个说话者更能:blue[准确]表达该情感？"
    # options_2 = ["", "左边", "右边"]
    question_2 = "哪个说话者的:blue[面部]运动更:blue[自然真实]？"
    options_2 = ["", "左边", "右边"]

    # 显示问题并获取用户的答案
    answer_1 = st.radio(label=question_1, options=options_1, key=fr"button{num}.1")
    answer_2 = st.radio(label=question_2, options=options_2, key=fr"button{num}.2")

    # 以1/0数据保存
    ans1 = get_ans(answer_1)
    ans2 = get_ans(answer_2)

    # 保存结果到列表
    Lip_Sync[num-1] = ans1
    Motion_Flu[num-1] = ans2

# 将用户的答案转化为1/0
def get_ans(answer_str):
    if "Left" in answer_str:
        return "1"
    elif "Right" in answer_str:
        return "0"
    elif "" in answer_str:
        return "3"
    
@st.cache_data
def play_video(file_name):
    video_bytes = open(file_name, 'rb').read()
    return video_bytes

@st.cache_data
def data_collection(email, password, Lip_Sync, Motion_Flu, random_num, array):
    # 发送内容
    data1 = ''.join(str(x) for x in Lip_Sync)
    data2 = ''.join(str(x) for x in Motion_Flu)
    string = "lip:" + data1 + "\n" + "motion:" + data2
    localtime = localtime = datetime.now()
    seconds = localtime.strftime('%S')
    
    localtime += timedelta(hours=8)
    localtime = localtime.strftime('%m-%d %H:%M:%S')
    # 打开文件并指定写模式
    ID = dataset + "_" + str(random_num+1) + "_" + str(array[random_num]) + "_" + seconds
    file_name = ID + ".txt"
    file = open(file_name, "w")
    # 将字符串写入文件
    file.write(string)
    # 关闭文件
    file.close()

    # 构建邮件主体
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email  # 收件人邮箱
    msg['Subject'] = ID

    # 邮件正文
    text = MIMEText(string)
    msg.attach(text)

    # 添加附件
    with open(file_name, 'rb') as f:
        attachment = MIMEApplication(f.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=file_name)
        msg.attach(attachment)

    # 发送邮件
    try:
        smtp = smtplib.SMTP('smtp.126.com')
        smtp.login(email, password)
        smtp.sendmail(email, email, msg.as_string())
        smtp.quit()
    except smtplib.SMTPException as e:
        print('邮件发送失败，错误信息：', e)

    return ID, localtime

def page(random_num):
    instrunction()
    file = open(fr"filenames_{dataset}_after.txt", "r", encoding='utf-8') 
    file_list = file.readlines()
    file.close()

    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False
        
    for num in range(video_num):
        # 显示页面内容
        # st.write(f'这是第{num+1+random_num*video_num}个视频，名称为{file_list[num+random_num*video_num].rstrip()}')
        st.subheader(fr"Video {num+1}")
        video_bytes = play_video(file_list[num+random_num*video_num].rstrip())
        st.video(video_bytes)

        # st.write("Please answer the following questions, after you watch the video. ")
        st.write("看完视频后，请回答下面的问题。")
        QA(Lip_Sync, Motion_Flu, num+1)

    st.divider()
    
    if not st.session_state.button_clicked:
        if st.button("Submit results"):
            if any(x == "" for x in Lip_Sync or x == "" for x in Motion_Flu):
                st.warning("Please answer all questions before submitting the results.")
            if not any(x == "" for x in Lip_Sync or x == "" for x in Motion_Flu):
                st.write('It will take about 10 seconds, please be patient and wait. ')
                array = read_email_(myemail, password)
                array[random_num]+=1
                send_email(myemail, password, array)
                ID, localtime = data_collection(myemail, password, Lip_Sync, Motion_Flu, random_num, array)
                st.divider()
                st.markdown(':blue[请将以下结果截图！！！]')
                st.write("**Time of submission:** ", localtime)
                st.write("**Your results ID:** ", ID)
                lip = ''.join(Lip_Sync)
                motion = ''.join(Motion_Flu)
                st.write("**Lip_Sync:** ", lip)
                st.write("**Motion_Flu:** ", motion)
                st.session_state.button_clicked = True 

    if st.session_state.button_clicked == True:
        st.cache_data.clear()
        st.success("Successfully submitted the results. Thank you for using it. Now you can exit the system.")


if __name__ == '__main__':
    dataset = 'vocaset' 
    video_num = 18
    times = 3

    st.set_page_config(page_title="userstudy")
    #st.cache_data.clear() # 初始化
    myemail = st.secrets["my_email"]["email"]  
    password =  st.secrets["my_email"]["password"]
    
    array = read_email(myemail, password)
    #array = [0 for x in range(10)]
    if all((element == times or element > times) for element in array):
        array = [0] * random_range

    if "Lip_Sync" and "Motion_Flu" not in st.session_state:
        # 初始化data变量
        Lip_Sync = [1 for x in range(video_num)]
        Motion_Flu = [1 for x in range(video_num)]
    else:
        Lip_Sync = st.session_state["Lip_Sync"]
        Motion_Flu = st.session_state["Motion_Flu"]

    random_num = 0

    if 'random_num' not in st.session_state:
        st.session_state.random_num = random.randint(0, random_range-1)
        if array[st.session_state.random_num] == times or array[st.session_state.random_num] > times :
            while True:
                st.session_state.random_num = random.randint(0, random_range-1)
                if array[st.session_state.random_num] < times :
                    break

    random_num = st.session_state.random_num
    page(random_num)
