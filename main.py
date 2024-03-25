import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import easyocr
import os
import chime
reader = easyocr.Reader(['en'])


plates_folder = 'plates/'


police_plates = ['WE 583CW',
                 'WE 574CW',
                 'WE 203EC',
                 'OP 26297',
                 'OP 25352',
                 'OB 34678',
                 'DZL TA72',
                 'DZL SW32',
                 'DZG H925',
                 'DZG E743',
                 'DZG E742',
                 'DZG E737',
                 'DZG E720',
                 'DZG E717',
                 'DZA 21NX',
                 'DWR 82546',
                 'DW 853LE',
                 'DW 809JC',
                 'DW 7691F',
                 'DW 731FU',
                 'DW 587ET',
                 'DW 48744',
                 'DW 485AG',
                 'DW 47910',
                 'DW 47901',
                 'DW 47654',
                 'DW 473ET',
                 'DW 47188',
                 'DW 47181',
                 'DW 47148',
                 'DW 422HS',
                 'DW 422HS',
                 'DW 400GG',
                 'DW 317GW',
                 'ME 027PS']
matched_plates = []
for filename in os.listdir(plates_folder):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        image_path = os.path.join(plates_folder, filename)
        output = reader.readtext(image_path)

        letters = []
        for word in output:
            text = word[1]
            for letter in text:
                letters.append(letter)

        for plate in police_plates:
            plate_letters = [char for char in plate if char != ' ']
            if len(plate_letters) == len(letters) and all(
                    plate_letters[i] == letters[i] for i in range(len(plate_letters))):
                matched_plates.append(plate)
                break

for plate in matched_plates:
    print(plate)




if matched_plates:
    chime.warning()

else:
    pass

