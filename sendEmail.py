import smtplib
 
def sendemail(from_addr = 'jatin.perl@gmail.com',
              to_addr_list = ['jatin.perl@gmail.com'],
              cc_addr_list = ['jatin.perl@gmail.com'],
              subject = 'Testing',
              message = 'Testing',
              login = 'abhishek.vijay04',
              password = "xxxxxx",
              smtpserver='smtp.gmail.com:587'):

    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

    
    return problems

sendemail()
