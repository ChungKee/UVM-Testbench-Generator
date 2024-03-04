#%%
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
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

    def CreateSmallComponent(self,x,y,name):
        left_inch = x
        top_inch = y
        width_inch = 0.15
        height_inch = 0.05 
        left   = self.prs.slide_width  * left_inch
        top    = self.prs.slide_height * top_inch
        width  = self.prs.slide_width  * width_inch
        height = self.prs.slide_height * height_inch
        oval   = self.slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        
        text_box = oval.text_frame
        text_box.text = name
        text_box.paragraphs[0].alignment = PP_ALIGN.CENTER

        fill = oval.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(0, 160, 0)

    def SavePowerPoint(self):
        # Save the presentation
        self.prs.save("my_presentation.pptx")
    
    def Run(self):
        self.CreateSlide()
        self.CreateSmallComponent(0.1, 0.1, "Scoreboard")
        self.CreateSmallComponent(0.1, 0.2, "Driver")
        self.CreateSmallComponent(0.1, 0.3, "Monitor")
        self.SavePowerPoint()

if __name__ == "__main__":
    prs = Presentation()
    MUP = MakeUVMPowerPoint()
    MUP.Run()

#%%





