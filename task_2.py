import re

str_link = """
http://www.obrnadzor.gov.ru http://stat.edu.ru www.lexed.ru http://www.ru www.edu.ru http://ege.edu.ru www.ecsocman.edu.ru
http://www.law.edu.ru http://www.ict.edu.ru http://minedu.karelia.ru http://www.stavminobr.ru http://www.minomos.ru
http://www.vrnedu.ru http://www.edunso.ru http://edu.tomsk.gov.ru http://www.avorontcov.ru http://bogoslovie.pro/
http://www.vlgregedu.ru http://mon.tatarstan.ru http://www.wikipedia.com http://accounts.google.com http://redbookvo.volgawetlands.ru
http://www.okm.ru
http://www.fonetica.ru
http://sokolova-aa.ru ary.80@mail.ru corey-by@mail.ru detka_05@mail.ru diman_x777@mail.ru evjw45j7yfxlx0@mail.ru fedvs@mail.ru forforums2004@mail.ru
http://Lelang.ru
http://www.statgrad.org
http://www.in-class.ru http://babla.ru http://tutorweb.ru http://lotuscenter.ru http://math.hashcode.ru www.piligrim.com/
http://cdt.gidrotorf.org http://www.toonto.ru http://ouhmao.ru
http://poluroka.ru http://english-mania.ru www.spaces.ru http://GEO.koltyrin.ru http://mail.ru www.erudyt.ru
http://epicon.ru www.linguahouse.ru http://zvzd3d.ru http://www.shelk-put.com
http://testmath.ru http://reword.org  qiozqcfq@mail.ru qiu85d0jwp1i7r1@mail.ru qwert13_3@mail.ru rzx2mssfxixvvqs@mail.ru
www.ed.vseved.ru http://prutzkow.com/numbers/ http://www.reg.ru
http://cleve.ru http://water-rf.ru www.lang-land.com/"""


def replace_email_link(input_str):
    template = r'([\w]+:[/]+[-.\w]+[\.][\w]+[.]?[\w]*[.]?[\w]*|[www]+[\.][\w]+[.]?[-\w.]*[.]?[\w]*|[*-\.\w]+@[-\w\.*]+[\.]\w+[\.]?[\w*]+)'
    list_find = re.findall(template, input_str)
    for i in list_find:
        input_str = re.sub(i, len(i) * "*", input_str)
    return input_str


print(replace_email_link(str_link))
