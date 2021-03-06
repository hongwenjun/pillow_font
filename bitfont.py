import base64
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

text = [ "!\"#$%&]'()*+,-./0123456789:;<=>?@",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`",
    "abcdefghijklmnopqrstuvwxyz{|}~"  ]

def load_default():
    """Load a "better than nothing" default font.
    .. versionadded:: 1.1.4
    :return: A font object.
    """
    f = ImageFont.load_default()
    return f

def load_fixedsys():
    """Load a "Fixedsys12.pil & Fixedsys12.pbm" Fixedsys font.
    .. versionadded:: 1.0.0
    :return: A font object.
    """
    f = ImageFont.load_default()
    f._load_pilfont_data(
        # courB08
        BytesIO(
            base64.b64decode(
                b"""
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
9AAIAAICxAAOAssAHA==
"""
            )
        ),
        Image.open(
            BytesIO(
                base64.b64decode(
                    b"""
iVBORw0KGgoAAAANSUhEUgAAAx8AAAAcAQAAAAAooz87AAADjElEQVR4nL2UXWgcVRiGn5lNN42s
bqJtnIvQLNIfqDadoDQ1rGTQG9sLyUUv0lJhatMYtJYoAbNpyB41bCMalBhvbCFrIpQYwUDBtL0o
A6lppS27vQnKts0WxSz+bkjMZjeZHS9mJ5mLBiNk+/LB+b7DOe/7/RwO5tkGy4Y5aFmWdcEOWk4m
lOTPwZOvW5H0vdCZme656TN5fwNdmcH8Qve2juOTmVhXJjvzSdBaDsbyp0s/6Mik1Y7Q0syVcN2P
sWDownJ3VTg4FwvOxYIl0odPY0Pq1YEKO3iqfVq6Le++ubekZ+TIoUvVUuD+o5sqh0YT5+uPv/AX
IJ1PnBriFbhadrtic9km7ZHPmyG6r2+8wtTGJSiPXRSp0cToaOJrmbWw/asSuDZgRnaC6vVyv29B
8DhEAfQtASAF+TZycqNJ8ig8Fv9SAJTvggXh408jZ1PJ1rvpAqvVAfC3Hdybrxqp2/Pq829CNq7x
BBpPlu6ObCUFKWC+HCwNqgMezLjZ1rhF5Z/ZJACnD0MGhbvibP/BHf0Hd8rWibgj0gpwyw6+aCO3
J8pzOXxJzzPS5Y8UVIa9VFJaJQnJICXplVFgadIEGmGyjYb3BUBWgzJqrwiaayd8tRM+2WM5lXgW
AcJ2kIe4EmQgCpp3KhSVvh9sRIffyP5SJyyNtKWl4yCd+9i+YOQ/BU+BKj/yhngtrHGu0K61RhLd
3qreAVDwGddR7iZT0uWcDwWSkmBxEXIprJq4khcwtmRcXAKT5NKNMb/xbZLf698zaB7sTA12pmSr
WnN4AwBXbX9Av9PeVchRMffrSEPzciTbDjoUpi8JpgpXe7KiNwv58Ns/vNM3K3rqd7V6XhR4j0WU
YxFFpkZ3ZqICeFdqyf10aBjY2+T/pvS78BG508O02Hr4WlivaCoVVtNCuGnhKPgtDRj7A4AWADIO
j5ODXOXMRH4Z4CU76IeWfbRQyNzBsy7fGYBx0179YlkHVB8AHSRWTsqoUTeLq5KpX5lyOuPglsvP
i4Kj2cusKAGIzwPQy/DqUXmb6mSmABywg0lQWB/SwRVXd++77q/9hNcr4uIyHry/9rdC6n+LmNqD
96XQqfFEMeytzuiqSqzwHW+07RfratfGQT6w47OiWE3SpaJO+IpihruSYrXIn/zPIxssUqx2XddX
NYrWLskoFrMLm/WHIFIWWPWL1i5LKxazC+7X9VC+lX8B2iISjTJo37QAAAAASUVORK5CYII=
"""
                )
            )
        ),
    )
    return f


def load_vcrmono():
    """Load a "VCRMono16.pil & VCRMono16.pbm"  VCR_OSD_MONO_1.001  font.
    .. versionadded:: 1.0.0
    :return: A font object.
    """
    f = ImageFont.load_default()
    f._load_pilfont_data(
        # courB08
        BytesIO(
            base64.b64decode(
                b"""
UElMZm9udAo7Ozs7OzsxOTsKREFUQQoAAAAAAAAAAAAAAAAAAAAAAAAAAAAOAAAAAP/tAA0AAAAA
AAAADQATAA4AAAAA/+0ADQAAAA0AAAAaABMADgAAAAD/7QANAAAAGgAAACcAEwAOAAAAAP/tAA0A
AAAnAAAANAATAA4AAAAA/+0ADQAAADQAAABBABMADgAAAAD/7QANAAAAQQAAAE4AEwAOAAAAAP/t
AA0AAABOAAAAWwATAA4AAAAA/+0ADQAAAFsAAABoABMADgAAAAD/7QANAAAAaAAAAHUAEwAOAAAA
AP/tAA0AAAB1AAAAggATAA4AAAAA/+0ADQAAAIIAAACPABMADgAAAAD/7QANAAAAjwAAAJwAEwAO
AAAAAP/tAA0AAACcAAAAqQATAA4AAAAA/+0ADQAAAKkAAAC2ABMADgAAAAD/7QANAAAAtgAAAMMA
EwAOAAAAAP/tAA0AAADDAAAA0AATAA4AAAAA/+0ADQAAANAAAADdABMADgAAAAD/7QANAAAA3QAA
AOoAEwAOAAAAAP/tAA0AAADqAAAA9wATAA4AAAAA/+0ADQAAAPcAAAEEABMADgAAAAD/7QANAAAB
BAAAAREAEwAOAAAAAP/tAA0AAAERAAABHgATAA4AAAAA/+0ADQAAAR4AAAErABMADgAAAAD/7QAN
AAABKwAAATgAEwAOAAAAAP/tAA0AAAE4AAABRQATAA4AAAAA/+0ADQAAAUUAAAFSABMADgAAAAD/
7QANAAABUgAAAV8AEwAOAAAAAP/tAA0AAAFfAAABbAATAAAAAAAAAAAAAQABAWwAAAFtAAEADgAA
AAD/7QANAAABbQAAAXoAEwAOAAAAAP/tAA0AAAF6AAABhwATAAwAAAAAAAAAAQABAYcAAAGIAAEA
DAAAAAT/8QAG//8BiAAAAYoADgAMAAAAAv/xAAr/9QGKAAABkgAEAAwAAAAB//EAC//+AZIAAAGc
AA0ADAAAAAH/8QAL//8BnAAAAaYADgAMAAAAAf/xAAv//wGmAAABsAAOAAwAAAAB/+8AC///AbAA
AAG6ABAADAAAAAT/8QAG//UBugAAAbwABAAMAAAAA//vAAj//wG8AAABwQAQAAwAAAAE/+8ACf//
AcEAAAHGABAADAAAAAL/8AAK//kBxgAAAc4ACQAMAAAAAf/zAAv//QHOAAAB2AAKAAwAAAAD//sA
B///AdgAAAHcAAQADAAAAAL/9wAK//kB3AAAAeQAAgAMAAAABP/9AAb//wHkAAAB5gACAAwAAAAB
//EAC///AeYAAAHwAA4ADAAAAAH/8QAL//8B8AAAAfoADgAMAAAAA//xAAn//wH6AAACAAAOAAwA
AAAB//EAC///AgAAAAIKAA4ADAAAAAH/8QAL//8CCgAAAhQADgAMAAAAAf/xAAv//wIUAAACHgAO
AAwAAAAB//EAC///Ah4AAAIoAA4ADAAAAAH/8QAL//8CKAAAAjIADgAMAAAAAf/xAAv//wIyAAAC
PAAOAAwAAAAB//EAC///AjwAAAJGAA4ADAAAAAH/8QAL//8CRgAAAlAADgAMAAAABP/zAAb//QJQ
AAACUgAKAAwAAAAC//MABv//AlIAAAJWAAwADAAAAAL/8AAJ//8CVgAAAl0ADwAMAAAAAf/1AAv/
+wJdAAACZwAGAAwAAAAC//AACf//AmcAAAJuAA8ADAAAAAH/8QAL//8CbgAAAngADgAMAAAAAf/x
AAv//gJ4AAACggANAAwAAAAB//EAC///AoIAAAKMAA4ADAAAAAH/8QAL//8CjAAAApYADgAMAAAA
Af/xAAv//wKWAAACoAAOAAwAAAAB//EAC///AqAAAAKqAA4ADAAAAAH/8QAL//8CqgAAArQADgAM
AAAAAf/xAAv//wK0AAACvgAOAAwAAAAB//EAC///Ar4AAALIAA4ADAAAAAH/8QAL//8CyAAAAtIA
DgAMAAAAA//xAAn//wLSAAAC2AAOAAwAAAAB//EAC///AtgAAALiAA4ADAAAAAH/8QAL//8C4gAA
AuwADgAMAAAAAf/xAAv//wLsAAAC9gAOAAwAAAAB//EAC///AvYAAAMAAA4ADAAAAAH/8QAL//8D
AAAAAwoADgAMAAAAAf/xAAv//wMKAAADFAAOAAwAAAAB//EAC///AxQAAAMeAA4ADAAAAAH/8QAL
//8AAAATAAoAIQAMAAAAAf/xAAv//wAKABMAFAAhAAwAAAAB//EAC///ABQAEwAeACEADAAAAAH/
8QAL//8AHgATACgAIQAMAAAAAf/xAAv//wAoABMAMgAhAAwAAAAB//EAC///ADIAEwA8ACEADAAA
AAH/8QAL//8APAATAEYAIQAMAAAAAf/xAAv//wBGABMAUAAhAAwAAAAB//EAC///AFAAEwBaACEA
DAAAAAH/8QAL//8AWgATAGQAIQAMAAAABP/vAAr//wBkABMAagAjAAwAAAAB//EAC///AGoAEwB0
ACEADAAAAAL/7wAI//8AdAATAHoAIwAMAAAAAf/xAAv/9gB6ABMAhAAYAAwAAAAA//4ADAAAAIQA
EwCQABUADAAAAAP/8QAI//QAkAATAJUAFgAMAAAAAf/zAAv//wCVABMAnwAfAAwAAAAB//EAC///
AJ8AEwCpACEADAAAAAH/9AAL//8AqQATALMAHgAMAAAAAf/xAAr//wCzABMAvAAhAAwAAAAB//QA
C///ALwAEwDGAB4ADAAAAAL/8QAK//8AxgATAM4AIQAMAAAAAf/zAAv//wDOABMA2AAfAAwAAAAB
//EAC///ANgAEwDiACEADAAAAAP/8gAJ//8A4gATAOgAIAAMAAAAA//wAAn//wDoABMA7gAiAAwA
AAAB//EAC///AO4AEwD4ACEADAAAAAX/8QAH//8A+AATAPoAIQAMAAAAAf/0AAv//wD6ABMBBAAe
AAwAAAAB//QAC///AQQAEwEOAB4ADAAAAAH/9AAL//8BDgATARgAHgAMAAAAAf/zAAv//wEYABMB
IgAfAAwAAAAB//MAC///ASIAEwEsAB8ADAAAAAH/9AAL//8BLAATATYAHgAMAAAAAf/0AAv//wE2
ABMBQAAeAAwAAAAD//EACf//AUAAEwFGACEADAAAAAH/9AAL//8BRgATAVAAHgAMAAAAAf/0AAv/
/wFQABMBWgAeAAwAAAAB//QAC///AVoAEwFkAB4ADAAAAAH/9AAL//8BZAATAW4AHgAMAAAAAf/z
AAv//wFuABMBeAAfAAwAAAAB//QAC///AXgAEwGCAB4ADAAAAAP/7wAJ//8BggATAYgAIwAMAAAA
Bf/vAAf//wGIABMBigAjAAwAAAAD/+8ACf//AYoAEwGQACMADAAAAAH/9gAL//oBkAATAZoAFwAM
AAAAAAAAAAEAAQGaABMBmwAUAAwAAAAB/+8AC///AZsAEwGlACMADAAAAAH/8QAL//8BpQATAa8A
IQAMAAAAAf/xAAv//wGvABMBuQAhAAwAAAAB//EAC///AbkAEwHDACEADAAAAAH/8QAL//8BwwAT
Ac0AIQAMAAAAAf/xAAv//wHNABMB1wAhAAwAAAAB//EAC///AdcAEwHhACEADAAAAAH/8QAL//8B
4QATAesAIQAMAAAAAf/xAAv//wHrABMB9QAhAAwAAAAB//EAC///AfUAEwH/ACEADAAAAAH/8QAL
//8B/wATAgkAIQAMAAAAAf/xAAv//wIJABMCEwAhAAwAAAAB//EAC///AhMAEwIdACEADAAAAAH/
8QAL//8CHQATAicAIQAMAAAAAf/xAAv//wInABMCMQAhAAwAAAAB//EAC///AjEAEwI7ACEADAAA
AAH/8QAL//8COwATAkUAIQAMAAAAAf/xAAv//wJFABMCTwAhAAwAAAAB//EAC///Ak8AEwJZACEA
DAAAAAH/8QAL//8CWQATAmMAIQAMAAAAAf/xAAv//wJjABMCbQAhAAwAAAAB//EAC///Am0AEwJ3
ACEADAAAAAH/8QAL//8CdwATAoEAIQAMAAAAAf/xAAv//wKBABMCiwAhAAwAAAAB//EAC///AosA
EwKVACEADAAAAAH/8QAL//8ClQATAp8AIQAMAAAAAf/xAAv//wKfABMCqQAhAAwAAAAB//EAC///
AqkAEwKzACEADAAAAAH/8QAL//8CswATAr0AIQAMAAAAAf/xAAv//wK9ABMCxwAhAAwAAAAB//EA
C///AscAEwLRACEADAAAAAH/8QAL//8C0QATAtsAIQAMAAAAAf/xAAv//wLbABMC5QAhAAwAAAAB
//EAC///AuUAEwLvACEADAAAAAH/8QAL//8C7wATAvkAIQAMAAAAAf/xAAv//wL5ABMDAwAhAAwA
AAAB//EAC///AwMAEwMNACEADAAAAAH/8QAL//8DDQATAxcAIQAMAAAAAf/xAAv//wAAACYACgA0
AAwAAAAB//EAC///AAoAJgAUADQADAAAAAH/8QAL//8AFAAmAB4ANAAMAAAAAf/xAAv//wAeACYA
KAA0AAwAAAAB//EAC///ACgAJgAyADQADAAAAAH/8QAL//8AMgAmADwANAAMAAAAAf/xAAv//wA8
ACYARgA0AAwAAAAB//EAC///AEYAJgBQADQADAAAAAH/8QAL//8AUAAmAFoANAAMAAAAAf/xAAv/
/wBaACYAZAA0AAwAAAAB//EAC///AGQAJgBuADQADAAAAAH/8QAL//8AbgAmAHgANAAMAAAAAf/x
AAv//wB4ACYAggA0AAwAAAAB//EAC///AIIAJgCMADQADAAAAAH/8QAL//8AjAAmAJYANAAMAAAA
Af/xAAv//wCWACYAoAA0AAwAAAAB//EAC///AKAAJgCqADQADAAAAAH/8QAL//8AqgAmALQANAAM
AAAAAf/xAAv//wC0ACYAvgA0AAwAAAAB//EAC///AL4AJgDIADQADAAAAAH/8QAL//8AyAAmANIA
NAAMAAAAAf/xAAv//wDSACYA3AA0AAwAAAAB//EAC///ANwAJgDmADQADAAAAAH/8QAL//8A5gAm
APAANAAMAAAAAf/xAAv//wDwACYA+gA0AAwAAAAB//EAC///APoAJgEEADQADAAAAAH/8QAL//8B
BAAmAQ4ANAAMAAAAAf/xAAv//wEOACYBGAA0AAwAAAAB//EAC///ARgAJgEiADQADAAAAAH/8QAL
//8BIgAmASwANAAMAAAAAf/xAAv//wEsACYBNgA0AAwAAAAB//EAC///ATYAJgFAADQADAAAAAH/
8QAL//8BQAAmAUoANAAMAAAAAf/xAAv//wFKACYBVAA0AAwAAAAB//EAC///AVQAJgFeADQADAAA
AAH/8QAL//8BXgAmAWgANAAMAAAAAf/xAAv//wFoACYBcgA0AAwAAAAB//EAC///AXIAJgF8ADQA
DAAAAAH/8QAL//8BfAAmAYYANAAMAAAAAf/xAAv//wGGACYBkAA0AAwAAAAB//EAC///AZAAJgGa
ADQADAAAAAH/8QAL//8BmgAmAaQANAAMAAAAAf/xAAv//wGkACYBrgA0AAwAAAAB//EAC///Aa4A
JgG4ADQADAAAAAH/8QAL//8BuAAmAcIANAAMAAAAAf/xAAv//wHCACYBzAA0AAwAAAAB//EAC///
AcwAJgHWADQADAAAAAH/8QAL//8B1gAmAeAANAAMAAAAAf/xAAv//wHgACYB6gA0AAwAAAAB//EA
C///AeoAJgH0ADQADAAAAAH/8QAL//8B9AAmAf4ANAAMAAAAAf/xAAv//wH+ACYCCAA0AAwAAAAB
//EAC///AggAJgISADQADAAAAAH/8QAL//8CEgAmAhwANAAMAAAAAf/xAAv//wIcACYCJgA0AAwA
AAAB//EAC///AiYAJgIwADQADAAAAAH/8QAL//8CMAAmAjoANAAMAAAAAf/xAAv//wI6ACYCRAA0
AAwAAAAB//EAC///AkQAJgJOADQADAAAAAH/8QAL//8CTgAmAlgANAAMAAAAAf/xAAv//wJYACYC
YgA0AAwAAAAB//EAC///AmIAJgJsADQADAAAAAH/8QAL//8CbAAmAnYANAAMAAAAAf/xAAv//wJ2
ACYCgAA0AAwAAAAB//EAC///AoAAJgKKADQADAAAAAH/8QAL//8CigAmApQANAAMAAAAAf/xAAv/
/wKUACYCngA0AAwAAAAB//EAC///Ap4AJgKoADQADAAAAAH/8QAL//8CqAAmArIANAAMAAAAAf/x
AAv//wKyACYCvAA0AAwAAAAB//EAC///ArwAJgLGADQADAAAAAH/8QAL//8CxgAmAtAANAAMAAAA
Af/xAAv//wLQACYC2gA0AAwAAAAB//EAC///AtoAJgLkADQADAAAAAH/8QAL//8C5AAmAu4ANAAM
AAAAAf/xAAv//wLuACYC+AA0AAwAAAAB//EAC///AvgAJgMCADQADAAAAAH/8QAL//8DAgAmAwwA
NAAMAAAAAf/xAAv//wMMACYDFgA0AAwAAAAB//EAC///AxYAJgMgADQADAAAAAH/8QAL//8AAAA5
AAoARwAMAAAAAf/xAAv//wAKADkAFABHAAwAAAAB//EAC///ABQAOQAeAEcADAAAAAH/8QAL//8A
HgA5ACgARwAMAAAAAf/xAAv//wAoADkAMgBHAAwAAAAB//EAC///ADIAOQA8AEcADAAAAAH/8QAL
//8APAA5AEYARwAMAAAAAf/xAAv//wBGADkAUABHAAwAAAAB//EAC///AFAAOQBaAEcAAAAAAAAA
AAABAAEAWgA5AFsAOg==
"""
            )
        ),
        Image.open(
            BytesIO(
                base64.b64decode(
                    b"""
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
+Cd/7SFjUnmieAAAAABJRU5ErkJggg==
"""
                )
            )
        ),
    )
    return f

def load_background():
    """Load a "50x50 Color Png image"
    :return: A image.
    """
    im = Image.open(
        BytesIO( 
            base64.b64decode( b"""
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

""" 
        ) 
    )
)
    return im

############################################################################



def run_example():
    from PIL import Image, ImageDraw, ImageFont
    import bitfont

    im = bitfont.load_background()
    (width, height) = (400, 310)
    im = im.resize((width, height))
    draw = ImageDraw.Draw(im)

    font = bitfont.load_fixedsys()
    draw.text((5, 10), "FontName: Fixedsys", (0, 255, 0),  font=font)
    draw.text((5, 30), bitfont.text[0], font=font)
    draw.text((5, 50), bitfont.text[1], (255, 0, 0), font=font)
    draw.text((5, 70), bitfont.text[2], (10, 10, 10),  font=font)
    font_fds = font

    font = bitfont.load_vcrmono()
    draw.text((5, 110), "FontName: VCRMono16.pil", (0, 255, 0),  font=font)
    draw.text((5, 130), bitfont.text[0], font=font)
    draw.text((5, 150), bitfont.text[1], (255, 0, 0), font=font)
    draw.text((5, 170), bitfont.text[2], (10, 10, 10),  font=font)
    font_vcr = font

    font = bitfont.load_default()
    draw.text((5, 200), "FontName: PIL_default", (0, 255, 0),  font=font)
    draw.text((5, 208), bitfont.text[0], font=font)
    draw.text((5, 216), bitfont.text[1], (255, 255, 0), font=font)
    draw.text((5, 224), bitfont.text[2], (10, 10, 10),  font=font)

    draw.text((5, 240), "load_background: 50x50 Color Png image", (255, 255, 0),  font=font_fds)
    draw.text((5, 255), "Fixedsys12.pil & Fixedsys12.pbm Fixedsys font.", (255, 255, 255),  font=font_fds)
    draw.text((5, 270), "VCRMono16.pil VCR_OSD_MONO font.", (128, 255, 128),  font=font_vcr)
    draw.text((5, 290), "a better than nothing default font.",  font=font)

    im.save("bitfont.png")
    im.show()

if __name__ == '__main__':
    run_example()