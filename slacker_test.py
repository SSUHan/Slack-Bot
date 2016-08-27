from slacker import Slacker

token = 'xoxb-72771591302-zfOyLVQB4KPdQCWOLfOpIGR6'
slack = Slacker(token)

attachments_dict = dict()
attachments_dict['pretext'] = "pretext:attachment 블록전에 나타나는 text"
attachments_dict['title'] = "title"
attachments_dict['title_link'] = "https://github.com/SSUHan"
attachments_dict['fallback'] = "fallback"
attachments_dict['text'] = "본문 text"
attachments_dict['text_link'] = "https://github.com/SSUHan"
attachments_dict['mrkdwn_in'] = ['text', 'pretext']
attachments = [attachments_dict, attachments_dict]

slack.chat.post_message('server-dev',text=None, attachments=attachments, as_user=True)
# slack.chat.post_message('server-dev', 'message', as_user=True)