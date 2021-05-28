import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from googleapiclient.discovery import build
from google.oauth2 import service_account

# read line from the .txt file
lines = open('artstation_links_copy.txt').readlines()

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options = options)

# looping from the end of a list
for line in lines[::-1]:
    url = line
    driver.get(url)
    
    try:
        role_not_fixed = driver.find_element_by_css_selector('div.wrapper-main').text
        role_fixed = role_not_fixed.split('\n')[1]
    except:
        role_fixed = None
    try:
        # looking for the word "at" and splitting text on that occurence. 
        word_at = ' at '
        before, keyword, after = role_fixed.partition(word_at)
        company_work_at = after.strip()
    except:
        company_work_at = None

    try:
        art_title = driver.find_element_by_css_selector('h1.h3').text
    except:
        art_title = None

    try:
        date_posted_not_fixed = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/aside/div/small[1]/i').text
        date_posted_fixed = date_posted_not_fixed.split(' ')[1:]
        date_posted = ' '.join(date_posted_fixed)
    except:
        date_posted = None

    try:
        number_likes = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/aside/div/ul/li[1]/as-likes/button/as-pluralize/span').text.replace(',', '')
    except:
        number_likes = '0'

    try:
        number_views = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/aside/div/ul/li[2]/as-pluralize/span').text.replace(',', '')
    except:
        number_views = '0'

    try:
        number_comments = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/aside/div/ul/li[3]/as-pluralize/span').text.replace(',', '')
    except:
        number_comments = '0'

    try:
        software_used_not_fixed = driver.find_element_by_css_selector('div.wrapper-main').text
        word = 'Software Used'
        # looking for the word "Software Used" and splitting text on that occurence. 
        before, keyword, after = software_used_not_fixed.partition(word)
        # looking for any occurence using regex
        pattern = re.findall('Blender|Photoshop|ZBrush|ScandyPro|Maya|Procreate|double shot espresso|Double Shot espresso|Double shot espresso|Nuke|Mari|Krakatoa|RealFlow|ArtFlow|Flash|Flame Painer|CrazyBump|Frost|FumeFX|Phoenix FD|Photoscan|ScansLibrary|Inkscape|GIMP|CRYENGINE|Frostbite Engine|MagicaVoxel|Black Magic Desing Fusion|Fusion 360|Coiffure|RealityCapture|FireAlpaca|Realtime Board|Dreams|Dreamweaver|Adobe Draw|Snowdrop|Final Draft|Hydra Renderer|zbursh|DragonBones|HDR Light Studio|CorelDRAW Graphics Studio|DragonFrame|SpeedTree|Illustrator Draw|Illust Studio|Adobe XD|Adobe Lightroom|Hair Strand Designer|trueSKY|Source Control|ArtRage|Sculptris|PFTrack|The Groove 3D|UNIGINE Engine|Character Creator|Acrobat|Gaea|Manga Studio|Game Textures|Sublime Text|RD-Textures|PolyBrush|Poliigon|InVision Draft|PureRef|Mischief|Yeti|Knald|TYFlow|UVLayout|Nomad Sculpt|Substance Painter|Substance Designer|FiberShop|Unreal Engine|After Effects|Lightroom|Octane Render|3DCoat|World Machine|3ds Max|V-Ray|Forest Pack|Ornatrix|Marvelous Designer|Arnold|Xgen|Cinema 4D|Mixer|Bridge|Marmoset Toolbag|Keyshot|RizomUV|Clarisse IFX|QuarkXPress|E-Cycles|iClone|X-Particles|SketchClub|RailClone|Cycles 4D|Qubicle|Sletchfab|Premiere|Lumion|Quixel|Quixel Mixer|Substance ALchemist|MightyBake|Modo|3Delight|AIR|Unity|Enscape|SOLIDWORKS Visualize|RenderMan|Verge3D|Thea Render|Mental Ray|Twinmotion|Maxwell Render|Redshift|Corona Renderer|Corona|Houdini|Mantra|Karma|formZ|Toolbag|LightWave 3D|Iray|LuxRender|YafaRay|FurryBall|FluidRay|Katana|Light Tracer Render|EEVEE|Cycles|LuxCoreRender|Raylectron|Radiance|Vegas Pro|SolidWorks|Rhinoceros|Moi3D|Moi|3dpeople|Python|PhotoLab 2|Shotgun|Photoshop Elements|Indigo Renderer|Gelato|Sketch App|SketchUp|AutoCAD|ArchiCAD|Mudbox|MudBox|Figma|Pixelmator|Zmodeler|R3DS Wrap|R3DS ZWRAP|TopoGun|Texturingxyz|xNormal|CLIP STUDIO PAINT|TVPaint|Megascans|Illustrator', after)
        # joining finded occurenceses on the new line
        software_used = '\n'.join(pattern)
    except:
        software_used = None

    try:
        tags_not_fixed = driver.find_element_by_css_selector('div.wrapper-main').text
        tags_fixed = tags_not_fixed.split('\n')[::-1][1].split('#')[1:]
        tags_final = '\n'.join(tags_fixed)
    except:
        tags_final = None
        
    # Watch this Google Sheets Python API tutorial: https://bit.ly/3bZZxd6
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'keys.json' # json keys from google cloud platform. 
    creds = None
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
    SAMPLE_SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID'
    service = build('sheets', 'v4', credentials = creds)
    sheet = service.spreadsheets()

    columns = [[role_fixed], [company_work_at], [date_posted], [number_views], [number_likes], [number_comments], [software_used], [tags_final], [art_title], [url]]
    request = service.spreadsheets().values().append(spreadsheetId = SAMPLE_SPREADSHEET_ID,
                                                     range = "Main!A2", valueInputOption = "USER_ENTERED",
                                                     body = {"majorDimension": "COLUMNS",
                                                             "values": columns}).execute()
    print(f'Writing: {request}')
    
    # deleting each line after it scraped. Note there's could be a better solution
    del lines[-1]
    open('artstation_links_copy.txt', 'w').writelines(lines)

driver.quit()
