from docx import Document
from docx.shared import Pt
from docx.shared import Inches
from docx.oxml.ns import qn

# 这个是放所有待修改的word文件的目录
dir_1 = "F:\\a"                           #C:\\Users\\visg\\Desktop\\4
filenames = os.listdir(dir_1)

document = Document()
document.styles['Normal'].font.name = u'宋体'
document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')