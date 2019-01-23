import re

str_mail = """ uk5ay1p7jmiy3w4@inbox.ru viktoriya1988@inbox.ru mxcrkupzou@inprise.com
*@johoman.com 179qwfma@johoman.com cleywdmmozz@kame.net ocros@land.ru xekhqnhwwkk@libsdl.org
 6gfl3f@list.ru aefebrxpxv@list.ru ajtelkhuxf@list.ru bvtrlxehdk@list.ru bxtwguykpp@list.ru
 gpthznex@list.ru gyddhlmen@list.ru harda@list.ru hello2007@list.ru injn6b@list.ru jyxdtjyoom@list.ru
 kxgeqcitjj@list.ru lawpro-6045@list.ru mpbxgoalyb@list.ru nsibblulsj@list.ru onqondjujy@list.ru phffdisjrt@list.ru
 pw50ap3nl652wvj@list.ru vashareklama@list.ru pmj@lxe.com aliya_aliyeva@mail.ru AMSEnterprise@mail.ru anton.relkin@mail.ru
 ary.80@mail.ru corey-by@mail.ru detka_05@mail.ru diman_x777@mail.ru evjw45j7yfxlx0@mail.ru fedvs@mail.ru forforums2004@mail.ru
 gunsi@mail.ru hwnmmcjll3gcvsa@mail.ru info5jnmk5mzojf@mail.ru infoo1jc2ftw82c@mail.ru jurisan4ik_1@mail.ru
 kat5ntu5cwa6niz@mail.ru martin_1_6@mail.ru megmoba@mail.ru olga2000@mail.ru podranok1@mail.ru pridurok@mail.ru
 qiozqcfq@mail.ru qiu85d0jwp1i7r1@mail.ru qwert13_3@mail.ru rzx2mssfxixvvqs@mail.ru
 kat5ntu5cwa6niz@mail.ru martin_1_6@mail.ru megmoba@mail.ru olga2000@mail.ru podranok1@mail.ru pridurok@mail.ru
 qiozqcfq@mail.ru qiu85d0jwp1i7r1@mail.ru qwert13_3@mail.ru rzx2mssfxixvvqs@mail.ru
"""


def find_email(mail_string):
    res = re.findall(r'([*-\.\w]+@[-\w\.*]+[\.]\w+[\.]?[\w*]+)\s?', mail_string)
    return set(res)


print(find_email(str_mail))
