#%%
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_VERTICAL_ANCHOR
from pptx.dml.color import RGBColor

class MakeUVMPowerPoint:
    def __init__(self) -> None:
        self.prs = Presentation()
        self.slide = None
        self.slide_layout = None

    def CreateSlide(self):
        # Add a slide
        self.slide_layout = self.prs.slide_layouts[0]  # Select a slide layout (0 is usually the title slide layout)
        self.slide = self.prs.slides.add_slide(self.slide_layout)

    def CreateComponent(self, x, y, width, height, name, 
                        shape = MSO_SHAPE.ROUNDED_RECTANGLE,
                        P_alignment = PP_ALIGN.CENTER,
                        color = RGBColor(0, 160, 0)):
        left   = self.prs.slide_width  * x
        top    = self.prs.slide_height * y
        width  = self.prs.slide_width  * width
        height = self.prs.slide_height * height
        oval   = self.slide.shapes.add_shape(shape, left, top, width, height)
        
        text_box = oval.text_frame
        text_box.text = name
        text_box.paragraphs[0].alignment = P_alignment
        text_box.vertical_anchor = MSO_VERTICAL_ANCHOR.TOP

        fill = oval.fill
        fill.solid()
        fill.fore_color.rgb = color
        return None

    def SavePowerPoint(self):
        # Save the presentation
        self.prs.save("my_presentation.pptx")
    
    def Run(self):
        self.CreateSlide()
        self.CreateComponent(x = 0.1, y = 0.1, width = 0.3, height = 0.2, name = "WriteAgent",
                             shape = MSO_SHAPE.RECTANGLE,
                             P_alignment = PP_ALIGN.LEFT)

        self.CreateComponent(x = 0.1, y = 0.7, width = 0.12, height = 0.05, name = "Driver")
        self.CreateComponent(x = 0.3, y = 0.7, width = 0.12, height = 0.05, name = "Monitor")

        self.CreateComponent(x = 0.425, y = 0.3, width = 0.15, height = 0.05, name = "Scoreboard")
        self.SavePowerPoint()

if __name__ == "__main__":
    
    MUP = MakeUVMPowerPoint()
    MUP.Run()

#%%





