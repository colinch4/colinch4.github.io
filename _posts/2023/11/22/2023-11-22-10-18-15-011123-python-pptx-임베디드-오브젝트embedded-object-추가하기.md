---
layout: post
title: "[python] python-pptx 임베디드 오브젝트(embedded object) 추가하기"
description: " "
date: 2023-11-22
tags: [python]
comments: true
share: true
---

python-pptx는 Python에서 PowerPoint 파일(.pptx)을 생성하고 편집할 수 있는 라이브러리입니다. 이 라이브러리를 사용하여 PowerPoint 파일에 임베디드 오브젝트를 추가하는 방법을 알아보겠습니다.

## 1. python-pptx 설치하기

python-pptx를 설치하기 위해 아래의 명령을 사용합니다.

```python
pip install python-pptx
```

## 2. 임베디드 오브젝트 추가하기

임베디드 오브젝트를 추가하기 위해 다음 단계를 따릅니다.

### 2.1. 라이브러리 임포트하기

```python
from pptx import Presentation
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import nsdecls
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
```

### 2.2. 프레젠테이션 생성하기

```python
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[0])
```

### 2.3. 임베디드 오브젝트 추가하기

```python
left = Inches(1)
top = Inches(1)
width = height = Inches(2)
shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)

# 임베디드 오브젝트 관련 속성 설정
# ex) shape.text = "Embedded Object"
#     shape.fill.solid()  # 배경색 설정
#     shape.fill.fore_color.rgb = RGBColor(255, 0, 0)  # RGB 색상 설정

# 임베디드 오브젝트 파일 경로 설정
embed_path = "path/to/your/embedded/object/file.xlsx"

rel = slide.part.relate_to(embed_path, RT.OLE_OBJECT)
embed = shape._element.get_or_add_picure_frame()
embed.nvPicPr.cNvPr._insert_nsdecls()

embed.nvPicPr.cNvPr.id = 6
embed.nvPicPr.cNvPr.name = 'Embedded Object'
embed.nvPicPr.cNvPr.descr = 'Embedded Object Description'
embed.nvPicPr.cNvPicPr._insert_nsdecls('a')
embed.nvPicPr.cNvPicPr.picLocks = 'a:extLst={}'.format(nsdecls('a'))

pic = embed.nvPicPr.cNvPicPr.append(CT_Picture())
pic._insert_nsdecls()
pic.nvPicPr = CT_PictureNonVisual()
pic.nvPicPr.cNvPr = CT_NonVisualDrawingProps()
pic.nvPicPr.cNvPr.id = 0
pic.nvPicPr.cNvPr.name = 'Picture 9'
pic.nvPicPr.cNvPr.descr = 'Python icon'

pic.nvPicPr.cNvPicPr = CT_NonVisualPictureProperties()
pic.nvPicPr.cNvPicPr.preferredHeight = 0
pic.nvPicPr.cNvPicPr.preferredWidth = 0

pic.blipFill = CT_BlipFillProperties()
pic.blipFill.blip = CT_Blip()
pic.blipFill.blip.embed = rel.reltype
pic.blipFill.stretch = CT_StretchInfoProperties()
pic.spPr = CT_ShapeProperties()
graphical_frame = shape._element.get_or_add_graphic_frame()
graphical_frame._insert_nsdecls('a')
```

### 2.4. 프레젠테이션 저장하기

```python
prs.save("path/to/save/presentation.pptx")
```

위의 단계를 따라서 python-pptx를 사용하여 PowerPoint 파일에 임베디드 오브젝트를 추가할 수 있습니다. 임베디드 오브젝트 파일로는 엑셀 파일(.xlsx) 등을 사용할 수 있으며, 파일 경로는 `embed_path` 변수에 지정하시면 됩니다.

더 자세한 내용은 python-pptx 문서([링크](https://python-pptx.readthedocs.io/))를 참고하시기 바랍니다.