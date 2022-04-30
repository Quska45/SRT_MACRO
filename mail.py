import smtplib
from email.mime.text import MIMEText

# 세션 생성
s = smtplib.SMTP('smtp.gmail.com', 587)

# TLS 보안 시작
s.starttls()

# 로그인 인증
s.login('123', '123')

# 보낼 메시지 설정
msg = MIMEText('srt 예매 성공')
msg['Subject'] = 'srt 예매 성공'

# 메일 보내기
s.sendmail("qusrhkdwls45@gmail.com", "qusrhkdwls@sehyunict.com", msg.as_string())

# 세션 종료

s.quit()